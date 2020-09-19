#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse


def plot_evolutionary_rates(dataset):
    '''
    Draw a scatterplot displaying the site-wise
    evolutionary rate as the first panel (left).
    In the right panel generates a boxplot showing
    the evolutionary rate for each amino acid type.
    Both dN/dS and protein rates are used.
    '''

    dataframe = pd.read_csv(dataset)

    sns.set_style("white")
    fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

    sns.scatterplot(
            x=range(1, 244),
            y='Omega',
            hue='Selection_type',
            data=dataframe[24:],
            palette='deep',
            ax=ax1
            )
    ax1.set(
            xlabel="Sequence Position",
            ylabel="dN/dS")

    sns.boxplot(
            x='Residue',
            y='Omega',
            data=dataframe.iloc[67:265],
            color='#d9d9d9',
            order=['P','R','K','H','Q','D','E','W','Y',
                   'F','N','V','L','T','S','A','G','M'],
            ax=ax2
            )
    ax2.set(
            xlabel="Residue",
            ylabel="dN/dS")
    fig1.tight_layout()
    fig1.savefig('omega_rates.svg')

    sns.set_style("white")
    fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.25, 4))

    sns.scatterplot(
            x=range(1, 244),
            y='LEISR',
            data=dataframe[24:],
            color='#595959',
            ax=ax1
            )
    ax1.set(
            xlabel="Sequence Position",
            ylabel="Evolutionary Rate")

    sns.boxplot(
            x='Residue',
            y='LEISR',
            data=dataframe.iloc[67:265],
            color='#d9d9d9',
            saturation=1,
            order=['P','R','K','H','Q','D','E','W','Y',
                   'F','N','V','L','T','S','A','G','M'],
            ax=ax2
            )
    ax2.set(
            xlabel="Residue",
            ylabel="Evolutionary Rate",
            ylim=(0, 3))
    fig2.tight_layout()
    fig2.savefig('evolutionary_rates.svg')


def main():
    '''Command line argument parser.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset',
                        help='Dataset file in .csv format')
    args = parser.parse_args()
    plot_evolutionary_rates(args.dataset)


if __name__ == "__main__":
    main()
