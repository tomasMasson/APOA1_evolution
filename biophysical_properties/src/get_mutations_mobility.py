#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

def get_mutations_mob(dataframe, filename):

    df = pd.read_csv(dataframe)
    with open(filename, 'r') as fh:
        next(fh)
        residues = [int(item.strip())
                    for item in fh]
    print(f'Mutation,Mobility')
    for item in residues:
        print(f'{item},{df.iloc[item-1]["Monomer_sqfl"]}')

def arguments_parser():
    ''' Command line argument parser.'''

    parser = argparse.ArgumentParser()
    parser.add_argument('dataframe',
                        type=str,
                        help='Dataframe')
    parser.add_argument('filename',
                        type=str,
                        help='List')
    args = parser.parse_args()

    return args.dataframe, args.filename

def main():

    dataframe, filename = arguments_parser()
    get_mutations_mob(dataframe, filename)

if __name__ == '__main__':
    main()
