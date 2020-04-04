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
        "cd-hit -i {input} -o {output}"

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

rule get_cds_ensembl:
    input:
        "data/raw_cds_ensembl.fna",
        "data/sequences_dataset.faa"
    output:
        "data/cds_ensembl.fna"
    shell:
        "src/get_sequences.py {input} > {output}"

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
        "molecular_evolution/sequences_aln.faa"
    shell:
        "mafft {input} >> {output}"

rule iqtree_phylogeny:
    input:
        "molecular_evolution/sequences_aln.faa"
    output:
        "molecular_evolution/phylogeny.treefile"
    shell:
        "iqtree -s {input} -alrt 1000 -nt 4 -pre molecular_evolution/phylogeny"

rule cds_alignment:
    input:
        "molecular_evolution/sequences_aln.faa",
        "data/cds_dataset_labeled.fna"
    output:
        "molecular_evolution/cds_aln.fna"
    shell:
        "pal2nal.pl {input} -output fasta > {output}"

rule hyphy_fel:
    input:
        align="molecular_evolution/cds_aln.fna",
        tree="molecular_evolution/phylogeny.treefile"
    output:
        "molecular_evolution/hyphy_fel.json"
    shell:
        "hyphy fel --alignment {input.align} --tree {input.tree} &&"
        "mv molecular_evolution/cds_aln.fna.FEL.json {output}"

rule hyphy_busted:
    input:
        align="molecular_evolution/cds_aln.fna",
        tree="molecular_evolution/phylogeny.treefile"
    output:
        "molecular_evolution/hyphy_busted.json"
    shell:
        "hyphy busted --alignment {input.align} --tree {input.tree} &&"
        "mv molecular_evolution/cds_aln.fna.BUSTED.json {output}"

rule hyphy_fubar:
    input:
        align="molecular_evolution/cds_aln.fna",
        tree="molecular_evolution/phylogeny.treefile"
    output:
        "molecular_evolution/hyphy_fubar.json"
    shell:
        "hyphy fubar --alignment {input.align} --tree {input.tree} &&"
        "mv molecular_evolution/cds_aln.fna.FUBAR.json {output}"

#rule hyphy_gard:
#    input:
#        align="molecular_evolution/cds_aln.fna"
#    output:
#        "molecular_evolution/hyphy_gard.json"
#    shell:
#        "hyphy gard --alignment {input.align} &&"
#        "mv molecular_evolution/cds_aln.fna.GARD.json {output}"

#rule hyphy_meme:
#    input:
#        align="molecular_evolution/cds_aln.fna",
#        tree="molecular_evolution/phylogeny.treefile"
#    output:
#        "molecular_evolution/hyphy_meme.json"
#    shell:
#        "hyphy meme --alignment {input.align} --tree {input.tree} &&"
#        "mv molecular_evolution/cds_aln.fna.MEME.json {output}"
