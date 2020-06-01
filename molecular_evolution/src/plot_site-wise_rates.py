#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse


def dataset_entry(data):
    df = pd.read_csv(data)
    return df


def plot_sitewise_rates(dataframe):
    '''
    Draw a scatterplot displaying the site-wise evolutionary rate
    (dN/dS) as the first panel (left).
    In the right panel generates a boxplot showing the dN/dS value
    for each position in the helix repeats.
    '''

    sns.set(font_scale=1)
    sns.set_style("white")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(
            x=range(1, 244),
            y='Omega',
            hue='Selection_type',
            legend=False,
            data=dataframe[24:],
            palette='deep',
            ax=ax
            )
    ax.set_xlabel('Sequence Position', fontsize=14)
    ax.set_ylabel('dN/dS', fontsize=14)
    fig.savefig('Figure_1B.svg')
    plt.close()

    dataframe = dataframe.iloc[67:265]
    categories = ['1', '2', '3', '4', '5', '6', '7', '8',
                  '9', '10', '11', '12', '13', '14', '15',
                  '16', '17', '18', '19', '20', '21', '22']
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(
            x=dataframe['Repeat_site'],
            y='Omega',
            data=dataframe,
            color='lightgray',
            order=categories,
            ax=ax
            )
    ax.set_xlabel('Repeat Position', fontsize=14)
    ax.set_ylabel('dN/dS', fontsize=14)
    fig.savefig('Figure_1C.svg')


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
    df.pipe(plot_sitewise_rates)


if __name__ == "__main__":
    main()
