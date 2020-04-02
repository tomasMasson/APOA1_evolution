#!/usr/bin/env python3

import argparse

def fix_refseq_header(multifasta):
    '''Modify the header of the sequences in a multifasta file to mantain only the unique protein identifier.'''

    with open(multifasta, 'r') as fh:
        for record in fh:
            if record.startswith('>'):
                header = f"{record.split('_')[3]}_{record.split('_')[4]}"
                print(f'>{header}')            
            else:
                print(record.strip())

def main():
    ''' Command line argument parser.'''

    prs = argparse.ArgumentParser()
    prs.add_argument('Sequences', help='File with sequences')
    args = prs.parse_args()
    multifasta = args.Sequences
    fix_refseq_header(multifasta)
    
if __name__ == '__main__':
    main()
