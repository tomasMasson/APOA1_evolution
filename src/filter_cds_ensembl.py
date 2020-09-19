#!/usr/bin/env python3

from Bio import SeqIO
import argparse


def filter_sequences(raw_cds, dataset):
    '''
    Takes a list of protein sequences identifiers from a dataset
    and search the cds inside a coding sequences multifasta.
    '''

    protein_seqs = SeqIO.parse(dataset, 'fasta')
    ids = [sequence.id for sequence in protein_seqs]
    cds = SeqIO.parse(raw_cds, 'fasta')
    for sequence in cds:
        if sequence.id in ids:
            print(f'>{sequence.id}\n{sequence.seq}\n')


def argument_parser():
    ''' Command line argument parser.'''

    parser = argparse.ArgumentParser(
            description="""
            Takes a multifasta file containing Ensembl CDS an
            retain only the sequences that are present in the
            protein dataset supplied.
            Results are returned to standard output.""",
            usage="python3 filter_cds_ensembl.py <raw_cds> <proteins_dataset>"
            )
    parser.add_argument('raw_cds',
                        help='File with cds in fasta format')
    parser.add_argument('dataset',
                        help='File with proteins dataset')
    args = parser.parse_args()
    return args.raw_cds, args.dataset


def main():
    raw_cds, dataset = argument_parser()
    filter_sequences(raw_cds, dataset)


if __name__ == '__main__':
    main()
