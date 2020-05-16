#!/usr/bin/env python3

import pandas as pd
import argparse

def extract_data(filename):
    '''
    Parse mutants pathogenicity score from Rhapsody output file
    and creates a .csv file ready to be used by Pandas for plotting.
    '''

    variants = {'G': [], 'A': [], 'V': [], 'L': [], 'I': [],
                'M': [], 'F': [], 'W': [], 'P': [], 'S': [],
                'T': [], 'C': [], 'Y': [], 'N': [], 'Q': [],
                'D': [], 'E': [], 'K': [], 'R': [], 'H': []}

    with open(filename, 'r') as fh:
        next(fh)
        count = 1
        for line in fh:
            record = line.split()
            mut = record[3]
            prob = float(record[6])
            variants[mut].append(prob)
            count += 1
            if count == 20:
                site = record[2]
                variants[site].append(0.5)
                count = 1
    df = pd.DataFrame.from_dict(variants)
    df = df.iloc[24:, :]
    df['Site'] = list(range(1, 244, 1))
    cols = df.columns.to_list()
    cols = cols[-1:] + cols[:-1]
    df = df[cols]
    df.to_csv('rhapsody_dataset.csv', index=False)

def argument_parser():
    '''Command line argument parser.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='Rhapsody results file')
    args = parser.parse_args()
    return args.file

def main():
    filename = argument_parser()
    extract_data(filename)

if __name__ == '__main__':
    main()
