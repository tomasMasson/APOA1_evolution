#!/usr/bin/env python3

from Bio import SeqIO
import sys


def prepare_TANGO_configuration(input_file):
    """
    Takes a multifasta file and outputs a
    TANGO configuration file.
    """

    sequences = SeqIO.parse(input_file, 'fasta')
    configuration = []
    for sequence in sequences:
        name, seq = sequence.id, sequence.seq
        configuration.append(f'{name} N N 7 310 0.1 {seq}\n')
    return configuration


if __name__ == '__main__':
    input_file = sys.argv[1]

    with open('TANGO_configuration.txt', 'w') as fh:
        for item in prepare_TANGO_configuration(input_file):
            fh.write(item)
