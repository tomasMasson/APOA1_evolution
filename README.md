# Evolutionary and Structural Constraints Influencing Apolipoprotein A-I Amyloid Behavior :page_facing_up:
---

In this repo you will find the code and data employed to prepare the figures and the paper.

A manuscript describing the results from this work has been posted on BioRxiv ([Preprint](https://doi.org/10.1101/2020.09.18.304337)) and is also available within the folder BioRxiv_manuscript.

## Sequence datasets (data/)

Evolutionary studies were conducted using sequence data from Ensembl and RefSeq databases.

Below you can find the link to retrieve protein sequence: 

- [Ensembl sequences](https://www.ensembl.org/Homo_sapiens/Gene/Compara_Ortholog?db=core;g=ENSG00000118137;r=11:116835751-116837950)

- [Refseq sequences](https://www.ncbi.nlm.nih.gov/gene/335/ortholog/?scope=7776)

Nucleotide sequences from Ensembl can be downloaded from the same link detailed above. In the case of RefSeq entries, nucleotide sequences were retrieve using NCBI [Entrez Programming Utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/).

## Phylogeny and molecular evolution of apoA-I (molecular_evolution/)

Contains the phylogenetic reconstruction of apoA-I evolution with [IQ-TREE](http://www.iqtree.org/) (APOA1_phylogeny.treefile) and the evolutionary rates inferred with [HyPhy](http://www.hyphy.org/) (the file evolution_dataset.csv contains all the data used for visualizations).

## Amyloid aggregation tendency (amyloid_aggregation/)

To compute the aggregation propensity of each protein sequence in our dataset we employed [TANGO](http://tango.crg.es/) with default settings. The file aprs_dataset.csv contains all the aggregating regions predicted for apoA-I sequences.

## Structural features (structural_features/)

Gaussian network model fluctuations (apoa1_msf.csv) and weighted contact numbers (apoa1.wcn.csv) were computed with the [ProDy](http://prody.csb.pitt.edu/) and with a custom script from  [clauswilke/proteinER](https://github.com/clauswilke/proteinER/), respectively. We used [Camsol](http://www-vendruscolo.ch.cam.ac.uk/camsolmethod.html) (Structurally-corrected protein solubility prediction) and [ZipperDB](https://services.mbi.ucla.edu/zipperdb/) (database of fibril-forming protein segments) to understand the contribution of apoA-I structure ([link](https://homepages.uc.edu/~davidswm/structures.html)) to its aggregation tendency (camsol_solubility.txt and zipperdb.csv).

## *In silico* saturation mutagenesis (in-silico_mutagenesis/)

We used [FoldX](http://foldxsuite.crg.eu/) to calculate the theoretical thermodynamic destabilization effect of each possible amino acid substitution in apoA-I sequence (foldx_dataset.csv) and automated this task with the aid of the [Mutatex](https://github.com/ELELAB/mutatex) pipeline. 

### MutateX command was run inside mutatex-env (as recommended in the repo)
`~/mutatex/bin/mutatex apoa1-hdl.pdb --foldx-binary ~/foldx5Linux64.tar__0/foldx --rotabase rotabase.txt --np 4 --binding-energy --foldx-log --clean deep --compress`

Pathogenicity scores (rhapsody_dataset.csv) were calculated with the [Rhapsody server](http://rhapsody.csb.pitt.edu/). Apoa-I natural variants were extracted from [gnomAD](https://gnomad.broadinstitute.org/). The file variants_dataset.csv contains all the data used for visualizations.

## Visualization (viz/)

Code and datasets used for visualization, together with the .svg figure files.
