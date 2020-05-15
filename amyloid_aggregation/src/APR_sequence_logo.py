#!/usr/bin/env python3

from Bio import AlignIO
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import logomaker
import argparse

def make_logo(filename, i: int, j: int):
    '''
    Prints a sequence logo from a multiple sequence alignment in Fasta 
    format.
    '''
    start = int(i) - 1
    end = int(j) - 1
    align = AlignIO.read(filename, 'fasta')
    sequence = [str(seq.seq[start:end]) for seq in align]

    sequence_matrix = logomaker.alignment_to_matrix(sequence,
                                                    None,
                                                    'information')
    sequence_logo = logomaker.Logo(sequence_matrix, 
                                   font_name='DejaVu Sans',
                                   color_scheme='hydrophobicity')
    sequence_logo.ax.tick_params(labelsize=16)
    sequence_logo.ax.set_xticklabels(f'{x}'
                                     for x in range(start, end+1, 1))
#    plt.savefig('sequence_logo.png')
    plt.show()

def argument_parser():
    '''Command line argument parser.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('align', help='Alignment file in Fasta format')
    parser.add_argument('start', type=int, help='Logo start position')
    parser.add_argument('end', type=int, help='Logo end position')
    args = parser.parse_args()
    return args.align, args.start, args.end

def main():
    filename, start, end = argument_parser()
    make_logo(filename, start, end)

if __name__ == '__main__':
    main()
