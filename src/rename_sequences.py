#!/usr/bin/env python3

from Bio import SeqIO
import argparse

def rename_sequences(multifasta, species_names):
    ''' Takes a multifasta file and appends the species name to each sequence header'''

    sequences = SeqIO.parse(multifasta, 'fasta')
    species = {}
    with open(species_names, 'r') as fh:
        for record in fh:
            identifier, name = record.strip().split(',')
            species[identifier] = name
            
    output_name = f'{multifasta.split(".")[0]}_labeled.{multifasta.split(".")[1]}'
    with open(output_name, 'w') as fh: 
        for sequence in sequences:
            if sequence.id in species.keys():
                sequence.id = f'{species[sequence.id]} {sequence.id} '
            fh.write(f'>{sequence.id}\n{sequence.seq}\n')

def main():
    prs = argparse.ArgumentParser()
    prs.add_argument('Sequences', help='File with sequeces')
    prs.add_argument('Names', help='File containing the species name')
    args = prs.parse_args()
    multifasta = args.Sequences
    species = args.Names
    rename_sequences(multifasta, species)

if __name__ == '__main__':
    main()
