#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_foldx_heatmap(filename):

    df = pd.read_csv(filename, index_col='Site')
    for i in range(3):
        start = int(243/3 * i)
        end = int(243/3 * (i+1))
        plt.figure(figsize=(16, 8))
        sns.heatmap(df[start:end].T,
                    vmin=5,
                    vmax=-3,
                    cmap='coolwarm',
                    cbar=True,
                    cbar_kws={"shrink": .4},
                    xticklabels=3,
                    square=True)
        name = f'foldx_mutagenesis{i+1}.svg'
        plt.savefig(name)
    plt.close('all')


def plot_foldx_histogram(filename):
    df = pd.read_csv(filename, index_col='Site')
    sns.distplot(df,
                 bins=100,
                 color='k',
                 kde=False,
                 norm_hist=True)
    plt.xlim(-5, 20)
    plt.xlabel('ddG')
    plt.ylabel('Frequency')
    plt.savefig('foldx_ddg_histogram.svg')


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
    plot_foldx_heatmap(filename)
    plot_foldx_histogram(filename)


if __name__ == '__main__':
    main()
