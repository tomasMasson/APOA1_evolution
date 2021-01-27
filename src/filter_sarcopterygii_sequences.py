#!/usr/bin/env python3

from Bio import Entrez
from Bio import SeqIO
import argparse


def taxonomic_data(taxids):
    """

    Retrieves the taxonomic information present
    at NCBI databases from a list of TaxIds.

    """

    # Always tell NCBI who you are
    Entrez.email = "tomasmasson0@gmail.com"
    # Epost againts NCBI taxonomy database
    post = Entrez.read(Entrez.epost("taxonomy",
                                    id=",".join(taxids)))
    # Store search query_key and webenv
    query_key = post['QueryKey']
    webenv = post['WebEnv']
    # Fetch the epost results
    fetch = Entrez.efetch(db="taxonomy",
                          retmode="xml",
                          webenv=webenv,
                          query_key=query_key)
    # Extract the a dictionary with the data
    data = Entrez.read(fetch)

    # Return data
    return data


def filter_sarcopterygii_sequences(multifasta, outfile):
    """
    
    Retain only the sequences from species
    belonging to the Sarcopterygii clade.

    In order to retrieve taxonomix information 
    from NCBI, the fasta header of each sequence
    has to contain its TaxId within the first
    field (underscore '_' are used as separators).

    """

    # Create a sequences list from the multifasta
    seqs = list(SeqIO.parse(multifasta, "fasta"))
    # Extract the TaxIds fields
    ids = [seq.id.split("_")[0] for seq in seqs]
    # Search taxonomic information at NCBI
    tax_data = taxonomic_data(ids)
    # Create a list with all the TaxIds corresponding
    # to Sarcopterygian species
    sarcopterygii = [ record["TaxId"] for record in tax_data
                      if "Sarcopterygii" in record["Lineage"]]

    # Create an outut file to redirect the filtered sequences
    with open(outfile, "w") as fh:
        # Iterate over the sequences
        for seq in seqs:
            # If the sequence belong to a Sarcopterygian
            if seq.id.split("_")[0] in sarcopterygii:
                # Create a simplified header (specie+id)
                seq_id = "_".join(seq.id.split("_")[1:])
                # Add sequence
                fh.write(f">{seq_id}\n{seq.seq}\n")


def main():
    """Command line argument parser"""

    parser = argparse.ArgumentParser()
    parser.add_argument("multifasta",
                        help="Multifasta input file")
    parser.add_argument("outfile",
                        help="Output file name")
    args = parser.parse_args()
    # Retrieve sequences
    filter_sarcopterygii_sequences(args.multifasta, args.outfile)


if __name__ == "__main__":
    main()
