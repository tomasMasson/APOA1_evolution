#!/usr/bin/env python3
'''
Takes MISTIC output file as command line input and returns a file for each of the
variables calculated (Conservation, Res. Distance, mfDCA, MI, gaussDCA and
plmDCA)
'''
import json
import argparse

def mistic_output_parser(input_file, key):

    '''Takes a json output dictionary from Mistic and convert it to a list file.'''
    with open(input_file, 'r') as fh:
        results = json.load(fh)
    
    print(f'i,j,Score')
    for record in results[key]:
        print(f'{record[0]},{record[1]},{record[2]}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('Results', help='File containing the output from Mistic2')
    parser.add_argument('Measure', help='Field to extract from json file (available fields are "Conservation", "Residue Distances", "mfDCA", "MI", "gaussianDCA", "plmDCA"')
    args = parser.parse_args()
    
    input_file = args.Results
    key = args.Measure
    mistic_output_parser(input_file, key)

if __name__ == '__main__':
    main()
