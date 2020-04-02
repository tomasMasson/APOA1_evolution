#!/usr/bin/env python3

from Bio import SeqIO
import sys

def rename_sequences(multifasta, species_names):
    ''' Takes a multifasta file and appends the species name to each sequence header'''

    sequences = SeqIO.parse(multifasta, 'fasta')
    species = {}
    with open(species_names, 'r') as fh:
        for record in fh:
            identifier, name = record.strip().split(',')
            species[identifier] = name
            
    with open('data/sequences_dataset_labeled.faa', 'w') as fh: 
        for sequence in sequences:
            if sequence.id in species.keys():
                sequence.id = f'{species[sequence.id]} {sequence.id} '
            fh.write(f'>{sequence.id}\n{sequence.seq}\n')

if __name__ == '__main__':
    input_file = sys.argv[1]
    name_list = sys.argv[2]
    rename_sequences(input_file, name_list)
