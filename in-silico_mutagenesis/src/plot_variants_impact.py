#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_variants_impact(filename):
    
    mutations = ['G', 'A', 'V', 'L', 'I', 'M', 'F', 'W', 'P', 'S',
                 'T', 'C', 'Y', 'N', 'Q', 'D', 'E', 'K', 'R', 'H']

    df = pd.read_csv(filename)
    plt.figure(figsize=(4,4))
    sns.boxplot(x='Class', y='ddG', data=df)
    plt.savefig('variants_ddg.svg')
    plt.close()
    
    plt.figure(figsize=(4,4))
    sns.boxplot(x='Class', y='Pathogenicity', data=df)
    plt.savefig('variants_pathog.svg')

    plt.figure(figsize=(4,4))
    sns.boxplot(x='Class', y='MSF', data=df)
    plt.savefig('variants_MSF.svg')

def arguments_parser():    
    ''' Command line argument parser.'''

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', 
                        type=str,
                        help='List')
    args = parser.parse_args()
    return args.filename

def main():
    filename = arguments_parser()
    plot_variants_impact(filename)

if __name__ == '__main__':
    main()
