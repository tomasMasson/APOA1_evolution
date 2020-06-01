#!/usr/bin/env python3

from Bio import SeqIO
import argparse


def filter_sequences(multifasta):
    ''' 
    Takes a multifasta file and remove sequences less than 200
    amino acids, not starting with a methionine or with an
    undefined character.
    '''

    sequences = SeqIO.parse(multifasta, 'fasta')
    out_file = f'data/filtered_{multifasta.split("raw_")[1]}'
    with open(out_file, 'w') as fh:
        for sequence in sequences:
            seq = sequence.seq
            if len(seq) >= 240 and seq.startswith('M') and 'X' not in seq:
                fh.write(f'>{sequence.id}\n{seq}\n')


def argument_parser():
    '''Command-line argument parser.'''

    parser = argparse.ArgumentParser()
    parser.add_argument('sequences', help='File with sequences')
    args = parser.parse_args()
    return args.sequences


def main():
    multifasta = argument_parser()
    filter_sequences(multifasta)


if __name__ == '__main__':
    main()
