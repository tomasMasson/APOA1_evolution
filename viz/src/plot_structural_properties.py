#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse


def plot_structural_features_profile(filename):
    '''
    Plot a composite graph displaying the profiles for
    MSF, WCN, solubility and beta zipper tendency values
    from a .csv file
    '''
    df = pd.read_csv(filename)
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(8,12))
    sns.lineplot(
            x='pdb_position',
            y='intrinsic_score',
            color='gray',
            data=df,
            ax=ax1
            )
    sns.lineplot(
            x='pdb_position',
            y='structurally_corrected_score',
            color='black',
            data=df,
            ax=ax1
            )
    ax1.set(xlabel='', ylabel='CamSol Score')
    ax1.axhline(-1, color='#fc9272', ls='--')
    sns.lineplot(
            x='pdb_position',
            y='rosetta_energy',
            color='gray',
            data=df,
            ax=ax2
            )
    ax2.set(xlabel='', ylabel='Rosetta Energy (kcal/mol)')
    ax2.axhline(-23, color='#fc9272', ls='--')
    sns.lineplot(
            x='pdb_position',
            y='msf',
            color='gray',
            data=df,
            ax=ax3
            )
    ax3.set(xlabel='', ylabel='MSF')
    sns.lineplot(
            x='pdb_position',
            y='wcn_sc',
            color='gray',
            data=df,
            ax=ax4
            )
    ax4.set(xlabel='', ylabel='WCN')

    plt.xlabel('Sequence Position')
    plt.savefig('structural_features.svg')


def argument_parser():
    '''Command line argument parser.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('file',
                        help='Data file in .csv format')
    args = parser.parse_args()
    return args.file


def main():
    filename = argument_parser()
    plot_structural_features_profile(filename)


if __name__ == '__main__':
    main()
