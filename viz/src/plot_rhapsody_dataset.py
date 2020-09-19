#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_rhapsody_results(filename):

    df = pd.read_csv(filename, index_col='Site')
    for i in range(3):
        start = int(243/3 * i)
        end = int(243/3 * (i+1))
        plt.figure(figsize=(16, 8))
        sns.heatmap(df[start:end].T,
                    vmin=0,
                    vmax=1,
                    cmap='coolwarm',
                    cbar=True,
                    cbar_kws={"shrink": .4},
                    xticklabels=3,
                    square=True)
        name = f'rhapsody_mutagenesis{i+1}.svg'
        plt.savefig(name)


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
    plot_rhapsody_results(filename)


if __name__ == '__main__':
    main()
