import pandas as pd
from Bio import AlignIO
from pytools.persistent_dict import PersistentDict

### Required output files ###
rule all:
    input:
        "apr_evolution/sarcopterygii_phylogeny_suppl.treefile",
        "ancestral_reconstruction/ancestral_sequences.faa",
        "viz/panels/aprs_conservation.svg",
#        "viz/panels/natural_selection_regimes.svg",
        "viz/panels/aprs_flexibility.svg",
        "viz/panels/aprs_flexibility_profiles.svg",
#        "mutatex/mutations/apoa1_model0_checked_Repair/LA14/WT_apoa1_model0_checked_Repair_2_4.pd"


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

# Retain only sequences belonging to sarcopterygii species
rule filter_sarcopterygii_sequences:
    input:
        "apr_evolution/ensembl_sequences.faa"
    output:
        "apr_evolution/raw_sarcopterygii_sequences.faa"
    shell:
        "src/filter_sarcopterygii_sequences.py {input} {output}"

# Remove sequences too short or without start codon
rule filter_low_quality_sequences:
    input:
        "apr_evolution/raw_sarcopterygii_sequences.faa"
    output:
        "apr_evolution/sarcopterygii_sequences.faa"
    shell:
        "src/filter_bad_quality_sequences.py {input} {output}"

# Align protein sequences with MAFFT
rule mafft_protein_alignment:
    input:
        "apr_evolution/sarcopterygii_sequences.faa"
    output:
        "apr_evolution/sarcopterygii_mafft.faa"
    shell:
        """
        mafft --maxiterate 1000 --localpair \
        {input} >> {output}
        """

# Infer a protein phylogeny from the sarcopterygii alignment
rule infer_phylogeny:
    input:
        "apr_evolution/sarcopterygii_mafft.faa"
    params:
        "apr_evolution/sarcopterygii_phylogeny"
    output:
        "apr_evolution/sarcopterygii_phylogeny.treefile",
        "apr_evolution/sarcopterygii_phylogeny.state"
    shell:
        """
        iqtree -s {input} --prefix {params} \
        --ufboot 1000 --alrt 1000 -nt 4 --ancestral \
        -o Xenopus_tropicalis_ENSXETP00000008146,Leptobrachium_leishanense_ENSLLEP00000049402
        """

# Align protein sequences with ClustalO
rule clustalo_protein_alignment:
    input:
        "apr_evolution/sarcopterygii_sequences.faa"
    output:
        "apr_evolution/sarcopterygii_clustalo.faa"
    shell:
        """
        clustalo -i {input} -o {output}
        """

# Prepare a supplementary phylogeny based on the ClustalO alignment
rule infer_supplementary_phylogeny:
    input:
        "apr_evolution/sarcopterygii_clustalo.faa"
    params:
        "apr_evolution/sarcopterygii_phylogeny_suppl"
    output:
        "apr_evolution/sarcopterygii_phylogeny_suppl.treefile",
    shell:
        """
        iqtree -s {input} --prefix {params} \
        --ufboot 1000 --alrt 1000 -nt 4 \
        -o Xenopus_tropicalis_ENSXETP00000008146,Leptobrachium_leishanense_ENSLLEP00000049402
        """

# Retain only coding sequences matching the sequences present in the protein dataset
rule filter_cds_ensembl:
    input:
        "apr_evolution/ensembl_sequences.fna",
        "apr_evolution/sarcopterygii_sequences.faa"
    output:
        "apr_evolution/sarcopterygii_sequences.fna"
    shell:
        "src/filter_nucleotide_sequences.py {input} > {output}"

# Align nucleotide sequences with PAL2NAL
rule pal2nal_alignment:
    input:
        "apr_evolution/sarcopterygii_mafft.faa",
        "apr_evolution/sarcopterygii_sequences.fna"
    output:
        "apr_evolution/sarcopterygii_mafft.fna"
    shell:
        """
        pal2nal.pl {input} -output fasta > {output}
        """

# Trim out highly gapped positions
rule trim_nucleotide_alignment:
    input:
        "apr_evolution/sarcopterygii_mafft.fna"
    output:
        "apr_evolution/sarcopterygii_mafft_trimmed.fna"
    shell:
        "trimal -in {input} -out {output} -gt 0.05"

# Run FEL analysis
rule fel_analysis:
    input:
        "apr_evolution/sarcopterygii_mafft_trimmed.fna",
        "apr_evolution/sarcopterygii_phylogeny.treefile"
    output:
        "apr_evolution/sarcopterygii_fel.json"
    shell:
        "hyphy fel --alignment {input[0]} --tree {input[1]} --output {output}"

# Run FUBAR analysis
rule fubar_analysis:
    input:
        "apr_evolution/sarcopterygii_mafft_trimmed.fna",
        "apr_evolution/sarcopterygii_phylogeny.treefile"
    output:
        "apr_evolution/sarcopterygii_fubar.json"
    shell:
        """
        hyphy fubar --alignment {input[0]} --tree {input[1]} && \
        mv apr_evolution/sarcopterygii_mafft_trimmed.fna.FUBAR.json {output} && \
        rm apr_evolution/sarcopterygii_mafft_trimmed.fna.FUBAR.cache
        """

# Remove treefile node label for MEME
rule fix_treefile_meme:
    input:
        "apr_evolution/sarcopterygii_phylogeny.treefile"
    output:
        "apr_evolution/sarcopterygii_phylogeny_meme.treefile"
    shell:
        """
        sed -E 's/Node[0-9]*\///g' {input} > {output}
        """

# Run MEME analysis
rule meme_analysis:
    input:
        "apr_evolution/sarcopterygii_mafft_trimmed.fna",
        "apr_evolution/sarcopterygii_phylogeny_meme.treefile"
    output:
        "apr_evolution/sarcopterygii_meme.json"
    shell:
        """
        hyphy meme  --alignment {input[0]} --tree {input[1]} --outfile {output} &&\
        mv apr_evolution/sarcopterygii_mafft_trimmed.fna.MEME.json {output}
        """

# Parse FEL JSON results into CSV files
rule parse_fel:
    input:
        "apr_evolution/sarcopterygii_fel.json",
        "apr_evolution/sarcopterygii_mafft.faa"
    output:
        "apr_evolution/sarcopterygii_fel.csv"
    shell:
        """
        ./src/parse_hyphy_fel.py {input} gorilla
        """

# Parse FUBAR JSON results into CSV files
rule parse_fubar:
    input:
        "apr_evolution/sarcopterygii_fubar.json",
        "apr_evolution/sarcopterygii_mafft.faa"
    output:
        "apr_evolution/sarcopterygii_fubar.csv"
    shell:
        """
        ./src/parse_hyphy_fubar.py {input} gorilla
        """

# Parse MEME JSON results into CSV files
rule parse_meme:
    input:
        "apr_evolution/sarcopterygii_meme.json",
        "apr_evolution/sarcopterygii_mafft.faa"
    output:
        "apr_evolution/sarcopterygii_meme.csv"
    shell:
        """
        ./src/parse_hyphy_meme.py {input} gorilla
        """

# Aggregate HyPhy results
rule aggregate_hyphy_results:
    input:
        "apr_evolution/sarcopterygii_fel.csv",
        "apr_evolution/sarcopterygii_fubar.csv",
        "apr_evolution/sarcopterygii_meme.csv"
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
        "apr_evolution/sarcopterygii_sequences.faa"
    output:
        "apr_evolution/aprs_aggregation_scores.csv"
    shell:
        """
        ./src/run_tango.py {input} 12 20 {config[tango]} APR1 >> {output}
        ./src/run_tango.py {input} 51 59 {config[tango]} APR2 >> {output}
        ./src/run_tango.py {input} 65 73 {config[tango]} APR3 >> {output}
        ./src/run_tango.py {input} 225 233 {config[tango]} APR4 >> {output}
        rm nt=N.txt
        """

### Calculate sequence entropy ###
rule calc_shannon_entropy:
    input:
        "apr_evolution/sarcopterygii_mafft.faa"
    output:
        "apr_evolution/aprs_entropy.csv"
    shell:
        "src/calc_shannon_entropy.py {input} >> {output}"

### Flexibility evolution ###

# Reconstruct ancestral sequences from IQ-Tree states file
rule reconstruct_ancestral_sequences:
    input:
        "apr_evolution/sarcopterygii_phylogeny.state",
        "apr_evolution/sarcopterygii_phylogeny.treefile",
        "apr_evolution/sarcopterygii_mafft.faa"
    output:
        "ancestral_reconstruction/ancestral_sequences.faa"
    shell:
        """
        src/get_ancestral_sequence.py {input} >> {output} &&
        mv *.svg ancestral_reconstruction/
        """

# Species used for structural comparisons
TARGETS = ["Homo_sapiens_ENSP00000364472",
           "Mus_musculus_ENSMUSP00000034588",
           "Crocodylus_porosus_ENSCPRP00005000967",
           "Gallus_gallus_ENSGALP00000011510"]

# Extrac target sequences to be structurally modelled
rule extract_target_sequences:
    input:
        "apr_evolution/sarcopterygii_sequences.faa"
    params:
        targets=expand("{targets}", targets=TARGETS)
    output:
        "ancestral_reconstruction/target_sequences.faa"
    run:
        for target in params.targets:
            shell("grep -A 1 {target} {input} >> {output}")

# Merge ancestral and extant sequences
#rule merge_sequences:
#    input:
#        "ancestral_reconstruction/ancestral_sequences.faa",
#        "ancestral_reconstruction/extant_sequences.faa"
#    output:
#        "ancestral_reconstruction/all_sequences.faa"
#    shell:
#        "cat {input} > {output}"

# Align protein sequences with MAFFT
rule mafft2_protein_alignment:
    input:
        "ancestral_reconstruction/target_sequences.faa"
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
        "ancestral_reconstruction/{target}_best_model.pdb"
    shell:
        "./src/run_modeller.py Homo_sapiens_ENSP00000364472 {input}"

# Model refinement (energy minimization)
rule model_refinement:
    input:
        "ancestral_reconstruction/{target}_best_model.pdb",
    output:
        "ancestral_reconstruction/{target}_best_model_relaxed.pdb"
    shell:
        """
        ./src/pyrosetta_fastrelax.py {input}
        """

# Compute MSF for each model
rule compute_msf:
    input:
        "ancestral_reconstruction/{target}_best_model_relaxed.pdb",
    output:
        "ancestral_reconstruction/{target}_best_model_relaxed.msf"
    shell:
        """
        ./src/calc_gnm.py {input}
        """

#  Compute WCN for each model
rule compute_wcn:
    input:
        "ancestral_reconstruction/{target}_best_model_relaxed.pdb",
    output:
        "ancestral_reconstruction/{target}_best_model_relaxed.wcn"
    shell:
        """
        python ./src/calc_wcn.py {input}
        """

# Aggregate MSF values
rule aggregate_msf:
    input:
        expand("ancestral_reconstruction/{target}_best_model_relaxed.msf", target=TARGETS)
    output:
        "ancestral_reconstruction/msf.csv"
    shell:
        "paste {input} > {output}"

# Aggregate WCN values
rule aggregate_wcn:
    input:
        expand("ancestral_reconstruction/{target}_best_model_relaxed.wcn", target=TARGETS)
    output:
        "ancestral_reconstruction/wcn.csv"
    shell:
        "paste {input} > {output}"


### MutateX in-silico mutagenesis ###

# Create MutateX configuration files
rule prepare_mutatex_templates:
    input:
        "apoa1.pdb"
    output:
        "mutatex_mutagenesis/mutate_runfile_template.txt",
        "mutatex_mutagenesis/repair_runfile_template.txt"
    run:
        with open(output[0], "w") as fh:
            fh.write("""command=BuildModel
pdb=$PDBS$
mutant-file=individual_list.txt
water=-CRYSTAL
numberOfRuns=$NRUNS$
complexWithDNA=true
""")
        with open(output[1], "w") as fh:
            fh.write("""command=RepairPDB
pdb=$PDBS$

temperature=298
water=-CRYSTAL
complexWithDNA=true
""")

# MutateX Mutagenesis
rule mutatex_mutagenesis:
    input:
        "apoa1.pdb",
        "mutatex_mutagenesis/mutate_runfile_template.txt",
        "mutatex_mutagenesis/repair_runfile_template.txt"
    params:
        "mutatex_mutagenesis",
        "/home/tmasson/foldx/foldx"
    output:
        "mutatex/mutations/apoa1_model0_checked_Repair/LA14/WT_apoa1_model0_checked_Repair_2_4.pd"
    shell:
        """
        cp {input[0]} {params[0]}/
        cd {params[0]}
        mutatex -f suite5 -x {params[1]} --np 4 {input[0]}
        """


### Plots generation ###

# APRs evolution plotting
rule plot_aprs_evolution:
    input:
        "apr_evolution/aprs_aggregation_scores.csv",
        "apr_evolution/aprs_entropy.csv",
        "apr_evolution/sarcopterygii_mafft.faa"
    output:
        "viz/panels/aprs_conservation.svg"
    params:
        "aprs_conservation.svg"
    shell:
        """
        ./viz/src/plot_apr_evolution.py {input} &&\
        mv {params} viz/panels/
        """

# HyPhy selection regimes plotting
rule plot_hyphy_evolution:
    input:
        "apr_evolution/hyphy_results.csv"
    output:
        "viz/panels/natural_selection_regimes.svg"
    params:
        "natural_selection_regimes.svg"
    shell:
        """
        ./viz/src/plot_hyphy_selection.py {input} &&\
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
