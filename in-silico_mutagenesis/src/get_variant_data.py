#!/usr/bin/env python3

import argparse
import pandas as pd


def get_variants_data(data, variants):
    '''
    Retrieve the data value for the variants specified in
    the input file. Can be used to collect ddG values from
    FoldX or probability values from Rhapsody.
    '''

    df = pd.read_csv(data)
    with open(variants, 'r') as fh:
        next(fh)
        residues = [(int(item.strip()[1:-1]),
                    str(item.strip()[-1]),
                    str(item.strip()))
                    for item in fh]
    print('Mutation,Value')
    for item in residues:
        print(item[2], df.iloc[item[0]-1][item[1]])


def arguments_parser():
    ''' Command line argument parser.'''

    parser = argparse.ArgumentParser()
    parser.add_argument('data',
                        type=str,
                        help='CSV file with the data')
    parser.add_argument('variants',
                        type=str,
                        help='Variants list')
    args = parser.parse_args()
    return args.data, args.variants


def main():
    data, variants = arguments_parser()
    get_variants_data(data, variants)


if __name__ == '__main__':
    main()
