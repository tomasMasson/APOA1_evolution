#!/usr/bin/env python3.8

import argparse
import requests


def fetch_ensembl_sequences(molecule_type, outfile):
    """
    Download apoa1 ortholog sequences using
    Ensembl REST API.

    Available molecule type are protein or nucleotide.
    """

    # Ensembl REST server
    server = "https://rest.ensembl.org"
    # APOA1 gene identifier
    apoa1 = "ENSG00000118137"
    # Set type of molecule to retrieve
    if molecule_type == "protein":
        ext = f"/homology/id/{apoa1}?"
    if molecule_type == "nucleotide":
        ext = f"/homology/id/{apoa1}?;sequence=cdna"
    # Make request
    r = requests.get(server+ext, headers={"Content-Type": "application/json"})
    # Convert request to a JSON dictionary
    decoded = r.json()

    # Save sequences to file
    with open(outfile, 'w') as fh:
        # Iterate over all orthologs stored in the dictionary
        for seq in decoded['data'][0]['homologies']:
            species = seq['target']['species'].capitalize()
            protein_id = seq['target']['protein_id']
            # Write species and protein id as sequence identifier
            fh.write(f">{species}_{protein_id}\n")
            # Extract sequence from pairwise alignment and remove gaps
            fh.write(f"{seq['target']['align_seq'].replace('-', '')}\n")
        # Add human apoa1 sequence
        species = seq['source']['species'].capitalize()
        protein_id = seq['source']['protein_id']
        fh.write(f">{species}_{protein_id}\n")
        fh.write(f"{seq['source']['align_seq'].replace('-', '')}\n")


def main():
    """Command line argument parser"""

    parser = argparse.ArgumentParser()
    parser.add_argument("molecule_type",
                        help="protein or nucleotide")
    parser.add_argument("outfile",
                        help="Output file name")
    args = parser.parse_args()
    # Retrieve sequences
    fetch_ensembl_sequences(args.molecule_type, args.outfile)


if __name__ == "__main__":
    main()
