# Set apoa1 alignments as target file
rule all:
    input:
        "apr_evolution/vertebrates_fel.csv",
        "apr_evolution/vertebrates_fubar.csv",
        "apr_evolution/vertebrates_meme.csv"

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

# Parse HyPhy results
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
