#!/usr/bin/env python3

from prody import *
from pylab import *
import argparse


def calculate_GNM(pdb):
    '''
    Parse a .pdb structure and calculates residue mobility using Prody.
    '''
    prot = parsePDB(pdb)
    calphas = prot.select('calpha')
    gnm = GNM('prot')
    gnm.buildKirchhoff(calphas)
    gnm.calcModes()
    residues_fluct = calcSqFlucts(gnm[:10])
    for fluct in residues_fluct:
        print(fluct)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('PDB', help='PDB file')
    args = parser.parse_args()
    pdb = args.PDB
    calculate_GNM(pdb)


if __name__ == '__main__':
    main()
