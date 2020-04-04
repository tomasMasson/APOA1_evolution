# APOA1 Molecular Evolution

This folder contains all the data and code used to prepare the manuscript about APOA1 evoution (in preparation).

## Sequences retrieval

Protein and coding sequences were retrieved from Ensembl from the following link:
- [Ensembl sequences] (https://www.ensembl.org/Homo_sapiens/Gene/Compara_Ortholog?db=core;g=ENSG00000118137;r=11:116835751-116837950)
Protein sequences from Refseq were retrieved from the following link:
- [Refseq sequences] (https://www.ncbi.nlm.nih.gov/gene/335/ortholog/?scope=7776)

Sequences were discarded if contained non-stadard symbols (e.g. X), were less than 200 AA or didn't have a start Methionine.

## Evolutionary analysis(molecular_evolution/)

Phylogenetic reconstruction was carried with IQ-TREE using a sequence alignmnet prepared with MAFFT.
Evolutionary rate was estimated usign the Hyphy package (molecular_evolution/hyphy.


