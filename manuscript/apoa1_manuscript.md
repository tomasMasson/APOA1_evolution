# Evolutionary and Structural Constraints Influencing Apolipoprotein A-I Amyloid Behaviour

Gisonno RA^a^, #, Masson T^b,#^, Ramella N^a^,, Barrera EE^c^, Romanowski V^b^, Tricerri MA^a^  

^a^ Instituto de Investigaciones Bioquímicas de La Plata (INIBIOLP, CONICET-UNLP), Facultad de Ciencias Médicas, Universidad Nacional de La Plata, La Plata, Argentina
^b^ Instituto de Biotecnología y Biología Molecular (IBBM, CONICET-UNLP), Facultad de Ciencias Exactas, Universidad Nacional de La Plata), La Plata, Argentina
^c^ Group of Biomolecular Simulations, Institut Pasteur de Montevideo, Montevideo, Uruguay  

^#^ Co-first authors

\newpage

## Highlights

* Aggregation prone region 1 (APR1), comprising residues 14-19, is consistently conserved during the evolutionary history of Apolipoprotein A-I.
* APR1 contributes to thermal stability of the ɑ-helix bundle in the full-length Apolipoprotein A-I model.
* Amyloid variants introduce a destabilizing effect on the monomer structure of Apolipoprotein A-I, in contrast to HDL-deficiency and gnomAD variants, which are nearly neutral.
* During molecular dynamics simulations, G26R mutant lead to the partial unfolding of ɑ-helix bundle and exposure of APR1.

\newpage

## Abstract

Apolipoprotein A-I (apoA-I) has a key function in the reverse cholesterol transport mediated by the high density lipoprotein (HDL) particles. However, aggregation of apoA-I single point mutants can lead to hereditary amyloid pathology. Although several studies have tackled the biophysical and structural impacts introduced by these mutations, there is little information addressing the relationship between the evolutionary and structural features that contribute to the amyloid behaviour of apoA-I. We combined evolutionary studies, in silico saturation mutagenesis and molecular dynamics (MD) simulations to provide a comprehensive analysis of the conservation and pathogenic role of the aggregation prone regions (APRs) present in apoA-I. ApoA-I sequences analysis demonstrated the pervasive conservation of an APR, designated APR1, within the N-terminal ɑ-helix bundle. Moreover, stability analysis carried out with the FoldX engine showed that this region contributes to the marginal stability of apoA-I. Structural properties of the full-length apoA-I model suggest that aggregation is avoided by placing APRs into highly packed and rigid portions of its structure. Compared to HDL-deficiency or natural silent variants extracted from the gnomAD database, the thermodynamic and pathogenic impact of apoA-I point mutations associated with amyloid pathologies were found to show a higher destabilizing effect. MD simulations of the amyloid variant G26R evidenced the partial unfolding of the ɑ-helix bundle and the occurrence of β-strand secondary elements at the C-terminus of apoA-I. Our findings highlight APR1 as a relevant component for apoA-I structural integrity and emphasize a destabilizing effect of amyloid variants that leads to the exposure of APRs. This information contributes to our understanding of how apoA-I, with its high degree of structural flexibility, maintains a delicate equilibrium between its lipid-binding function and intrinsic tendency to form amyloid aggregates. In addition, our stability measurements could be used as a proxy to interpret the structural impact of new mutations affecting apoA-I.

\newpage

## Introduction

Apolipoprotein A-I (apoA-I) is the most abundant protein component of high-density lipoproteins (HDL) and is responsible for the reverse cholesterol transport from extracellular tissues back to the liver (Lund-Katz and Phillips 2010; Rader et al. 2008), which has been associated with a protective function against cardiac disease and atherosclerosis (Navab et al. 2008; Rosenson et al. 2015). The scaffolding functions of apoA-I in the HDL particle and its multiple protein-protein interactions, mainly with the lecithin:cholesterol acyltransferase and the ATP-binding cassette A1 transporter (Chroni et al. 2002; Manthei et al. 2020), forces it to maintain a dynamical and flexible conformation (Gursky and Atkinson 1996).

In contrast to these physiological functions, several point mutations affecting apoA-I have been associated with hereditary amyloid pathology (Sipe et al. 2016). These mutations are mainly distributed into two "hot spots", located at the N-terminal region and the C-terminal portion of the protein, each one with a typical clinical manifestation (Das and Gursky 2015). Mutations that occur at the N-terminal region (residues 26–100) are characterized by amyloid deposits in the liver and kidney (Mucchiano et al. 2001; Obici et al. 2006), while those located at a short C-terminal domain (residues 170–178) are mainly associated with heart, larynx and skin deposits (Gaglione et al. 2018). In non-hereditary amyloidosis, full-length apoA-I is deposited in atherosclerotic plaques as fibrils or the senile forms of amyloid. This process has been associated with aging, but it has also been described in chronic pathologies such as Alzheimer's disease and type 2 diabetes mellitus (Westermark et al. 1995). 

Amyloid behaviour of apoA-I N-terminal fragment has been attributed to the presence of aggregation-prone regions (APRs) in its sequence and, specifically, to an APR located at the N-terminus (Obici et al. 2006). It has been hypothesized that amyloidogenic mutations or post-translational modifications could promote aggregation through the destabilization of the partially disorganized structure of apoA-I -described as a molten globular state- followed by the exposure of APRs. In this sense, most studies addressing the effect of amyloid variants have focused on the biophysical and physiological consequences of specific mutants. However, our understanding of the relationship between apoA-I sequence determinants and its aggregation process remains unclear.

In this study, through an extensive evolutionary analysis we characterized the conservation of aggregating regions in a broad dataset of vertebrates apoA-I sequences. Using the recently described full-length consensus structure (Melchior, 2017), we examined the structural properties of apoA-I that contribute to minimize the exposure of its constituent APRs. In silico saturation mutagenesis analysis of apoA-I demonstrated that an evolutionary-conserved APR, located between residues 14-19, contributes to the thermodynamic stability of the N-terminus and revealed a common destabilizing effect for amyloid-associated variants. Using molecular dynamics simulations, we studied the conformational and dynamical impact of five different amyloid variants on the structure of full-length apoA-I. Altogether, our results suggest that APR1 is a structural component that contributes to the stability of apoA-I helix bundle and emphasizes the destabilizing effect of amyloid variants, which is linked to subsequent APRs exposure in the case of G26R variant. This information is relevant to understand how a marginally stable, but metabolically active protein manages to initiate the formation of an amyloid structure and develop a severe pathology.

## Results

### Molecular evolution of apoA-I aggregating regions within the Sarcopterygii group

Given that apoA-I has four previously characterized aggregation-prone regions (APRs), we asked if this amyloid regions could be relevant to the protein functionality in spite of its know pathogenic role [@Louros_2016?]. To tackle this question, first of all we decided to explored the evolutionary conservation of these motifs within apoA-I sequences of sarcopterygian organisms. Our analysis was restricted to this group because of the large evolutionary distance between fishes and tetrapods, a factor that could mislead our results. We collected our sequences from the Ensembl database and constructed multiple sequence alignment (MSA) in order to identify the APRs present in other species based on the reported APRs for the human species. Then, we employed the Tango software to predict the sequence-based aggregation propensity of each one of the APRs sequences and also computed the sequence conservation from the MSA based on the Shannon entropy (H). Our amyloidogenicity results for the four APRs suggest that the APR1 (residues 14 to 19) present an amyloid behaviour in more than 60% of the sequences of our dataset, followed by the APR4 in approximately 30% of the sequences. On the other hand, APR2 and APR3 presented a non aggregating behaviour in virtually all the sequences (Figure 1A). Regarding sequence conservation, APR1 is also one of the most conserved APRs, together with the APR3. When compared against the average H value of apoA-I, the sequence entropy of APR1 and APR3 are significantly lower, meaning that these amyloid regions are more conserved than most of the residues of apoA-I on average (Figure 1B). 

![Figure 1 Evolutionary conservation of APRs within apoA-I sequences. **A** Percentage of sequences in our dataset that are described are amyloidogenic according to Tango (average score over 5%). **B** Sequence entropy (H) calculated for each residue inside the corresponding APR.](){width=100%}

We decided to study the selection constraints affecting apoA-I as a way to provide further evidence of the conservation of its APRs. A maximum likelihood phylogeny reflecting the evolutionary relationships between sequences was reconstructed from the MSA (Supplementary figure 1). Using this phylogeny as framework, we computed the site-wise evolutionary rates at codon level (dN/dS, ratio of nonsynonymous to synonymous mutations) and evaluated its statistical significance in order to evidence the presence of selection constraints acting on the apoA-I sequence. In particular, we employed different methods from the HyPHY package in order to detect both pervasive and episodic selection events. In general terms, the evolutionary rate profile of apoA-I revealed that most of the protein sequence displayed a dN/dS value significantly lower than 1 but this value tend to rise for the C-terminus of the protein (Supplementary figure 2A). Using a cartoon representation to depict the statistical evidence for the different types of selective pressure (negative, neutral or positive) at each site, we evidenced the extent of negative selection, both pervasive and episodic, acting on apoA-I sequence. In accordance with the entropy results, the residues corresponding to the APRs have evolved mainly under purifying selection, meaning that they tend to be conserved during evolution (Supplementary figure 2B). These data together supports the idea that some APRs, in particular APR1, have been conserved during the evolutionary history of apoA-I and may contribute to the functional properties of the protein.

### Comparative structural modelling of apoA-I historical sequences

Prompted by the sequence conservation of some of the APRs present in apoA-I, we decided to expand these results with information at the protein structure level. For this, we implemented a comparative modelling approach to compared several apoA-I structures corresponding to the ancestral sequences inferred from apoA-I phylogeny and several extant species, including reptiles, birds and mammals. To date, the most comprehensive and complete structure available for apoA-I is deposited on the webpage of the Davidson's lab [ApoA-I consensus structure link](http://homepages.uc.edu/~davidswm/Melchior%20et%20al%20apoA-I.pdb), so we used it as the template for our homology-based modelling pipeline. We used Modeller to generate a structural model for each target sequence and the PyRosetta FastRelax tool to further refine it. A structure-based alignment of the best scoring model for each target sequence showed that the root mean square deviation (RMSD) between structures were in the range of 0.5-1, suggesting that the overall structure of apoA-I has been conserved along its evolutionary history (Supplementary figure 3A). Additionally, we computed the approximated intrinsic dynamic profile for each model using a gaussian normal network (GNM) model. These results showed that, besides the geometric properties of human apoA-I structure, its mean squared fluctuation (MSF) profiles are also conserved across ancestral and extant structures (Supplementary figure 3B).

We used these structural models to explore the intrinsic fluctuations levels and packaging number of the residue sites composing apoA-I APRs. Our results showed that APRs residue have significantly lower MSF values when compared with the value distribution for the non-APR residues of apoA-I (Figure 2A, *P* value = X). In a similar trend, the weighted contact number (WCN), a measure of how crowned is the molecular environment of a residue, also showed that APRs sites are consistently surrounded by a larger number of residues than the non-APR site of apoA-I (Figure 2B, *P* value = Y). Together, this data suggest that apoA-I has conserved its structure and dynamics behaviour during its evolution. In this structural context, APRs residues are integrated into relatively rigid and densely packaged segments of apoA-I, a hallmark of functionally relevant sites for the protein structure [@cita].

### Amyloid-associated variants have a destabilizing effect on apoA-I monomer structure

In order to better understand the structural consequences of amyloid variants on apoA-I monomer, we explored their thermodynamic and pathological effects using in silico saturation mutagenesis. Destabilizing effect of each possible mutation in apoA-I sequence, represented by the difference in free energy (ΔΔG) between wild type and mutant structure, was measured using the FoldX empirical force field and the MutateX automation pipeline. To complement this approach, variant impact on protein function was estimated using Rhapsody. We noticed from the ΔΔGs distribution that most of the variants had a moderate impact on apoA-I stability (-1 kcal/mol < ΔΔG < 1 kcal/mol) (Figure 4A, complete FoldX results are available with Supplementary Figure 3). Further examination revealed that apoA-I structure is highly sensitive to mutations in the region of residues 7-28, which comprises the APR1 (Figure 4B). Rhapsody predictions also support this region as a mutation-sensible segment of apoA-I structure (Supplementary Figure 4). This result suggests that conservation of APR1 in apoA-I could be necessary to maintain the marginal thermodynamic stability of the ɑ-helix bundle despite the risk to undergo aggregation. In line with our observations, APRs have been recently proposed to play a stabilizing role on protein structure (Langenberg et al. 2020).  
We used ΔΔG values to highlight differences between pathogenic variants associated with amyloidosis or HDL deficiencies (Gogonea 2016), and natural variants reported by the gnomAD project (Karczewski et al. 2020). Our results evidenced that amyloid mutations had a destabilizing effect and a pathogenicity score significantly greater when compared with natural or HDL-deficiency variants (Figure 5A and 5B), emphasizing the relationship between structural destabilization and amyloid pathology onset. An interesting observation from this result is that HDL-deficiency mutations have similar effects compared with natural variants, suggesting that this type of mutations exert its pathogenic effect without disrupting apoA-I monomer stability. Given the fact that a small group of variants in the gnomAD database showed an elevated impact on protein stability (> 2 ΔΔG kcal/mol), we decided to investigate how frequently they occur at population level. Frequency spectrum (Figure 5C) showed that variants with a severe impact on protein stability were present at low frequencies, thus minimizing their deleterious effect on the population. In contrast, variants with the higher frequency in our dataset had a nearly neutral effect on stability. It is worth noting that although gnomAD excluded subjects with mendelian and pediatric diseases from its cohorts, we cannot rule out the possibility that some of these destabilizing variants correspond to non diagnosed pathologies.  

![Figure 4 APR1 contributes to the stability of the ɑ-helix bundle in apoA-I. The protein structural stability was quantified using the FoldX engine. The free energy difference (ΔΔG) was calculated by comparison between the ΔG of the mutant and wild type sequence A ΔΔG values distribution corresponding to all possible mutations. B Heatmap of ΔΔG values for the first 40 residues of apoA-I N-terminal region.](){width=100%}
  
![Figure 5 Impact of apoA-I variants on protein stability and function A-B Free energy difference (ΔΔG) and Rhapsody pathogenicity distributions for amyloid, HDL and gnomAD variant classes (p-value < 0.01, Mann-Whitney rank test). C Allele frequency distribution for gnomAD variants against its predicted effect on protein stability.](){width=100%}

### Molecular dynamics simulations of apoA-I mutants

To complement our previous results showing the destabilizing effect of amyloid variants, we decided to study the dynamic properties of apoA-I amyloid mutants by conducting coarse-grain molecular dynamics simulations under the SIRAH force field. We selected four amyloid mutants (G26R, L60R, Δ107 and R173P) previously characterized by our group (Gaddi et al. 2020; Gisonno et al. 2020; Ramella et al. 2012; Rosú et al. 2015), plus the wild type protein, to prepare our simulation systems. Our selection also ensured that mutations were distributed throughout the apoA-I sequence.  
In the first place, we explored the overall dynamics of our systems by means of its root mean square deviation (RMSD). The recently described consensus structure for apoA-I was used as reference coordinates for RMSD calculations. We observed a great variability in the RMSD values for all simulated systems (5.4-10 Å) during our 1 µs simulation, which could be related with the highly dynamic and marginally stable structure proposed for apoA-I. We did not evidence any significant differences between systems (Supplementary Table 2), suggesting that the impact of point mutations is negligible when compared against the intrinsic backbone dynamics.  
Given the structural variability evidenced by RMSD, we decided to compute MD observables over the last 100 ns of the simulations. Position-specific root mean square fluctuations (RMSF) for each of the systems studied showed that loop regions 120-150 and 180-200 are the most flexible regions in apoA-I, while the N-terminal ɑ-helix bundle maintained a more compact structure during the simulation time (Supplementary Figure 5). These results are in good agreement with the MSF values computed by the GNM model (Figure 3C), reinforcing the dynamic profile obtained for apoA-I. The similar fluctuation profiles between the wild type apoA-I and the above-mentioned mutants suggest that mutations do not introduce major structural changes, at least during the simulation time frame. Because of this, we decided to compute more specific structural properties over the last 100 ns of the simulations.  
To further characterize the structural impact of single point mutations on each system we measured the gyration radius (Rg) as a general descriptor of the protein shape for each system. When mutants were compared against the wild type system (Figure 6A), only the L60R system displayed a significantly higher Rg value, indicating a more extended conformation for this mutant. Mutants G26R and R173P also showed a tendency to present greater Rg values when compared against wild type, but they were statistically not significant, in part due to the highly variable nature of the apoA-I system.  
We explored the possible role of mutations in amyloid aggregation of full length apoA-I by analyzing the solvent accessible surface area (SASA) of each APR in our five systems. We noted a significant increase in the solvent exposure of the APR1 in the G26R system when compared against the wild type, while the other systems did not exhibit a significant increase of SASA values for any of the APRs (Figure 6B). Visualization of the final time frames of the trajectory corresponding to the G26R system showed a partial unfolding of the ɑ-helix bundle, which explains the increased exposure of APR1 (Figure 6C). Additionally, the G26R mutant evidenced the transitory formation of β-strand secondary structures at the APR3. The low impact of the L60P, Δ107 and R173P variants on APRs exposure suggest that these mutants could require further post-translational modifications in order to undergo amyloid aggregation.
  
![Figure 6 Molecular dynamics simulations of full-length apoA-I mutants A Gyration radius (Rg) of each system computed over the last 100 nanoseconds from five independent simulations. The L60R mutant showed a higher Rg when compared against the wild type system (p-value = 0.05, Student’s Test). B Solvent accessible surface area (SASA) calculated for the APR1 (residues 14-19). The G26R system displayed a higher APR1 exposure when compared with the wild type system (p-value < 0.05 Student’s Test). C Graphical representation of the consensus model (WT) and the final snapshot of one of the replicas simulated for the G26R mutant. The substitution of glycine by arginine in position 26 destabilizes the helix bundle, expelling helix H6 with the concomitant solvent exposure of APR1 (left inset). A 180º view rotation shows the β-sheet hairpin formed between residues S224 and A232, corresponding to the APR3 (right inset).](){width=100%}


## Discussion

Molecular mechanism of amyloid aggregation for apoA-I remains largely unknown, due in part to the limited structural information given its inherent conformational plasticity (Gursky and Atkinson 1996). This work builds upon evolutionary, dynamical and structural features of apoA-I in order to provide a comprehensive characterization of the amyloid phenomena in this protein, complementing the extensive experimental results available. Collectively, our results suggest an intimate relationship between aggregating regions and structural stability in apoA-I. Additionally, MD simulations of full-length apoA-I mutants shed light on the first steps of the aggregation process in amyloid mutants.

First, we aimed to complement the few studies available that tackle the evolutionary history of apoA-I and its implications on its structure (Bashtovyy et al. 2010). An important observation that emerges from our results is that apoA-I evolution is tightly linked with the biophysical properties imposed by its constituent amphipathic ɑ-helices. This is especially evident in the case of prolines and positively charged residues, which are critical for apoA-I function and structure. Prolines have been extensively characterized as a fundamental component for apoA-I flexibility and stability, as their positioning at the beginning of the 22-mers induces a relative break of one helical segment respect to the other, allowing the protein rearrangement required for lipid removal and dynamic interactions with membranes and proteins interactors (Klon 2002 JMB https://doi.org/10.1016/S0022-2836(02)01143-9). In the case of charged residues, a strong lipid affinity has been attributed to the cationic residues within the polar face of the amphipathic ɑ-helices (Fuentes et al. 2018), as they interact with the negative heads of the phospholipids at the surface of lipid bilayers through a process designated "snorkeling" (Leman, Maryanoff, and Ghadiri 2013; Oda 2017). Also, arginine residues present at the helix 6 (R149, R153, and R160) are relevant for apoA-I-mediated activation of LCAT (Roosbeek et al. 2001 JLR  PMID: 11160363). In a different trend, conservation of specific leucine residues could be driven by its involvement in lipid binding (Hovingh 2003 J Am Coll Cardiol 10.1016/j.jacc.2004.06.070, Fotakis 2013 JLR 10.1194/jlr.M038356) and stabilization of the hydrophobic clusters inside helix bundle (Gursky 2012 Biochemistry). In addition, given that fast evolving regions of proteins have been associated with greater flexibility (Tiwari 2018 https://doi.org/10.1016/j.sbi.2017.12.001; Campitelli et al. 2020), the higher evolutionary rate observed for the C-terminal region could be linked with the maintenance of the flexibility required for its lipid-binding properties.

The fact that apoA-I has conserved an aggregating segment (APR1) consistently along its evolutionary history raises questions about its structural relevance. Amyloid motifs have been proposed to contribute to protein structural stability through extensive interactions inside protein hydrophobic cores (Tartaglia et al. 2010 https://doi.org/10.1016/j.jmb.2010.08.013; Langenberg et al. 2020), which establish a trade-off between protein environment, foldability and aggregation propensity (Linding 2004 JMB https://doi.org/10.1016/j.jmb.2004.06.088; Monsellier 2008 PLoS CB https://doi.org/10.1371/journal.pcbi.1000199). Based on its conserved nature and FoldX stability results, it is possible to hypothesize that APR1 is necessary to ensure the marginal stability of apoA-I ɑ-helix bundle, even though this region could trigger aggregation upon solvent exposure or proteolytic cleavage (Arciello FEBS Letters 2016 https://doi.org/10.1002/1873-3468.12468). Moreover, the presence of APR2 exclusively in human species represents a synergizing factor that could aggravate the amyloid behaviour of apoA-I, as demonstrated recently for the N-terminal peptide (Wong et al. 2012 10.1016/j.febslet.2012.05.007; Mizuguchi et al. 2019). In this context, the structural features of APR1 (low intrinsic flexibility and highly packaged environment) are likely to control its exposure to solvent and prevent aggregation events. Hydrogen-deuterium exchange experiments (Das et al. 2016) support the highly packaged nature of the ɑ-helix bundle and the low solvent exposure of APR1 in apoA-I. 

Amyloidogenic variants are primarily located in the N-terminal region of apoA-I, whereas variants associated with HDL deficiencies are clustered in the H5-H7 region (Gogonea 2016; Matsunaga et al. 2010). Through a comprehensive evaluation of the destabilizing effect and pathogenicity of each possible mutation affecting apoA-I we demonstrated that amyloid variants have a significant destabilizing effect on the monomer structure. The fact that TANGO aggregation tendency of APRs was not modified by the introduction of amyloid mutations, supports the hypothesis that aggregation propensity per se has a limited impact on the aggregation process of full-length apoA-I (Raimondi et al. 2011). On the other hand, variants associated with HDL defects have a minimal effect on structural instability, which provides evidence that this type of disorders could be caused by mechanisms less dependent on protein unfolding and probably involving the disruption of interaction sites with protein interactors during the reverse cholesterol transport pathway. In addition, we believed that ΔΔG values derived from our in silico saturation mutagenesis would be useful as a proxy for the initial study of novel apoA-I mutants.

Taking advantage of the recently described consensus model of apoA-I (Melchior et al. 2017), our MD simulations of mutant G26R revealed a partial unfolding of the N-terminal ɑ-helix bundle and a significant increase in the exposure of APR1, which is also congruent with the destabilizing effect predicted from our ΔΔG calculations. This partial unfolding is in line with the experimental reports of increased susceptibility to proteases (Adachi et al. 2012) and greater hydrogen-deuterium exchange rate of the ɑ-helix bundle (Das et al. 2016) for this mutant. Moreover, β-sheet secondary structures present at APR3 could provide a template for the aggregation of full-length apoA-I (Das et al. 2014).

Altogether, our results obtained from full-lenght protein support the current hypothesis that unfolding of the helix bundle and exposure of aggregating regions represents the first steps of apoA-I-mediated amyloidosis (Mizuguchi et al. 2019). The mild effect of L60R, Δ107 and R173P variants on apoA-I structure and APRs exposure suggest that further modifications could be required to promote protein aggregation of these mutants, like oxidation or proteolytic cleavage (Witkowski 2018 10.1096/fj.201701127R; Chan 2015 10.1074/jbc.M114.630442). 

Recently, the connection between the pro-inflammatory microenvironment and the formation of aggregation-prone species has been deeply characterized, reinforcing this hypothesis (Gisonno et al. 2020). Moreover, the presence of the N-terminal proteolytic fragment (residues 1-93) within patients’ lesions raises the hypothesis that mutations may facilitate the cleavage of apoA-I by circulating proteases (Cavigiolio and Jayaraman 2014; Kareinen et al. 2018). 

In agreement with the late onset of the hereditary apoA-I amyloidosis in patients, it may be hypothesized that mild chronic events may be required to induce the protein unfolding. 

## Materials and Methods

### Evolutionary analysis of apoA-I sequences

A comprehensive dataset of sequences was generated by collating apoA-I orthologs available at Ensembl and Refseq databases (O'Leary 2015 Nucleic Acids Research https://doi.org/10.1093/nar/gkv1189; Yates 2020 Nucleic Acids Research https://doi.org/10.1093/nar/gkz966). To exclude low quality data, only sequences which did not contain ambiguous characters, had a proper methionine (M) starting codon and were longer than 200 amino acids were kept. Additionally, as both Ensembl and Refseq have overlapping data for some species, CD-HIT clustering tool (Fu et al. 2012) was employed to generate groups of similar sequences with an identity cut-off value of 0.98. Our fInal dataset comprised 215 protein sequences covering both Actinopterygii and Sarcopterygii lineages of Vertebrata. 
In order to reconstruct a maximum likelihood phylogeny, a multiple sequence alignment (MSA) was built from the protein sequences using ClustalO with default parameters (Sievers et al. 2011) and the phylogenetic inference was carried out with the IQ-TREE software (Minh et al. 2020). The substitution model was selected based on the ModelFinder evolutionary model fitting tool (Kalyaanamoorthy et al. 2017) and the ultrafast bootstrap implemented in IQ-TREE was used to calculate the support values for phylogeny branches (Minh, Nguyen, and Haeseler 2013). We rooted our phylogeny using cartilaginous fish species as outgroups, as proposed by de Carvalho et al. (2019). Visualization of the resulting phylogeny was carried out using the iTOL server (Letunic and Bork 2019). 

### Selective pressure acting on apoA-I sequence

Nucleotide coding sequences were retrieved for each protein in our dataset using the NCBI Entrez eutils tools for Refseq sequences and the Ensembl orthologs dataset. Because the evolutionary rate estimation requires a codon-level alignment, the software PAL2NAL was used to align codons in nucleotide sequence using a protein alignment as a guide (Suyama, Torrents, and Bork 2006). The Hypothesis Testing using Phylogenies (HyPhy) package was used to conduct evolutionary analysis on the codon-based alignment. Before testing for evidence of selective pressure, we conducted a recombination analysis using the Genetic Algorithm Recombination Detection (GARD) method, (Pond et al. 2006) in order to screen for possible recombination events in our alignment; it is known that the presence of recombination leads to a larger number of false positives in selection analysis. We inferred the natural selection strength (Omega, dN/dS) for each alignment position using our phylogeny as framework. We employed the Fixed Effects Likelihood (FEL) (Pond and Frost 2005) and the Fast Unconstrained Bayesian Approximation (FUBAR) methods (Murrell et al. 2013) to quantify the dN/dS ratio for each codon in the alignment. Although both methods provide similar information, FEL provides support for negative selection (dN/dS < 1) whereas FUBAR has more statistical power to detect positive selection (dN/dS > 1). Because codon alignment positions are difficult to put in structural context, data were extracted for codons occurring in wild type human apoA-I. Additionally, we estimated evolutionary rates based on alignments at amino acid levels using LEISR.  

### Coevolving residue pairs

Pairs of residues that are evolutionary correlated (coevolving sites) are useful to predict structural contacts. However, the repetitive structure of apoA-I and the lack of several ortholog sequences poses difficulties for this kind of analysis. To overcome these difficulties, putative coevolving residues were computed using the RaptorX server (Wang et al. 2017). RaptorX applies an ultra-deep convolutional residual neural network to predict contacts and distance and works particularly well on proteins without many sequence homologs. This method works by predicting the contact/distance matrix as a whole instead of predicting one residue pair independent of the others. RaptorX output represents the probability of two residues being in contact (i.e., their distance falling in the range 0-8 Å). Only residue pairs with a contact probability greater than 0.5 were retained.

### Structural features measurement

Residue solubility profile for apoA-I consensus structure was computed with the CamSol method (Sormanni 2015 JMB http://dx.doi.org/10.1016/j.jmb.2014.09.026). CamSol first calculates an intrinsic solubility score for each residue, based only on sequence information. Then, the algorithm applies a score correction to the solubility profile from the previous step to account for the spatial proximity of amino acids in the three-dimensional structure and for their solvent exposure.  
Fibril-forming segments were identified with the ZipperDB resource (https://services.mbi.ucla.edu/zipperdb/). Fibrillation propensity is calculated as proposed by Thompson et al. (PNAS https://doi.org/10.1073/pnas.0511295103). Briefly, each hexapeptide not containing a proline from the query sequence is mapped onto the cross-beta crystal structure of the fibril-forming peptide NNQQNY. Energetic fit is evaluated with the RosettaDesign software (Kuhlman 2000 PNAS https://doi.org/10.1073/pnas.97.19.10383). Hexapeptides with energies below the threshold of -23 kcal/mol were considered as highly propense to fibrillation.
Packaging level for residue i was represented by its Weighted Contact Number (WCN), which was calculated as follows: 
 
Where, rij is the distance between the geometric center of the side-chain atoms for residue i and residue j. Calculations were carried out using a custom script developed by Sydykova et al. (2018 F1000 https://doi.org/10.12688/f1000research.12874.2).  
Protein intrinsic dynamics was characterized using a coarse-grained simulation model based solely on protein topological information represented as a Gaussian Network Model (GNM). In this approach, protein structure is modelled as a network of nodes (alpha carbons) connected by springs. Numerical resolution of this model allows the calculation of the equilibrium displacement for all nodes (Mean Square Fluctuation, MSF), describing the global motions of the system. The ProDy package (Bakan, Meireles, and Bahar 2011) was used to adjust a GNM to the apoA-I consensus structure. We selected the first ten slow modes for analysis and plotting, since they have been reported previously as the main determinants of the global dynamics of protein structure (Kitao 1999 https://doi.org/10.1016/S0959-440X(99)80023-2).

### Conservation of Aggregation Prone Regions (APRs)

Signal peptide sequences were trimmed and removed from the MSA to retain only the mature protein sequence. TANGO software (Fernandez-Escamilla et al. 2004) was used to detect APRs in the protein sequences dataset. This algorithm predicts beta-aggregation using a space phase where the unfolded protein can adopt one of five states: random coil, alpha-helix, beta-turn, alpha-helical aggregation or beta-sheet aggregation. Importantly, TANGO is based on the assumption that the core regions of an aggregate are fully buried. Predictions were carried out using default settings: no protection for the C-terminus and N-terminus, pH 7, temperature of 310° K and ionic strength of 0.1.
Output files provide an aggregation score per position; as suggested in the TANGO manual and elsewhere, contiguous regions comprising five or more residues with a score of at least five were annotated as an APR. To address the impact of single point mutations in apoA-I aggregation tendency we ran TANGO for each mutant sequence and compared the scores profile against the wild type sequence. Sequence logos of each APR were plotted using the LogoMaker package (Tareen and Kinney 2019). TANGO software was downloaded from http://tango.crg.es using an academic license.

### Thermodynamics impact of missense variants

The FoldX engine (Guerois, Nielsen, and Serrano 2002) implements an empirical energy function based on terms significant for protein structure stability. The free energy of unfolding (ΔG) of the protein includes terms for van der Waals interactions, solvation of apolar and polar residues, intra and intermolecular hydrogen bonds, water bridges, electrostatic interactions and entropic cost for fixed backbone and side chains. Changes in free energy of folding upon mutation is calculated as the difference between the folding energy (ΔΔG) estimated for the mutants and the wild type variants. Although FoldX seems to be more accurate for the prediction of destabilizing mutations and less accurate for the prediction of stabilizing mutations, in both cases it was shown that FoldX is a valuable tool to infer putative relevant sites for structural stability. FoldX 5 suite was downloaded from http://foldxsuite.crg.eu/academic-license-info.  
We employed MutateX software (Tiberti et al. 2019) to automate the prediction of ΔΔGs associated with the systematic mutation of each available residue within apoA-I, by employing the FoldX energy function. At the heart of MutateX lies an automated pipeline engine that handles input preparation and performs parallel runs with FoldX. Basic steps involve protein data bank (PDB) structure repair (involving energy minimization to remove unfavorable interactions), model building for the mutant variants, energy calculations for both mutant and wild type structures and summarizing the estimated average free energy differences. 

### Pathogenicity scoring or missense variants

The Rhapsody prediction tool (Ponzoni et al. 2020) consists of a random forest classifier that combines sequence, structure, and dynamics-based features associated with a given amino acid variant and is trained over a comprehensive dataset of annotated human missense variants. Dynamical features include: mean-square fluctuations of the residue at the mutation site, which estimates local conformational flexibility; perturbation-response scanning effectiveness/sensitivity, accounting for potential allosteric responses involving the mutation site, and the mechanical stiffness at the sequence position of the mutated residue. These properties are computed from Elastic Network Models (ENM) representations of protein structures that describe inter-residue contact topology in a compact and computationally-efficient format that lends itself to a unique analytical solution for each structure. The algorithm was recently upgraded to include coevolutionary features calculated on conserved Pfam domains, and the training dataset was further expanded and refined. The latter combines annotated human variants from several publicly available datasets (Humvar, ExoVar, predictSNP, VariBench, SwissVar, Uniprot’s Humsavar and ClinVar). All analyses were performed using the Rhapsody server http://rhapsody.csb.pitt.edu/

### Molecular Dynamics Simulations

Coarse grained Molecular Dynamics simulations were performed with the SIRAH force field (Machado et al. 2019) and GROMACS 2018.4 software package (Abraham et al. 2015). We employed the consensus model of human apoA-I in its monomeric and lipid-free state, proposed by Davidson et al. (Melchior et al. 2017). The PDB file was downloaded from Davidson Lab homepage (http://homepages.uc.edu/~davidswm/structures.html). Mapping atomic to coarse-grained representations was done with a Perl script included in SIRAH Tools (Machado and Pantano 2016). G26R, L60R, R173P and Δ107 mutants were generated with Chimera (Pettersen et al. 2004), editing the coordinates of the consensus model pdb file. For the case of the deletion mutant, we removed Lys107 and connected residues Lys106 and Trp108 with an unstructured segment using Modloop (Fiser and Sali 2003). Wild type apoA-I and the mutant systems were assembled using the following setup: The protein was placed inside an octahedron simulation box defined by setting a distance of 1.5 nm between the solute and the edges of the box. Systems were solvated setting a 150 mM NaCl concentration following the protocol proposed by Machado et. al. (2020). Energy minimization and heating steps were done following the protocol recommended by Machado et al. (2019) using positional restraints in the protein backbone to ensure side-chain relaxation, especially in the mutant models. Production runs were performed by quintuplicate in the absence of any positional restraint, generating 1 μs trajectories at 310 K using a 1 bar NPT ensemble. Structural analysis was performed with GROMACS tools gmx rmsf, gmx gyrate and gmx sasa. Root mean square fluctuation was calculated for each residue aligning the full trajectory APOA-1 coordinates with the initial models. Radius of gyration and Solvent accessible surface areas (SASA) were obtained averaging the values corresponding to the last 0.1 μs of simulation. The SASA calculations were measured over three amyloid prone regions, comprising residues 14-19 (APR1), 53-57 (APR2) and 227-232 (APR3). 

### Code Availability

All Python packages used were installed through the Conda environment manager into a single environment. A requirements file is available in the repository of this project in order to install dependencies used in our analysis. The workflow manager Snakemake was used in the evolutionary analysis in order to gain reproducibility and consistency of the results (Koster and Rahmann 2012). The Snakefile and Python scripts used in this work are available at https://github.com/tomasMasson/APOA1_evolution.
Statistical Analyses and Visualizations
Scipy Python library was used for data manipulation and all statistical analyses [Scipy]. Statistical significance was determined using Mann-Whitney U Test for variant’s impact comparison and Student’s Test for MD observables. MD graphs are reported as means ± standard deviation derived from five independent experiments. All visualizations were prepared with the Seaborn library [Seaborn]. 

\newpage

## References

Abraham, Mark James, Teemu Murtola, Roland Schulz, Szilárd Páll, Jeremy C. Smith, Berk Hess, and Erik Lindahl. 2015. “GROMACS: High Performance Molecular Simulations through Multi-Level Parallelism from Laptops to Supercomputers.” SoftwareX 1–2:19–25.
Adachi, Emi, Hiroyuki Nakajima, Chiharu Mizuguchi, Padmaja Dhanasekaran, Hiroyuki Kawashima, Kohjiro Nagao, Kenichi Akaji, Sissel Lund-Katz, Michael C. Phillips, and Hiroyuki Saito. 2012. “Dual Role of an N-Terminal Amyloidogenic Mutation in Apolipoprotein A-I.” Journal of Biological Chemistry 288(4):2848–56.
Bakan, A., L. M. Meireles, and I. Bahar. 2011. “ProDy: Protein Dynamics Inferred from Theory and Experiments.” Bioinformatics 27(11):1575–77.
Bashtovyy, Denys, Martin K. Jones, G. M. Anantharamaiah, and Jere P. Segrest. 2010. “Sequence Conservation of Apolipoprotein A-I Affords Novel Insights into HDL Structure-Function.” Journal of Lipid Research 52(3):435–50.
Buck, Patrick M., Sandeep Kumar, and Satish K. Singh. 2013. “On the Role of Aggregation Prone Regions in Protein Evolution, Stability, and Enzymatic Catalysis: Insights from Diverse Analyses” edited by L. M. Iakoucheva. PLoS Computational Biology 9(10):e1003291.
Campitelli, Paul, Tushar Modi, Sudhir Kumar, and S. Banu Ozkan. 2020. “The Role of Conformational Dynamics and Allostery in Modulating Protein Evolution.” Annual Review of Biophysics 49(1):267–88.
de Carvalho, Leonor Lopes, Eva Bligt-Lindén, Arunachalam Ramaiah, Mark S. Johnson, and Tiina A. Salminen. 2019. “Evolution and Functional Classification of Mammalian Copper Amine Oxidases.” Molecular Phylogenetics and Evolution 139:106571.
Cavigiolio, Giorgio and Shobini Jayaraman. 2014. “Proteolysis of Apolipoprotein A-I by Secretory Phospholipase A2.” Journal of Biological Chemistry 289(14):10011–23.
Chroni, Angeliki, Tong Liu, Irina Gorshkova, Horng-Yuan Kan, Yoshinari Uehara, Arnold von Eckardstein, and Vassilis I. Zannis. 2002. “The Central Helices of ApoA-I Can Promote ATP-Binding Cassette Transporter A1 (ABCA1)-Mediated Lipid Efflux.” Journal of Biological Chemistry 278(9):6719–30.
Das, Madhurima and Olga Gursky. 2015. “Amyloid-Forming Properties of Human Apolipoproteins: Sequence Analyses and Structural Insights.” Pp. 175–211 in Advances in Experimental Medicine and Biology. Springer International Publishing.
Das, Madhurima, Xiaohu Mei, Shobini Jayaraman, David Atkinson, and Olga Gursky. 2014. “Amyloidogenic Mutations in Human Apolipoprotein A-I Are Not Necessarily Destabilizing - A Common Mechanism of Apolipoprotein A-I Misfolding in Familial Amyloidosis and Atherosclerosis.” FEBS Journal 281(11):2525–42.
Das, Madhurima, Christopher J. Wilson, Xiaohu Mei, Thomas E. Wales, John R. Engen, and Olga Gursky. 2016. “Structural Stability and Local Dynamics in Disease-Causing Mutants of Human Apolipoprotein A-I: What Makes the Protein Amyloidogenic?” Journal of Molecular Biology 428(2):449–62.
Fernandez-Escamilla, Ana Maria, Frederic Rousseau, Joost Schymkowitz, and Luis Serrano. 2004. “Prediction of Sequence-Dependent and Mutational Effects on the Aggregation of Peptides and Proteins.” Nature Biotechnology 22(10):1302–6.
Fiser, A. and A. Sali. 2003. “ModLoop: Automated Modeling of Loops in Protein Structures.” Bioinformatics 19(18):2500–2501.
Fu, Limin, Beifang Niu, Zhengwei Zhu, Sitao Wu, and Weizhong Li. 2012. “CD-HIT: Accelerated for Clustering the next-Generation Sequencing Data.” Bioinformatics 28(23):3150–52.
Fuentes, Lukas A., Wendy H. J. Beck, Maki Tsujita, and Paul M. M. Weers. 2018. “Charged Residues in the C-Terminal Domain of Apolipoprotein A-I Modulate Oligomerization.” Biochemistry 57(15):2200–2210.
Gaddi, Gisela M., Romina A. Gisonno, Silvana A. Rosú, Lucrecia M. Curto, Eduardo D. Prieto, Guillermo R. Schinella, Gabriela S. Finarelli, M. Fernanda Cortez, Letizia Bauzá, Esteban E. Elías, Nahuel A. Ramella, and M. Alejandra Tricerri. 2020. “Structural Analysis of a Natural Apolipoprotein A-I Variant (L60R) Associated with Amyloidosis.” Archives of Biochemistry and Biophysics 685:108347.
Gaglione, Rosa, Giovanni Smaldone, Rocco Di Girolamo, Renata Piccoli, Emilia Pedone, and Angela Arciello. 2018. “Cell Milieu Significantly Affects the Fate of AApoAI Amyloidogenic Variants: Predestination or Serendipity?” Biochimica et Biophysica Acta (BBA) - General Subjects 1862(3):377–84.
Gisonno, Romina A., Eduardo D. Prieto, Juan P. Gorgojo, Lucrecia M. Curto, M. Eugenia Rodriguez, Silvana A. Rosú, Gisela M. Gaddi, Gabriela S. Finarelli, M. Fernanda Cortez, Guillermo R. Schinella, M. Alejandra Tricerri, and Nahuel A. Ramella. 2020. “Fibrillar Conformation of an Apolipoprotein A-I Variant Involved in Amyloidosis and Atherosclerosis.” Biochimica et Biophysica Acta - General Subjects 1864(4):129515.
Gogonea, Valentin. 2016. “Structural Insights into High Density Lipoprotein: Old Models and New Facts.” Frontiers in Pharmacology 6.
Guerois, Raphael, Jens Erik Nielsen, and Luis Serrano. 2002. “Predicting Changes in the Stability of Proteins and Protein Complexes: A Study of More than 1000 Mutations.” Journal of Molecular Biology 320(2):369–87.
Gursky, Olga and David Atkinson. 1996. “Thermal Unfolding of Human High-Density Apolipoprotein A-1: Implications for a Lipid-Free Molten Globular State.” Proceedings of the National Academy of Sciences of the United States of America 93(7):2991–95.
Kalyaanamoorthy, Subha, Bui Quang Minh, Thomas K. F. Wong, Arndt von Haeseler, and Lars S. Jermiin. 2017. “ModelFinder: Fast Model Selection for Accurate Phylogenetic Estimates.” Nature Methods 14(6):587–89.
Karczewski, Konrad J., Laurent C. Francioli, Grace Tiao, Beryl B. Cummings, Jessica Alföldi, Qingbo Wang, Ryan L. Collins, Kristen M. Laricchia, Andrea Ganna, Daniel P. Birnbaum, Laura D. Gauthier, Harrison Brand, Matthew Solomonson, Nicholas A. Watts, Daniel Rhodes, Moriel Singer-Berk, Eleina M. England, Eleanor G. Seaby, Jack A. Kosmicki, Raymond K. Walters, Katherine Tashman, Yossi Farjoun, Eric Banks, Timothy Poterba, Arcturus Wang, Cotton Seed, Nicola Whiffin, Jessica X. Chong, Kaitlin E. Samocha, Emma Pierce-Hoffman, Zachary Zappala, Anne H. O’Donnell-Luria, Eric Vallabh Minikel, Ben Weisburd, Monkol Lek, James S. Ware, Christopher Vittal, Irina M. Armean, Louis Bergelson, Kristian Cibulskis, Kristen M. Connolly, Miguel Covarrubias, Stacey Donnelly, Steven Ferriera, Stacey Gabriel, Jeff Gentry, Namrata Gupta, Thibault Jeandet, Diane Kaplan, Christopher Llanwarne, Ruchi Munshi, Sam Novod, Nikelle Petrillo, David Roazen, Valentin Ruano-Rubio, Andrea Saltzman, Molly Schleicher, Jose Soto, Kathleen Tibbetts, Charlotte Tolonen, Gordon Wade, Michael E. Talkowski, Benjamin M. Neale, Mark J. Daly, and Daniel G. MacArthur. 2020. “The Mutational Constraint Spectrum Quantified from Variation in 141,456 Humans.” Nature 581(7809):434–43.
Kareinen, Ilona, Marc Baumann, Su Duy Nguyen, Katariina Maaninka, Andrey Anisimov, Minoru Tozuka, Matti Jauhiainen, Miriam Lee-Rueckert, and Petri T. Kovanen. 2018. “Chymase Released from Hypoxia-Activated Cardiac Mast Cells Cleaves Human ApoA-I at Tyr192 and Compromises Its Cardioprotective Activity.” Journal of Lipid Research 59(6):945–57.
Koster, J. and S. Rahmann. 2012. “Snakemake--a Scalable Bioinformatics Workflow Engine.” Bioinformatics 28(19):2520–22.
Langenberg, Tobias, Rodrigo Gallardo, Rob van der Kant, Nikolaos Louros, Emiel Michiels, Ramon Duran-Romaña, Bert Houben, Rafaela Cassio, Hannah Wilkinson, Teresa Garcia, Chris Ulens, Joost Van Durme, Frederic Rousseau, and Joost Schymkowitz. 2020. “Thermodynamic and Evolutionary Coupling between the Native and Amyloid State of Globular Proteins.” Cell Reports 31(2):107512.
Leman, Luke J., Bruce E. Maryanoff, and M. Reza Ghadiri. 2013. “Molecules That Mimic Apolipoprotein A-I: Potential Agents for Treating Atherosclerosis.” Journal of Medicinal Chemistry 57(6):2169–96.
Letunic, Ivica and Peer Bork. 2019. “Interactive Tree Of Life (ITOL) v4: Recent Updates and New Developments.” Nucleic Acids Research 47(W1):W256--W259.
Louros, Nikolaos, Katerina Konstantoulea, Matthias De~Vleeschouwer, Meine Ramakers, Joost Schymkowitz, and Frederic Rousseau. 2019. “WALTZ-DB 2.0: An Updated Database Containing Structural Information of Experimentally Determined Amyloid-Forming Peptides.” Nucleic Acids Research 48(D1):D389--D393.
Lund-Katz, Sissel and Michael C. Phillips. 2010. “High Density Lipoprotein Structure–Function and Role in Reverse Cholesterol Transport.” Pp. 183–227 in Cholesterol Binding and Cholesterol Transport Proteins: Springer Netherlands.
Machado, Matías R., Exequiel E. Barrera, Florencia Klein, Martín Sóñora, Steffano Silva, and Sergio Pantano. 2019. “The SIRAH 2.0 Force Field: Altius, Fortius, Citius.” Journal of Chemical Theory and Computation 15(4):2719–33.
Machado, Matías R. and Sergio Pantano. 2016. “SIRAH Tools: Mapping, Backmapping and Visualization of Coarse-Grained Models.” Bioinformatics 32(10):1568–70.
Machado, Matías R. and Sergio Pantano. 2020. “Split the Charge Difference in Two! A Rule of Thumb for Adding Proper Amounts of Ions in MD Simulations.” Journal of Chemical Theory and Computation 16(3):1367–72.
Manthei, Kelly A., Dhabaleswar Patra, Christopher J. Wilson, Maria V Fawaz, Lolita Piersimoni, Jenny Capua Shenkar, Wenmin Yuan, Philip C. Andrews, John R. Engen, Anna Schwendeman, Melanie D. Ohi, and John J. G. Tesmer. 2020. “Structural Analysis of Lecithin:Cholesterol Acyltransferase Bound to High Density Lipoprotein Particles.” Communications Biology 3(1).
Matsunaga, Akira, Yoshinari Uehara, Bo Zhang, and Keijiro Saku. 2010. Apolipoprotein A-I Mutations. First Edit. Elsevier Inc.
Melchior, John T., Ryan G. Walker, Allison L. Cooke, Jamie Morris, Mark Castleberry, Thomas B. Thompson, Martin K. Jones, Hyun D. Song, Kerry-Anne Rye, Michael N. Oda, Mary G. Sorci-Thomas, Michael J. Thomas, Jay W. Heinecke, Xiaohu Mei, David Atkinson, Jere P. Segrest, Sissel Lund-Katz, Michael C. Phillips, and W. Sean Davidson. 2017. “A Consensus Model of Human Apolipoprotein A-I in Its Monomeric and Lipid-Free State.” Nature Structural & Molecular Biology 24(12):1093–99.
Minh, B. Q., M. A. T. Nguyen, and A. von Haeseler. 2013. “Ultrafast Approximation for Phylogenetic Bootstrap.” Molecular Biology and Evolution 30(5):1188–95.
Minh, Bui Quang, Heiko A. Schmidt, Olga Chernomor, Dominik Schrempf, Michael D. Woodhams, Arndt von Haeseler, and Robert Lanfear. 2020. “IQ-TREE 2: New Models and Efficient Methods for Phylogenetic Inference in the Genomic Era” edited by E. Teeling. Molecular Biology and Evolution 37(5):1530–34.
Mizuguchi, Chiharu, Miho Nakagawa, Norihiro Namba, Misae Sakai, Naoko Kurimitsu, Ayane Suzuki, Kaho Fujita, Sayaka Horiuchi, Teruhiko Baba, Takashi Ohgita, Kazuchika Nishitsuji, and Hiroyuki Saito. 2019. “Mechanisms of Aggregation and Fibril Formation of the Amyloidogenic N-Terminal Fragment of Apolipoprotein A-I.” Journal of Biological Chemistry 294(36):13515–24.
Mucchiano, G. I., B. Häggqvist, K. Sletten, and P. Westermark. 2001. “Apolipoprotein A-1-Derived Amyloid in Atherosclerotic Plaques of the Human Aorta.” The Journal of Pathology 193(2000):270–75.
Murrell, B., S. Moola, A. Mabona, T. Weighill, D. Sheward, S. L. Kosakovsky Pond, and K. Scheffler. 2013. “FUBAR: A Fast, Unconstrained Bayesian AppRoximation for Inferring Selection.” Molecular Biology and Evolution 30(5):1196–1205.
Navab, Mohamad, Srinivasa T. Reddy, Brian J. Van Lenten, G. M. Anantharamaiah, and Alan M. Fogelman. 2008. “The Role of Dysfunctional HDL in Atherosclerosis.” Journal of Lipid Research 50(Supplement):S145--S149.
Obici, Laura, Guido Franceschini, Laura Calabresi, Sofia Giorgetti, Monica Stoppini, Giampaolo Merlini, and Vittorio Bellotti. 2006. “Structure, Function and Amyloidogenic Propensity of Apolipoprotein A-I.” Amyloid : The International Journal of Experimental and Clinical Investigation : The Official Journal of the International Society of Amyloidosis 13(4):191–205.
Oda, Michael N. 2017. “Lipid-Free ApoA-I Structure - Origins of Model Diversity.” Biochimica et Biophysica Acta - Molecular and Cell Biology of Lipids 1862(2):221–33.
Pettersen, Eric F., Thomas D. Goddard, Conrad C. Huang, Gregory S. Couch, Daniel M. Greenblatt, Elaine C. Meng, and Thomas E. Ferrin. 2004. “UCSF Chimera?A Visualization System for Exploratory Research and Analysis.” Journal of Computational Chemistry 25(13):1605–12.
Pond, Sergei L. Kosakovsky and Simon D. W. Frost. 2005. “Not So Different After All: A Comparison of Methods for Detecting Amino Acid Sites Under Selection.” Molecular Biology and Evolution 22(5):1208–22.
Pond, Sergei L. Kosakovsky, David Posada, Michael B. Gravenor, Christopher H. Woelk, and Simon D. W. Frost. 2006. “Automated Phylogenetic Detection of Recombination Using a Genetic Algorithm.” Molecular Biology and Evolution 23(10):1891–1901.
Ponzoni, Luca, Daniel A. Peñaherrera, Zoltán N. Oltvai, and Ivet Bahar. 2020. “Rhapsody: Predicting the Pathogenicity of Human Missense Variants” edited by Y. Ponty. Bioinformatics 36(10):3084–92.
Rader, Daniel J., Eric T. Alexander, Ginny L. Weibel, Jeffrey Billheimer, and George H. Rothblat. 2008. “The Role of Reverse Cholesterol Transport in Animals and Humans and Relationship to Atherosclerosis.” Journal of Lipid Research 50(Supplement):S189--S194.
Raimondi, Sara, Fulvio Guglielmi, Sofia Giorgetti, Sonia Di Gaetano, Angela Arciello, Daria M. Monti, Annalisa Relini, Daniela Nichino, Silvia M. Doglia, Antonino Natalello, Piero Pucci, Palma Mangione, Laura Obici, Giampaolo Merlini, Monica Stoppini, Paul Robustelli, Gian Gaetano Tartaglia, Michele Vendruscolo, Christopher M. Dobson, Renata Piccoli, and Vittorio Bellotti. 2011. “Effects of the Known Pathogenic Mutations on the Aggregation Pathway of the Amyloidogenic Peptide of Apolipoprotein A-I.” Journal of Molecular Biology 407(3):465–76.
Ramella, Nahuel a, Guillermo R. Schinella, Sergio T. Ferreira, Eduardo D. Prieto, María E. Vela, José Luis Ríos, M. Alejandra Tricerri, and Omar J. Rimoldi. 2012. “Human Apolipoprotein A-I Natural Variants: Molecular Mechanisms Underlying Amyloidogenic Propensity.” PloS One 7(8):e43755.
Rosenson, Robert S., H. Bryan Brewer, Benjamin J. Ansell, Philip Barter, M. John Chapman, Jay W. Heinecke, Anatol Kontush, Alan R. Tall, and Nancy R. Webb. 2015. “Dysfunctional HDL and Atherosclerotic Cardiovascular Disease.” Nature Reviews Cardiology 13(1):48–60.
Rosú, Silvana A., Omar J. Rimoldi, Eduardo D. Prieto, Lucrecia M. Curto, José M. Delfino, Nahuel A. Ramella, and M. Alejandra Tricerri. 2015. “Amyloidogenic Propensity of a Natural Variant of Human Apolipoprotein A-I: Stability and Interaction with Ligands.” PLoS ONE 10(5):1–17.
Sievers, Fabian, Andreas Wilm, David Dineen, Toby J. Gibson, Kevin Karplus, Weizhong Li, Rodrigo Lopez, Hamish McWilliam, Michael Remmert, Johannes Söding, Julie D. Thompson, and Desmond G. Higgins. 2011. “Fast, Scalable Generation of High-Quality Protein Multiple Sequence Alignments Using Clustal Omega.” Molecular Systems Biology 7(1):539.
Sipe, Jean D., Merrill D. Benson, Joel N. Buxbaum, Shu-ichi Ikeda, Giampaolo Merlini, Maria J. M. Saraiva, and Per Westermark. 2016. “Amyloid Fibril Proteins and Amyloidosis: Chemical Identification and Clinical Classification International Society of Amyloidosis 2016 Nomenclature Guidelines.” Amyloid 23(4):209–13.
Suyama, M., D. Torrents, and P. Bork. 2006. “PAL2NAL: Robust Conversion of Protein Sequence Alignments into the Corresponding Codon Alignments.” Nucleic Acids Research 34(Web Server):W609--W612.
Tareen, Ammar and Justin B. Kinney. 2019. “Logomaker: Beautiful Sequence Logos in Python” edited by A. Valencia. Bioinformatics 36(7):2272–74.
Tiberti, Matteo, Thilde Terkelsen, Tycho Canter Cremers, Miriam Di Marco, Isabelle da Piedade, Emiliano Maiani, and Elena Papaleo. 2019. “MutateX: An Automated Pipeline for in-Silico Saturation Mutagenesis of Protein Structures and Structural Ensembles.”
Wang, Sheng, Siqi Sun, Zhen Li, Renyu Zhang, and Jinbo Xu. 2017. “Accurate De Novo Prediction of Protein Contact Map by Ultra-Deep Learning Model” edited by A. Schlessinger. PLOS Computational Biology 13(1):e1005324.
Westermark, P. P., G. G. Mucchiano, T. T. Marthin, K. H. K. H. Johnson, and K. K. Sletten. 1995. “Apolipoprotein A1-Derived Amyloid in Human Aortic Atherosclerotic Plaques.” Am J Pathol 147(5):1186–92.
Wong, Yuan Qi, Katrina J. Binger, Geoffrey J. Howlett, and Michael D. W. Griffin. 2010. “Methionine Oxidation Induces Amyloid Fibril Formation by Full-Length Apolipoprotein A-I.” Proceedings of the National Academy of Sciences of the United States of America 107(5):1977–82.

\newpage

## Supplementary material

Supplementary Figure 1 Apoa-I evolutionary rates based on codon alignments
A Evolutionary rate (dN/dS) profile for apoA-I coding sequence, estimated with FEL. Points colored in blue indicate the presence of purifying selection, while orange indicates neutral selection at a residue position.
B Evolutionary rate (dN/dS) for each residue type inside apoA-I tandem repeats. Proline and positively charged residues (K and R) display values consistent with a more stringent conservation. 

Supplementary Figure 2 Sequence logos representing apoA-I tandem repeats
Sequence logos corresponding to each of the ten tandem repeats present in apoA-I (residues 48-243) were extracted from a multiple sequence alignment of mammalian sequence using the LogoMaker package. Position-specific conservation was calculated using information content (expressed in Bits).

Supplementary Figure 3 FoldX Thermodynamic Destabilization landscape
ΔΔG values obtained by in silico saturation mutagenesis of apoA-I structure using the FoldX engine. Mutation introduced is depicted in the Y axis. Scales at the right indicate ΔΔG values expressed in kcal/mol.

Supplementary Figure 4 Rhapsody Pathogenicity landscape
Pathogenicity values obtained by in silico saturation mutagenesis of apoA-I structure using the Rhapsody package. Mutation introduced is depicted in the Y axis. Scales at the right indicate pathogenicity score (1 more pathogenic, 0 less pathogenic).

Supplementary Figure 5 Root mean square fluctuation (RMSF) profiles for apoA-I mutants
RMSF values were computed for each protein position over the last 100 ns of the simulation. Mean values are depicted together with its standard deviation.
________________
Supplementary Table 1 Coevolving residue pairs for apoA-I
res_i   res_j   Prob
32          38          0.9745979
32          41          0.9356469
29          42          0.8026068
32          42          0.7793443
10          63          0.7535808
21          52          0.7366209
33          42          0.7339497
29          45          0.7262684
14          59          0.6868986
28          45          0.6604719
25          45          0.6544870
18          56          0.6307588
18          52          0.6276968
25          49          0.6210243
14          56          0.6128104
21          49          0.6127903
14          63          0.6056398
33          39          0.6045238
7           70          0.6029568
10          66          0.6011602
10          67          0.5999863
22          49          0.5937240
7           67          0.5832257
3           9           0.5820144
7           63          0.5752648
29          46          0.5712630
18          53          0.5689167
6           66          0.5582736
10          70          0.5409693
14          228         0.5365205
6           70          0.5255757
10          59          0.5169616
28          41          0.5164070
11          60          0.5149656
32          45          0.5145751
7           66          0.5117174
11          63          0.5069553
17          59          0.5011830
________________


Supplementary Table 2 Root mean square deviation values from molecular dynamics simulations




System
	Root Mean Square Deviation (RMSD, Å)
	Replicate 1
	Replicate 2
	Replicate 3
	Replicate 4
	Replicate 5
	Mean
	Standard Deviation
	Wild type (WT)
	7.91
	7.24
	8.04
	5.39
	7.92
	7.30
	1.11
	G26R
	6.75
	10.33
	7.54
	7.65
	6.10
	7.67
	1.61
	L60R
	6.61
	6.11
	10.28
	8.30
	7.87
	7.83
	1.63
	Δ107
	7.28
	6.84
	7.77
	6.03
	8.79
	7.34
	1.03
	R173P
	8.97
	8.24
	7.14
	6.91
	8.16
	7.88
	0.85
	

[a]no parecen ser claves al model que dice gursky, el L46 esta en la region44-55, lo que pasa es que desde el 185 en adelante no estan en la estructura cristalina asi que quiza se puedan predecir
dx.doi.org/10.1021/bi2017014 | Biochemistry 2012, 51, 10−18
