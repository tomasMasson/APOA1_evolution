#!/usr/bin/env python3

from prody import *
from pylab import *
import pandas as pd
import argparse

def get_GNM(pdb):
    '''
    Parse a .pdb structure an calculates residue mobility using Prody.
    '''
    prot = parsePDB(pdb)
    calphas = prot.select('calpha')
    gnm = GNM('prot')
    gnm.buildKirchhoff(calphas)
    gnm.calcModes()
    residues_fluct = calcSqFlucts(gnm[:10])
    for fluct in residues_fluct:
        print(fluct)
    # Show modes fluctuation
    showSqFlucts(gnm[:10])
    plt.show()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('PDB', help='PDB file')
    args = parser.parse_args()
    pdb = args.PDB
    get_GNM(pdb)

if __name__ == '__main__':
    main()
