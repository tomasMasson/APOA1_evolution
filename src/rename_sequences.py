#!/usr/bin/env python3

from Bio import SeqIO
import argparse


def add_species_name(seq_file, species_names):
    '''
    Takes a multifasta file and appends the species name
    to each sequence header.
    '''

    sequences = SeqIO.parse(seq_file, 'fasta')
    species = {}
    with open(species_names, 'r') as fh:
        for record in fh:
            identifier, name = record.strip().split(',')
            species[identifier] = name
            
    output_name = f'{seq_file.split(".")[0]}_labeled.{seq_file.split(".")[1]}'
    with open(output_name, 'w') as fh:
        for sequence in sequences:
            if sequence.id in species.keys():
                sequence.id = f'{species[sequence.id]}_{sequence.id} '
            fh.write(f'>{sequence.id}\n{sequence.seq}\n')


def argument_parser():
    '''Command line argument parser.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('sequences', help='File with sequeces')
    parser.add_argument('names', help='File containing the species name')
    args = parser.parse_args()
    return args.sequences, args.names


def main():
    sequences, names = argument_parser()
    add_species_name(sequences, names)


if __name__ == '__main__':
    main()
