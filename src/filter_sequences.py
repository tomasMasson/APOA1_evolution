#!/usr/bin/env python3

from Bio import SeqIO
import argparse


def filter_sequences(multifasta, outfile):
    '''
    Takes a multifasta file and remove sequences less than 200
    amino acids long, not starting with a methionine or with an
    undefined character.
    '''

    sequences = SeqIO.parse(multifasta, 'fasta')
    with open(outfile, 'w') as fh:
        for sequence in sequences:
            seq = sequence.seq
            if len(seq) >= 240 and seq.startswith('M') and 'X' not in seq:
                fh.write(f'>{sequence.id}\n{seq}\n')


def argument_parser():
    '''Command line argument parser.'''

    parser = argparse.ArgumentParser(
            description="""
            Discard sequences smaller than 200 amino acids,
            without an initial methionine or with undefined
            characters (X).
            """,
            usage="python3 filter_sequences.py <sequences>"
            )
    parser.add_argument('sequences', help='File with sequences')
    parser.add_argument('outfile', help='Output file name')
    args = parser.parse_args()
    return args.sequences, args.outfile


def main():
    multifasta, outfile = argument_parser()
    filter_sequences(multifasta, outfile)


if __name__ == '__main__':
    main()
