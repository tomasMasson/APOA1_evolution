#!/usr/bin/env python3

from pathlib import Path
import argparse
import pandas as pd

def get_foldx_results(folder):
    ''' 
    Retrieves the results from the output folder of FoldX.
    Return a dictionary containing the residue identifiers as key
    and the ddG as values.
    Residues ddg order is [G,A,V,L,I,M,F,W,P,S,T,C,Y,N,Q,D,E,K,R,H]. 
    '''
    
    cwd = str(Path.cwd()) + '/'
    results = folder
    directory = Path(cwd+results)
    data = {}
    for entry in directory.iterdir():
        with open(entry, 'r') as fh:
            next(fh)
            key = int(entry.name.split('_')[0][2:])
            data[key] = [line.split()[0] for line in fh] 
    data_sorted = {}
    for key in sorted(data.keys()):
        data_sorted[key] = data[key]
    
    columns = ['G','A','V','L','I','M','F','W','P','S',
               'T','C','Y','N','Q','D','E','K','R','H']
    df = pd.DataFrame.from_dict(data_sorted,
                                orient='index',
                                columns=columns)
    df.to_csv('foldx_dataset.csv', index_label='Site')
    return data_sorted

def arguments_parser():    
    ''' Command line argument parser.'''

    parser = argparse.ArgumentParser()
    parser.add_argument('folder', 
                        type=str,
                        help='Path to FoldX results')
    args = parser.parse_args()
    return args.folder

def main():

    results_folder = arguments_parser()
    data = get_foldx_results(results_folder)

if __name__ == '__main__':
    main()
