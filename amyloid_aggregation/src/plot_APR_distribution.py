#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse


def plot_dataset(dataframe):
    sns.set(style="white")
    ax = sns.distplot(
            dataframe['Position'],
            color='gray',
            bins=50,
            kde=False
            )
    ax.set(xlabel='Sequence Position', ylabel='# Amyloid Regions')
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
