#!/usr/bin/env python3

from Bio import AlignIO
from collections import Counter
import argparse
import numpy as np
import pandas as pd

def calculate_entropy(dictionary):
    '''Calculates the entropy of a sequence list.'''

    counter = Counter(dictionary)
    counts = np.fromiter(counter.values(), dtype=float)
    prob = counts / sum(counts)
    H = -sum(prob * np.log2(prob))
    return H

def get_alignment_entropy(alignment):
    '''Calculates the Shannon entropy (H) per column of a sequence alignment.'''

    alignment = AlignIO.read(alignment, 'fasta')
    for sequence in alignment:
        if 'Homo_sapiens' in sequence.id:
            residues = [item for item in sequence.seq]
    
    alignment_array = np.array([list(sequence) for sequence in alignment])
    H_list = []
    for column in alignment_array.T:
        H_list.append(calculate_entropy(column))
        
    df = pd.DataFrame({'Residue': residues, 'Entropy':H_list})
    df = df[df['Residue'] != '-']
    df.index = range(len(df))
    return df

def main():
    '''Command line argument parser.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('Alignment', help='Sequence alignment in fasta format')
    args = parser.parse_args()
    alignment = args.Alignment
    df = get_alignment_entropy(alignment)
    df.to_csv('sequences_entropy.csv', index=False)

if __name__ == '__main__':
    main()
