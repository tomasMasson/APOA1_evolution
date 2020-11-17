# Set apoa1 alignments as target file
rule all:
    input:
        "apr_evolution/vertebrates_mafft_trimmed.aln"


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
rule sequence_filtering:
    input:
        "apr_evolution/ensembl_sequences.faa"
    output:
        "apr_evolution/vertebrates_sequences.faa"
    shell:
        "src/filter_sequences.py {input} {output}"

# Retain only coding sequences matching the sequences present in the protein dataset
rule filter_cds_ensembl:
    input:
        "apr_evolution/ensembl_sequences.fna",
        "apr_evolution/vertebrates_sequences.faa"
    output:
        "apr_evolution/vertebrates_sequences.fna"
    shell:
        "src/filter_cds_ensembl.py {input} > {output}"

# Align protein sequences with MAFFT
rule mafft_alignment:
    input:
        "apr_evolution/vertebrates_sequences.faa"
    output:
        "apr_evolution/vertebrates_mafft.aln"
    shell:
        """
        mafft --maxiterate 1000 --localpair \
        {input} >> {output}
        """
# Trim out highly gapped positions
rule trim_alignment:
    input:
        "apr_evolution/vertebrates_mafft.aln"
    output:
        "apr_evolution/vertebrates_mafft_trimmed.aln"
    shell:
        "trimal -in {input} -out {output} -gt 0.06"
