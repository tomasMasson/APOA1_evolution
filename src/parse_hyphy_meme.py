#!/usr/bin/env python3

from Bio import AlignIO
import json
import pandas as pd
import argparse


def parse_hyphy(hyphy_file):
    '''
    Takes an hyphy output file and returns two lists, for the data and headers.
    '''
    with open(hyphy_file, 'r') as fh:
        dic = json.load(fh)
    data = dic['MLE']['content']['0']
    headers = [header[0] for header in dic['MLE']['headers']]
    df = pd.DataFrame(data, columns=headers)
    df = df.loc[:, (df != 0).any(axis=0)]
    return df


def filter_dataframe(df, algn_file, reference):
    '''
    Takes a data and headers lists from parse_hyphy and filter the positions
    corresponding to the Human sequence. Returns a pandas dataframe.
    '''
    algn = AlignIO.read(algn_file, 'fasta')
    for sequence in algn:
        if reference in sequence.id:
            residues = [item for item in sequence.seq]

    df['Residue'] = residues
    df = df[df['Residue'] != '-']
    df.index = range(1, len(df)+1, 1)
    return df


def assign_selective_pressure(df):
    '''
    Takes a datafame with hyphy results and assign a column displaying
    the type of selective pressure in each residue.
    '''
    episodic_selection = []
    for index, row in df.iterrows():
        if row['p-value'] <= 0.05:
            episodic_selection.append('Episodic Diversifiyng')
        else:
            episodic_selection.append('Not significant')
    df['Episodic Selection'] = episodic_selection
    return df


def main():
    '''Command line argument parser.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('hyphy',
                        help='File with hyphy results in .json format')
    parser.add_argument('Alignment',
                        help='Sequence alignment used to filter codons')
    parser.add_argument('reference',
                        help='Reference sequence used to filter codons')
    args = parser.parse_args()
    hyphy, alignment, reference = args.hyphy, args.Alignment, args.reference
    output_file = f'{hyphy.split(".json")[0]}.csv'
    df = parse_hyphy(hyphy)
    df = filter_dataframe(df, alignment, reference)
    df = assign_selective_pressure(df)
    df.to_csv(output_file, index=True, index_label="Position")


if __name__ == '__main__':
    main()
