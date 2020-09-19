#!/usr/bin/env python3

import argparse


def fix_refseq_header(multifasta):
    '''
    Modify the header of the sequences in a multifasta file
    to mantain only the unique protein identifier.
    '''

    with open(multifasta, 'r') as fh:
        for record in fh:
            if record.startswith('>'):
                header = f"{record.split('_')[3]}_{record.split('_')[4]}"
                print(f'>{header}')
            else:
                print(record.strip())


def argument_parser():
    ''' Command line argument parser.'''

    parser = argparse.ArgumentParser(
            description="""
            Modify Refseq sequence header to retain
            only the unique protein identifier.
            """,
            usage="python fix_refseq_header.py <sequences>"
            )
    parser.add_argument('sequences', help='Sequences file')
    args = parser.parse_args()
    return args.sequences


def main():
    multifasta = argument_parser()
    fix_refseq_header(multifasta)


if __name__ == '__main__':
    main()
