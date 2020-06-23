#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_variants_impact(filename):

    df = pd.read_csv(filename)
    plt.figure(figsize=(4, 4))
    sns.boxplot(x='Class', y='FoldX', data=df)
    plt.savefig('variants_foldx.svg')
    plt.close()

    plt.figure(figsize=(4, 4))
    sns.boxplot(x='Class', y='Rhapsody', data=df)
    plt.savefig('variants_rhapsody.svg')

    plt.figure(figsize=(4, 4))
    sns.boxplot(x='Class', y='Envision', data=df)
    plt.savefig('variants_envision.svg')


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
