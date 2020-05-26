#!/usr/bin/env python3

import argparse
import csv


def reformat_gnomad_data(filename):
    '''
    Reformat the mutation data retrieved from gnomAD from
    three letters to one letter amino acid code.
    '''

    aa_codes = {'Ala': 'A', 'Cys': 'C', 'Asp': 'D', 'Glu': 'E',
                'Phe': 'F', 'Gly': 'G', 'His': 'H', 'Ile': 'I',
                'Lys': 'K', 'Leu': 'L', 'Met': 'M', 'Asn': 'N',
                'Pro': 'P', 'Gln': 'Q', 'Arg': 'R', 'Ser': 'S',
                'Thr': 'T', 'Val': 'V', 'Trp': 'W', 'Tyr': 'Y'
                }

    with open(filename, 'r') as fh:
        reader = csv.reader(fh)
        next(reader)
        for line in reader:
            data = line[8]
            if data[-3:] in aa_codes:
                mutation = aa_codes[data[-3:]]
                position = int(data[5:-3])
                aa = aa_codes[data[2:5]]
            if position > 24:
                print(f'{aa}{position-24}{mutation}')


def argument_parser():
    '''Command line argument parser.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='CSV file with gnomAD data')
    args = parser.parse_args()
    return args.file


def main():
    filename = argument_parser()
    reformat_gnomad_data(filename)


if __name__ == '__main__':
    main()
