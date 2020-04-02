#!/usr/bin/env python3

from Bio import SeqIO
import argparse

def fetch_sequences(multifasta, identifiers):
    ''' Takes a list of identifiers and search the sequences inside a multifasta file'''

    ids = [sequence.id for sequence in SeqIO.parse(identifiers, 'fasta')]
    sequences = SeqIO.parse(multifasta, 'fasta')
    for sequence in sequences:
        if sequence.id in ids:
            print(f'>{sequence.id}\n{sequence.seq}\n')

def main():
    ''' Command line argument parser.'''

    parser = argparse.ArgumentParser()
    parser.add_argument('Sequences', help='File with sequences in fasta format')
    parser.add_argument('Identifiers', help='File with identifiers')
    args = parser.parse_args()
    multifasta = args.Sequences
    identifiers = args.Identifiers
    fetch_sequences(multifasta, identifiers)

if __name__ == '__main__':
    main()
