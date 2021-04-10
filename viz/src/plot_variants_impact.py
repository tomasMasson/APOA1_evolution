#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_variants_impact(filename):

    df = pd.read_csv(filename)
    order = ['Amyloid', 'gnomAD_v2', 'gnomAD_v3']
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
    sns.boxplot(
            x='Class',
            y='FoldX',
            data=df,
            fliersize=0,
            palette="vlag",
            hue_order=order,
            ax=ax1
            )
    # Plot individual points
    sns.stripplot(x="Class",
                  y="FoldX",
                  data=df,
                  size=4,
                  color=".3",
                  linewidth=0,
                  alpha=0.5,
                  ax=ax1)
    ax1.set(xlabel='Variant Class',
            ylabel='FoldX ΔΔG (kcal/mol)',
            ylim=(-3, 12))

    sns.boxplot(
            x='Class',
            y='Rhapsody',
            data=df,
            fliersize=0,
            palette="vlag",
            hue_order=order,
            ax=ax2
            )
    # Plot individual points
    sns.stripplot(x="Class",
                  y="Rhapsody",
                  data=df,
                  size=4,
                  color=".3",
                  linewidth=0,
                  alpha=0.5,
                  ax=ax2)
    ax2.set(xlabel='Variant Class',
            ylabel='Pathogenicity Probability',
            ylim=(0, 1))
    plt.savefig('variants_effect.svg')

    fig, ax = plt.subplots(1, 1, figsize=(5.5, 4))
    ax.set(xscale='log')
    sns.scatterplot(
            x='Frequency',
            y='FoldX',
            data=df,
            color='gray',
            ax=ax
            )
    ax.set(xlabel='Allele Frequency',
           ylabel='FoldX ΔΔG (kcal/mol)')
    fig.savefig('variants_frequency.svg')


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
