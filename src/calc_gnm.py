#!/usr/bin/env python3

from prody import *
from pylab import *
import argparse


def calculate_GNM(pdb):
    """
    Parse a .pdb structure and calculates residue mobility using Prody.
    """

    # Read the pdb file
    prot = parsePDB(pdb)
    # Select the protein's alpha-carbons for calculations
    calphas = prot.select('calpha')
    # Instantiate a GNM model
    gnm = GNM('prot')
    # Build the Kirchhoff matrix between nodes
    gnm.buildKirchhoff(calphas)
    # Compute the normal modes
    gnm.calcModes()
    # Get the fluctuations from the ten first modes
    residues_fluct = calcSqFlucts(gnm[:10])

    # Return a Numpy array with the residues fluctuations
    return residues_fluct


def main():
    # Command-line argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('PDB', help='PDB file')
    args = parser.parse_args()
    pdb = args.PDB

    # Compute fluctuations
    fluct = calculate_GNM(pdb)
    # Set the output file name (replace the .pdb extension with .msf)
    outfile = f"{pdb.split('.pdb')[0]}.msf"
    # Store the structure name (compatible with the Snakemake workflow)
    model = pdb.split("/")[1]
    # Write down the results into the output file
    with open(outfile, "w") as fh:
        # Header with the model name
        fh.write(f"{model}\n")
        # fluctuation data
        for field in fluct:
            fh.write(f"{str(field)}\n")


if __name__ == '__main__':
    main()
