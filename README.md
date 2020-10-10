# Evolutionary and Structural Constraints Influencing Apolipoprotein A-I Amyloid Behavior :scroll:
---

In this folder you will find all the code and data used to prepare the figures and the paper.

A manuscript describing the results from this work has been posted on the BioRxiv preprint server ([BioRxiv preprint](https://doi.org/10.1101/2020.09.18.304337)) and is also available within the folder BioRxiv_manuscript.

## Sequence Datasets (available at the data folder)

Evolutionary studies were conducted using sequence data from Ensembl and RefSeq databases.

Below you can find the link to retrieve protein sequence: 

- [Ensembl sequences](https://www.ensembl.org/Homo_sapiens/Gene/Compara_Ortholog?db=core;g=ENSG00000118137;r=11:116835751-116837950)

- [Refseq sequences](https://www.ncbi.nlm.nih.gov/gene/335/ortholog/?scope=7776)

Nucleotide sequences from Ensembl can be downloaded from the same link detailed above. In the case of RefSeq database, nucleotide sequences were retrieve using NCBI [Entrez Programming Utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/).

## Amyloid aggregation tendency (amyloid_aggregation)

To compute aggregation propensities, the following programs were employed:

- [TANGO](http://tango.crg.es/) (prediction of aggregating region in unfolded polypeptides)
- [Camsol](http://www-vendruscolo.ch.cam.ac.uk/camsolmethod.html) (Structurally-corrected protein solubility prediction)
- [ZipperDB](https://services.mbi.ucla.edu/zipperdb/) (database of fibril-forming protein segments)

## Structural features

Gaussian network model (GNM) and weighted contact number (WCN) were computed with the [ProDy](http://prody.csb.pitt.edu/)and with a custom script from  [clauswilke/proteinER](https://github.com/clauswilke/proteinER/), respectively.

## *In silico* saturation mutagenesis

We used [FoldX](http://foldxsuite.crg.eu/) to calculate the theoretical thermodynamic destabilization effect of each possible amino acid substitution in apolipoprotein A-I sequence. We automated this task with the aid of the [Mutatex](https://github.com/ELELAB/mutatex) pipeline.
