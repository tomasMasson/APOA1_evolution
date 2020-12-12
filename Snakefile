import pandas as pd
from Bio import AlignIO

# Species used for structural comparisons
NODES = ["Node10", "Node15", "Node92", "Node99"]
EXTANTS = ["Gorilla_gorilla_ENSGGOP00000033442",
           "Mus_musculus_ENSMUSP00000034588",
           "Crocodylus_porosus_ENSCPRP00005000967",
           "Gallus_gallus_ENSGALP00000011510"]
TARGETS = NODES + EXTANTS

### Required output files ###
rule all:
    input:
        expand("ancestral_reconstruction/{target}/best_model.pdb", target=TARGETS),
        expand("ancestral_reconstruction/{target}/best_model.msf", target=TARGETS),
        expand("ancestral_reconstruction/{target}/best_model.wcn", target=TARGETS),
        "viz/panels/aprs_conservation.svg",
        "viz/panels/natural_selection_regimes.svg",
        "viz/panels/aprs_flexibility.svg",
        "viz/panels/aprs_flexibility_profiles.svg"


### APRs evolution ###

# Get apoa1 protein ortholog sequences from ensembl
rule get_protein_sequences:
    input:
    output:
        "apr_evolution/ensembl_sequences.faa"
    shell:
        "src/get_ensembl_sequences.py protein {output}"

# Get apoa1 nucleotide ortholog sequences from ensembl
rule get_nucleotide_sequences:
    input:
    output:
        "apr_evolution/ensembl_sequences.fna"
    shell:
        "src/get_ensembl_sequences.py nucleotide {output}"

# Remove sequences too short or without start codon
rule sequences_filtering:
    input:
        "apr_evolution/ensembl_sequences.faa"
    output:
        temp("apr_evolution/vertebrates_sequences_filt.faa")
    shell:
        "src/filter_sequences.py {input} {output}"

# Cluster together sequences at 98% of identity
rule sequences_clustering:
    input:
        "apr_evolution/vertebrates_sequences_filt.faa"
    output:
        "apr_evolution/vertebrates_sequences.faa"
    shell:
        "cd-hit -i {input} -o {output} -c 0.98"

# Align protein sequences with MAFFT
rule mafft_protein_alignment:
    input:
        "apr_evolution/vertebrates_sequences.faa"
    output:
        "apr_evolution/vertebrates_mafft.faa"
    shell:
        """
        mafft --maxiterate 1000 --localpair \
        {input} >> {output}
        """

# Trim out highly gapped positions
rule trim_protein_alignment:
    input:
        "apr_evolution/vertebrates_mafft.faa"
    output:
        "apr_evolution/vertebrates_mafft_trimmed.faa"
    shell:
        "trimal -in {input} -out {output} -gt 0.05"

# Infer a protein phylogeny from the vertebrates alignment
rule infer_phylogeny:
    input:
        "apr_evolution/vertebrates_mafft_trimmed.faa"
    params:
        "apr_evolution/vertebrates_phylogeny"
    output:
        "apr_evolution/vertebrates_phylogeny.treefile"
    shell:
        """
        iqtree -s {input} --prefix {params} \
        -B 1000 --alrt 1000 -nt 4 --ancestral
        """

# Retain only coding sequences matching the sequences present in the protein dataset
rule filter_cds_ensembl:
    input:
        "apr_evolution/ensembl_sequences.fna",
        "apr_evolution/vertebrates_sequences.faa"
    output:
        "apr_evolution/vertebrates_sequences.fna"
    shell:
        "src/filter_cds_ensembl.py {input} > {output}"

# Align nucleotide sequences with PAL2NAL
rule pal2nal_alignment:
    input:
        "apr_evolution/vertebrates_mafft.faa",
        "apr_evolution/vertebrates_sequences.fna"
    output:
        "apr_evolution/vertebrates_mafft.fna"
    shell:
        """
        pal2nal.pl {input} -output fasta > {output}
        """

# Trim out highly gapped positions
rule trim_nucleotide_alignment:
    input:
        "apr_evolution/vertebrates_mafft.fna"
    output:
        "apr_evolution/vertebrates_mafft_trimmed.fna"
    shell:
        "trimal -in {input} -out {output} -gt 0.05"

# Run FEL analysis
rule fel_analysis:
    input:
        "apr_evolution/vertebrates_mafft_trimmed.fna",
        "apr_evolution/vertebrates_phylogeny.treefile"
    output:
        "apr_evolution/vertebrates_fel.json"
    shell:
        "hyphy fel --alignment {input[0]} --tree {input[1]} --output {output}"

# Run FUBAR analysis
rule fubar_analysis:
    input:
        "apr_evolution/vertebrates_mafft_trimmed.fna",
        "apr_evolution/vertebrates_phylogeny.treefile"
    output:
        "apr_evolution/vertebrates_fubar.json"
    shell:
        """
        hyphy fubar --alignment {input[0]} --tree {input[1]} && \
        mv apr_evolution/vertebrates_mafft_trimmed.fna.FUBAR.json {output} && \
        rm apr_evolution/vertebrates_mafft_trimmed.fna.FUBAR.cache
        """

# Remove treefile node label for MEME
rule fix_treefile_meme:
    input:
        "apr_evolution/vertebrates_phylogeny.treefile"
    output:
        "apr_evolution/vertebrates_phylogeny_meme.treefile"
    shell:
        """
        sed -E 's/Node[0-9]*\///g' {input} > {output}
        """

# Run MEME analysis
rule meme_analysis:
    input:
        "apr_evolution/vertebrates_mafft_trimmed.fna",
        "apr_evolution/vertebrates_phylogeny_meme.treefile"
    output:
        "apr_evolution/vertebrates_meme.json"
    shell:
        """
        hyphy meme  --alignment {input[0]} --tree {input[1]} --outfile {output} &&\
        mv apr_evolution/vertebrates_mafft_trimmed.fna.MEME.json {output}
        """

# Parse FEL JSON results into CSV files
rule parse_fel:
    input:
        "apr_evolution/vertebrates_fel.json",
        "apr_evolution/vertebrates_mafft_trimmed.faa"
    output:
        "apr_evolution/vertebrates_fel.csv"
    shell:
        """
        ./src/parse_hyphy_fel.py {input} gorilla
        """

# Parse FUBAR JSON results into CSV files
rule parse_fubar:
    input:
        "apr_evolution/vertebrates_fubar.json",
        "apr_evolution/vertebrates_mafft_trimmed.faa"
    output:
        "apr_evolution/vertebrates_fubar.csv"
    shell:
        """
        ./src/parse_hyphy_fubar.py {input} gorilla
        """

# Parse MEME JSON results into CSV files
rule parse_meme:
    input:
        "apr_evolution/vertebrates_meme.json",
        "apr_evolution/vertebrates_mafft_trimmed.faa"
    output:
        "apr_evolution/vertebrates_meme.csv"
    shell:
        """
        ./src/parse_hyphy_meme.py {input} gorilla
        """

# Aggregate HyPhy results
rule aggregate_hyphy_results:
    input:
        "apr_evolution/vertebrates_fel.csv",
        "apr_evolution/vertebrates_fubar.csv",
        "apr_evolution/vertebrates_meme.csv"
    output:
        "apr_evolution/hyphy_results.csv"
    run :
        # Read all inputs as Pandas DataFrames
        df_fel = pd.read_csv(input[0])    
        df_fubar = pd.read_csv(input[1])    
        df_meme = pd.read_csv(input[2])    
        # Save columns with the selection regime data
        dic = { "FEL": df_fel["Selection_type"],
                "FUBAR": df_fubar["Selection_type"],
                "MEME": df_meme["Episodic Selection"]}
        # Save data to output file
        df = pd.DataFrame(dic)
        df.to_csv(output[0], index=False, header=True)


### APR aggregation prediction ###

# Predict aggregation propensity with Tango
rule run_tango_predictions:
    input:
        "apr_evolution/vertebrates_mafft_trimmed.faa",
        "/home/tmasson/Tango/tango_x86_64_release"
    output:
        "apr_evolution/aprs_aggregation_scores.csv"
    shell:
        """
        ./src/run_tango.py {input} 54 62 APR1 >> {output}
        ./src/run_tango.py {input} 93 101 APR2 >> {output}
        ./src/run_tango.py {input} 107 115 APR3 >> {output}
        ./src/run_tango.py {input} 267 275 APR4 >> {output}
        rm nt=N.txt
        """


### Calculate sequence entropy ###
rule calc_shannon_entropy:
    input:
        "apr_evolution/vertebrates_mafft_trimmed.faa"
    output:
        "apr_evolution/aprs_entropy.csv"
    shell:
        "src/calc_shannon_entropy.py {input} >> {output}"

### Flexibility evolution ###

# Reconstruct ancestral sequences from IQ-Tree states file
rule extract_ancestral_sequences:
    input:
        "apr_evolution/vertebrates_phylogeny.state"
    params:
        nodes=expand("{nodes}", nodes=NODES)
    output:
        "ancestral_reconstruction/ancestral_sequences.faa"
    run:
        for node in params.nodes:
            shell("""
                  ./src/get_ancestral_sequence.py {input} {node} >> {output} &&\
                  mv *.svg ancestral_reconstruction/
                  """)

# Add Human, Mouse, Chicken and Crocodrillus sequences
rule add_extant_sequences:
    input:
        "apr_evolution/vertebrates_sequences.faa"
    params:
        extants=expand("{extants}", extants=EXTANTS)
    output:
        "ancestral_reconstruction/extant_sequences.faa"
    run:
        for extant in params.extants:
            shell("grep -A 1 {extant} {input} >> {output}")

# Merge ancestral and extant sequences
rule merge_sequences:
    input:
        "ancestral_reconstruction/ancestral_sequences.faa",
        "ancestral_reconstruction/extant_sequences.faa"
    output:
        "ancestral_reconstruction/all_sequences.faa"
    shell:
        "cat {input} > {output}"

# Align protein sequences with MAFFT
rule mafft2_protein_alignment:
    input:
        "ancestral_reconstruction/all_sequences.faa"
    output:
        "ancestral_reconstruction/alignment.faa"
    shell:
        """
        mafft --maxiterate 1000 --localpair \
        {input} >> {output}
        """

# Trim signal peptide from alignment
rule trim_signal_peptide:
    input:
        "ancestral_reconstruction/alignment.faa"
    output:
        "ancestral_reconstruction/alignment_trimmed.faa"
    run:
        align = AlignIO.read(input[0], "fasta")
        align_trimmed = align[:, 24:]
        with open (output[0], "w") as fh:
            for seq in align_trimmed:
                fh.write(f">{seq.id}\n{seq.seq}\n")

# Create protein models with Modeller
rule protein_modelling:
    input:
        "ancestral_reconstruction/alignment_trimmed.faa",
        "apoa1.pdb",
    output:
        "ancestral_reconstruction/{target}/best_model.pdb"
    shell:
        "./src/run_modeller.py Gorilla_gorilla_ENSGGOP00000033442 {wildcards.target} {input}"

# Compute MSF for each model
rule compute_msf:
    input:
        "ancestral_reconstruction/{target}/best_model.pdb"
    output:
        "ancestral_reconstruction/{target}/best_model.msf"
    shell:
        "./src/calc_gnm.py {input} -o {wildcards.target} > {output}"

# Compute WCN for each model
rule compute_wcn:
    input:
        "ancestral_reconstruction/{target}/best_model.pdb"
    output:
        "ancestral_reconstruction/{target}/best_model.wcn"
    shell:
        "python ./src/calc_wcn.py {input} -o {wildcards.target} > {output}"

# Aggregate MSF values
rule aggregate_msf:
    input:
        expand("ancestral_reconstruction/{target}/best_model.msf", target=TARGETS)
    output:
        "ancestral_reconstruction/msf.csv"
    shell:
        "paste {input} > {output}"

# Aggregate WCN values
rule aggregate_wcn:
    input:
        expand("ancestral_reconstruction/{target}/best_model.wcn", target=TARGETS)
    output:
        "ancestral_reconstruction/wcn.csv"
    shell:
        "paste {input} > {output}"


### Plots generation ###

# APRs evolution plotting
rule plot_aprs_evolution:
    input:
        "apr_evolution/aprs_aggregation_scores.csv",
        "apr_evolution/aprs_entropy.csv",
        "apr_evolution/hyphy_results.csv"
    output:
        "viz/panels/aprs_conservation.svg",
        "viz/panels/natural_selection_regimes.svg"
    params:
        "aprs_conservation.svg",
        "natural_selection_regimes.svg"
    shell:
        """
        ./viz/src/plot_apr_evolution.py {input} &&\
        mv {params} viz/panels/
        """

# MSF and WCN plotting
rule plot_aprs_msf_wcn:
    input:
        "ancestral_reconstruction/msf.csv",
        "ancestral_reconstruction/wcn.csv"
    output:
        "viz/panels/aprs_flexibility.svg",
        "viz/panels/aprs_flexibility_profiles.svg"
    params:
        "aprs_flexibility.svg",
        "aprs_flexibility_profiles.svg"
    shell:
        """
        ./viz/src/plot_msf_wcn.py {input} &&\
        mv {params} viz/panels/
        """
