# Target files
rule all:
    input:
        "molecular_evolution/APOA1_phylogeny.treefile",
        "molecular_evolution/hyphy/hyphy_gard.json",
        "molecular_evolution/hyphy/hyphy_fel.json",
        "molecular_evolution/hyphy/hyphy_fubar.json",
        "molecular_evolution/hyphy/hyphy_leisr.json"

# Data Tidying

rule merge_sequences:
    input:
        "data/sequences_refseq.faa",
        "data/sequences_ensembl.faa"
    output:
        "data/raw_sequences_dataset.faa"
    shell:
        "cat {input} > {output}"

rule sequence_filtering:
    input:
        "data/raw_sequences_dataset.faa"
    output:
        "data/filtered_sequences_dataset.faa"
    shell:
        "src/filter_sequences.py {input}"

rule cdhit_clustering:
    input:
        "data/filtered_sequences_dataset.faa"
    output:
        "data/sequences_dataset.faa"
    shell:
        "cd-hit -i {input} -o {output} -c 0.98 "

rule add_names_sequences:
    input:
        "data/sequences_dataset.faa",
        "data/identifiers_species_table"
    output:
        "data/sequences_dataset_labeled.faa"
    shell:
        "src/rename_sequences.py {input}"

# Coding sequences fetching

rule get_cds_refseq:
    input:
        "data/sequences_dataset.faa",
    output:
        "data/raw_cds_refseq.fna"
    shell:
        "egrep 'XP_|NP_' {input} | " 
        "awk '{{print substr($1,2)}}' | "
        "epost -db protein | "
        "efetch -format fasta_cds_na > {output}"

rule fix_refseq_headers:
    input:
        "data/raw_cds_refseq.fna"
    output:
        "data/cds_refseq.fna"
    shell:
        "src/fix_refseq_header.py {input} > {output}"

rule filter_cds_ensembl:
    input:
        "data/raw_cds_ensembl.fna",
        "data/sequences_dataset.faa"
    output:
        "data/cds_ensembl.fna"
    shell:
        "src/filter_cds_ensembl.py {input} > {output}"

rule merge_cds_sequences:
    input:
        "data/cds_ensembl.fna",
        "data/cds_refseq.fna"
    output:
        "data/cds_dataset.fna"
    shell:
        "cat {input} > {output}"

rule add_names_cds:
    input:
        "data/cds_dataset.fna",
        "data/identifiers_species_table"
    output:
        "data/cds_dataset_labeled.fna"
    shell:
        "src/rename_sequences.py {input}"

# Evolutionary Analysis

rule mafft_alignment:
    input:
        "data/sequences_dataset_labeled.faa"
    output:
        "molecular_evolution/APOA1_alignment.faa"
    shell:
        "clustalo -i {input} -o {output}"

rule iqtree_phylogeny:
    input:
        "molecular_evolution/APOA1_alignment.faa"
    output:
        "molecular_evolution/APOA1_phylogeny.treefile"
    params:
        "molecular_evolution/APOA1_phylogeny"
    shell:
        "iqtree -s {input} -bb 1000 -nt 4 -pre {params} -redo"

rule cds_alignment:
    input:
        "molecular_evolution/APOA1_alignment.faa",
        "data/cds_dataset_labeled.fna"
    output:
        "molecular_evolution/cds_alignment.fna"
    shell:
        "pal2nal.pl {input} -output fasta > {output}"

rule hyphy_gard:
    input:
        align="molecular_evolution/cds_alignment.fna"
    output:
        "molecular_evolution/hyphy/hyphy_gard.json"
    shell:
        "hyphy gard --alignment {input.align} &&"
        "mv molecular_evolution/cds_alignment.fna.GARD.json {output}"

rule hyphy_fel:
    input:
        align="molecular_evolution/cds_alignment.fna",
        tree="molecular_evolution/APOA1_phylogeny.treefile"
    output:
        "molecular_evolution/hyphy/hyphy_fel.json"
    shell:
        "hyphy fel --alignment {input.align} --tree {input.tree} &&"
        "mv molecular_evolution/cds_alignment.fna.FEL.json {output}"

rule hyphy_fubar:
    input:
        align="molecular_evolution/cds_alignment.fna",
        tree="molecular_evolution/APOA1_phylogeny.treefile"
    output:
        "molecular_evolution/hyphy/hyphy_fubar.json"
    shell:
        "hyphy fubar --alignment {input.align} --tree {input.tree} &&"
        "mv molecular_evolution/cds_alignment.fna.FUBAR.json {output}"

rule hyphy_leisr:
    input:
        align="molecular_evolution/APOA1_alignment.faa",
        tree="molecular_evolution/APOA1_phylogeny.treefile"
    output:
        "molecular_evolution/hyphy/hyphy_leisr.json"
    shell:
        "hyphy leisr --alignment {input.align} --tree {input.tree} &&"
        "mv molecular_evolution/APOA1_alignment.faa.LEISR.json {output}"

