#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse


def plot_dataset(dataframe):
    sns.set(style="white")
    sns.distplot(
            dataframe['Position'],
            color='#0571b0',
            bins=20,
            kde=False
            )
    df = dataframe[dataframe['Taxon'] == 'Mammalia']
    sns.distplot(
            df['Position'],
            color='#e66101',
            bins=20,
            kde=False
            )
    plt.xlabel('Sequence Position')
    plt.ylabel('# Amyloid Regions')
    plt.savefig('amyloid_regions_distribution.svg')
    return plt.show()


def argument_parser():
    '''Command line argument parser.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset',
                        help='Dataset file in .csv format')
    args = parser.parse_args()
    return args.dataset


def main():
    dataset = argument_parser()
    df = pd.read_csv(dataset)
    df.pipe(plot_dataset)


if __name__ == "__main__":
    main()
