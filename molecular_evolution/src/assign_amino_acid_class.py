#!/usr/bin/env python3

import pandas as pd
import argparse


def assign_amino_acid_class(dataset):
    '''
    Takes a dataset with a column containing protein residues and
    returns each residue biophysical class to standard output.
    '''

    classes = {
        'A': 'Hydrophobic',
        'C': 'Polar',
        'D': 'Charged',
        'E': 'Charged',
        'F': 'Aromatic',
        'G': 'Glycine',
        'H': 'Polar',
        'I': 'Hydrophobic',
        'K': 'Charged',
        'L': 'Hydrophobic',
        'M': 'Hydrophobic',
        'N': 'Polar',
        'P': 'Proline',
        'Q': 'Polar',
        'R': 'Charged',
        'S': 'Polar',
        'T': 'Polar',
        'V': 'Hydrophobic',
        'W': 'Aromatic',
        'Y': 'Aromatic',
        }

    data = pd.read_csv(dataset, header=0)
    for residue in data.Residue:
        print(classes[residue])


def argument_parser():
    '''Command line argument parser.'''

    parser = argparse.ArgumentParser()
    parser.add_argument('dataset',
                        help='Dataset in .csv format')
    args = parser.parse_args()
    return args.dataset


def main():
    dataset = argument_parser()
    assign_amino_acid_class(dataset)


if __name__ == '__main__':
    main()
