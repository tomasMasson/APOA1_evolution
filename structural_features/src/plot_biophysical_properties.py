#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

def msf_profile_plot(filename):
    '''
    Plot MSF values against position using a .csv file
    '''
    df = pd.read_csv(filename)
    positions = list(range(1, 244, 1))
    sns.lineplot(x=positions, y='msf',
                 palette='deep', data=df)
    plt.xlabel('Position')
    plt.ylabel('MSF')
    plt.savefig('msf_profile.svg')
    plt.close()

def msf_wcn_plot(filename):
    '''
    Plot MSF values against WCN using a .csv file
    '''
    df = pd.read_csv(filename)
    sns.scatterplot(x='wcn_sc', y='msf',
                    palette='deep', data=df)
    plt.xlabel('WCN')
    plt.ylabel('MSF')
    plt.savefig('msf_wcn_plot.svg')
    plt.close()

def omega_msf_wcn_plot(filename):
    '''
    Plot dN/dS values against MSF ans WCN using a .csv file
    '''
    df = pd.read_csv(filename)
    fig, axs = plt.subplots(1, 2, figsize=(12,6))
    sns.scatterplot(x='msf', y='Omega',
                    palette='deep', data=df, ax=axs[0])
    sns.scatterplot(x='wcn_sc', y='Omega',
                    palette='deep', data=df, ax=axs[1])
    plt.savefig('supplementary_figure2.svg')

def argument_parser():
    '''Command line argument parser.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('file',
                        help='Data file in .csv format')
    args = parser.parse_args()
    return args.file

def main():
    filename = argument_parser()
    msf_profile_plot(filename)
    msf_wcn_plot(filename)
    omega_msf_wcn_plot(filename)

if __name__ == '__main__':
    main()
