#!/usr/bin/env python3

from Bio import AlignIO
import matplotlib.pyplot as plt
import logomaker
import argparse


def make_logo(filename, i: int, j: int):
    '''
    Print a sequence logo from a multiple sequence alignment
    in Fasta format.
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
                                   color_scheme='NajafabadiEtAl2017')
    sequence_logo.ax.set_xticks(range(len(sequence_matrix)))
    sequence_logo.ax.tick_params(labelsize=10)
    sequence_logo.ax.set_xticklabels(f'{x}'
                                     for x in range(start+1, end+1, 1))
    sequence_logo.ax.set_xlabel('Sequence Position', fontsize=14)
    sequence_logo.ax.set_ylabel('Information (Bits)', fontsize=14)
    plt.savefig('sequence_logo.svg')
    return plt.show()


def argument_parser():
    '''Command line argument parser.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('align',
                        help='Alignment file in Fasta format')
    parser.add_argument('start',
                        type=int,
                        help='Logo start position')
    parser.add_argument('end',
                        type=int,
                        help='Logo end position')
    args = parser.parse_args()
    return args.align, args.start, args.end


def main():
    filename, start, end = argument_parser()
    make_logo(filename, start, end)


if __name__ == '__main__':
    main()
