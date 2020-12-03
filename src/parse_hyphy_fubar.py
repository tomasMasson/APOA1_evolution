#!/usr/bin/env python3

from Bio import AlignIO
import json
import numpy as np
import pandas as pd
import argparse


def parse_hyphy(hyphy_file):
    '''
    Takes an hyphy output file and returns two lists,
    for the data and headers.
    '''

    with open(hyphy_file, 'r') as fh:
        dic = json.load(fh)
    array = np.array(dic['MLE']['content']['0'])
    headers = [header[0] for header in dic['MLE']['headers']]
    df = pd.DataFrame(array[:, :6], columns=headers)
    df = df.loc[:, (df != 0).any(axis=0)]
    return df


def filter_dataframe(df, algn_file, reference):
    '''
    Takes a data and headers lists from parse_hyphy and filter
    the positions corresponding to SfMNPV sequence.
    Returns a pandas dataframe.
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
    Takes a datafame with hyphy results and assign a column
    displaying the type of selective pressure in each residue.
    '''

    selection_type = []
    for index, row in df.iterrows():
        if row["Prob[alpha>beta]"] >= 0.9:
            selection_type.append('Purifiyng')
        elif row["Prob[alpha<beta]"] >= 0.9:
            selection_type.append('Diversifiyng')
        else:
            selection_type.append('Neutral')
    df['Selection_type'] = selection_type
    return df


def argument_parser():
    '''Command line argument parser.'''

    parser = argparse.ArgumentParser()
    parser.add_argument('hyphy',
                        help='Hyphy results in .json format')
    parser.add_argument('align',
                        help='Sequence alignment')
    parser.add_argument('reference',
                        help='Reference sequence')
    args = parser.parse_args()
    return args.hyphy, args.align, args.reference


def main():
    hyphy_file, align, reference = argument_parser()
    df = parse_hyphy(hyphy_file)
    df = filter_dataframe(df, align, reference)
    df = assign_selective_pressure(df)
    output_file = f'{hyphy_file.split(".json")[0]}.csv'
    df.to_csv(output_file, index=True, index_label="Position")


if __name__ == '__main__':
    main()
