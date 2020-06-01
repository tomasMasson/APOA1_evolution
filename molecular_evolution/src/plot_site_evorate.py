#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

def dataset_entry(data):
    df = pd.read_csv(data)
    return df

def plot_dataset(dataframe):
    sns.set(style="ticks")
    ax = sns.scatterplot(
            x=range(1,244),
            y='Omega',
            hue='Selection_type',
            data=dataframe[24:],
            palette='colorblind'
            )
    ax.set(xlabel='Sequence Position', ylabel='dN/dS')
    plt.savefig('site_evolutionary_rate.svg')
    plt.savefig('site_evolutionary_rate.png')
    return plt.show()

def main():
    '''Command line argument parser.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset', help='Dataset file in .csv format')
    args = parser.parse_args()
    dataset = args.dataset
    
    df = dataset_entry(dataset)
    df.pipe(plot_dataset)

if __name__ == "__main__":
    main()
    
