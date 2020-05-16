#!/usr/bin/env python3

from pathlib import Path
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

    return data_sorted

def plot_foldx_results(data):
    
    mutations = ['G', 'A', 'V', 'L', 'I', 'M', 'F', 'W', 'P', 'S',
                 'T', 'C', 'Y', 'N', 'Q', 'D', 'E', 'K', 'R', 'H']

    df = pd.DataFrame.from_dict(data,
                                orient='index',
                                columns=mutations,
                                dtype='float64')
    sns.heatmap(df[:60].T,
                vmin=-10,
                vmax=10,
                cmap='RdBu_r',
                cbar=True,
                square=True)
    plt.show()
    values = df.to_numpy().flatten()
    sns.distplot(values,
                 bins=100,
                 color='k',
                 kde=False,
                 norm_hist=True)
    plt.xlim(-5, 20)
    plt.xlabel('ddG')
    plt.ylabel('Frequency')
    plt.savefig('ddg_distribution.svg')
    plt.show()

def get_mutants_ddg(data, filename):
    
    mutations = ['G', 'A', 'V', 'L', 'I', 'M', 'F', 'W', 'P', 'S',
                 'T', 'C', 'Y', 'N', 'Q', 'D', 'E', 'K', 'R', 'H']

    df = pd.DataFrame.from_dict(data,
                                orient='index',
                                columns=mutations,
                                dtype='float64')
    with open(filename, 'r') as fh:
        next(fh)
        residues = [(int(item.strip()[1:-1]),
                    str(item.strip()[-1]),
                    str(item.strip()))
                    for item in fh]
    print(f'Mutation,ddg')
    for item in residues:
        print(item[2], df.iloc[item[0]-1][item[1]])

def arguments_parser():    
    ''' Command line argument parser.'''

    parser = argparse.ArgumentParser()
    parser.add_argument('folder', 
                        type=str,
                        help='Path to FoldX results')
    parser.add_argument('filename', 
                        type=str,
                        help='List')
    args = parser.parse_args()

    return args.folder, args.filename

def main():

    results_folder, filename = arguments_parser()
    data = get_foldx_results(results_folder)
    plot_foldx_results(data)
#    get_mutants_ddg(data, filename)

if __name__ == '__main__':
    main()
