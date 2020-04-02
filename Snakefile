# Data Tidying

rule merge_sequences:
    input:
        "data/sequences_ensembl.faa",
        "data/sequences_refseq.faa"
    output:
        "data/raw_sequences_dataset.faa"
    shell:
        "cat {input} > {output}"

rule sequence_filtering:
    input:
        "data/raw_sequences_dataset.faa"
    output:
        "data/raw_sequences_dataset.faa_filtered"
    script:
        "src/sequence_filtering.py"

rule cdhit_clustering:
    input:
        "data/raw_sequences_dataset.faa_filtered"
    output:
        "data/sequences_dataset.faa"
    shell:
        "cd-hit -i {input} -o {output}"

# Evolutionary Analysis

rule mafft_alignment:
    input:
        "data/sequences_dataset.faa"
    output:
        "molecular_evolution/results/sequences_aln.faa"
    shell:
        "mafft {input} >> {output}"

rule iqtree_phylogeny:
    input:
        "

#rule hyphy_fubar

#rule hyphy_meme
