#!/usr/bin/env python3

from Bio import SeqIO
import argparse
import sys

def filter_sequences(multifasta):
    ''' Takes a multifasta file and remove sequences less than 200 amini acids, not starting with a methionine or with an undefined character.'''
    sequences = SeqIO.parse(multifasta, 'fasta')
    
    with open(f'{multifasta}_filtered', 'w') as fh:
        for sequence in sequences:
            seq = sequence.seq
            if len(seq) >= 200 and seq.startswith('M') and 'X' not in seq:
                fh.write(f'>{sequence.id}\n{seq}\n')

def main():
    '''Command-line argument parser.'''
    
    parser = argparse.ArgumentParser()
    parser.add_argument('sequences', help='File with sequences')
    args = parser.parse_args()
    multifasta = args.sequences
    filter_sequences(multifasta)

if __name__ == '__main__':
    main()
