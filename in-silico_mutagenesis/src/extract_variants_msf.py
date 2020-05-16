#!/usr/bin/env python3

from pathlib import Path
import argparse
import pandas as pd

def get_variants_msf(datafile, variants):
    ''' 
    Retrieves the Mean Square Fluctuation (MSF) from a dataset.
    Variants must be specified as residue position.
    '''
    
    df = pd.read_csv(datafile)
    with open(variants, 'r') as fh:
        next(fh)
        print(f'Residues MSF')
        for line in fh:
            site = int(line[1:-2])
            print(line.strip(), df.loc[site, 'msf'])

def arguments_parser():    
    ''' Command line argument parser.'''

    parser = argparse.ArgumentParser()
    parser.add_argument('datafile', 
                        type=str,
                        help='Dataset with MSF values')
    parser.add_argument('variants', 
                        type=str,
                        help='Dataset with variants')
    args = parser.parse_args()
    return args.datafile, args.variants

def main():

    datafile, variants = arguments_parser()
    data = get_variants_msf(datafile, variants)

if __name__ == '__main__':
    main()
