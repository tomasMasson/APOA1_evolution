#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

def dataset_entry(data):
    df = pd.read_csv(data)
    df = df.iloc[67:265]
    return df

def plot_dataset(dataframe):
    sns.set(style="ticks")
    ax = sns.boxplot(
            x=dataframe['Repeat_site'],
            y='Omega',
            data=dataframe,
            color='peachpuff',
            order=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                '21', '22']
            )
    ax.set(xlabel='Repeat Position', ylabel='dN/dS')
    plt.savefig('repeats_evolutionary_rate.svg')
    plt.savefig('repeats_evolutionary_rate.png')
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
    
