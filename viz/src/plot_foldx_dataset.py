#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


def plot_foldx_heatmap(filename):

    df = pd.read_csv(filename, index_col='Site')
    for i in range(3):
        start = int(243/3 * i)
        end = int(243/3 * (i+1))
        plt.figure(figsize=(16, 8))
        sns.heatmap(df[start:end].T,
                    vmin=5,
                    vmax=-3,
                    cmap='coolwarm',
                    cbar=True,
                    cbar_kws={"shrink": .4},
                    xticklabels=3,
                    square=True)
        name = f'foldx_mutagenesis{i+1}.svg'
        plt.savefig(name)
    plt.close('all')


def plot_foldx_histogram_impact(filename):
    """
    Plot ΔΔG distribution and values associated with
    each APR region
    """

    df = pd.read_csv(filename, index_col='Site')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 3))
    sns.distplot(df,
                 bins=100,
                 color='k',
                 kde=False,
                 norm_hist=True,
                 ax=ax1)
    ax1.set(xlabel="ΔΔG (kcal/mol)",
           ylabel="Frequency",
           xlim=(-5, 20))

    # Compute average ΔΔG values for each position
    df["Average_ΔΔG"] = df.iloc[:,1:].mean(axis=1)
    # Discard extreme values
    df = df[df["Average_ΔΔG"] < 12]
    # Add APR/non-APR labels
    df["Class"] = "non-APR"
    df.loc[14:19, "Class"] = "APR1"
    df.loc[53:59, "Class"] = "APR2"
    df.loc[67:72, "Class"] = "APR3"
    df.loc[227:232, "Class"] = "APR4"
    df.to_csv("tmp.csv")
    # Plot ΔΔG data points for each APR
    sns.boxplot(
            x='Class',
            y='Average_ΔΔG',
            data=df,
            fliersize=0,
            palette="vlag",
            ax=ax2
            )
    # Plot ΔΔG single data points for each APR
    sns.stripplot(x="Class",
                  y="Average_ΔΔG",
                  data=df,
                  size=4,
                  color=".3",
                  linewidth=0,
                  alpha=0.5,
                  ax=ax2)
    ax2.set(xlabel="APR Class",
           ylabel="FoldX ΔΔG (kcal/mol)",
           ylim=(-3, 12))

    plt.savefig('foldx_distribution_impact.svg')

    # Perform Mann Whitney U test for ΔΔG of APR and non-APR residues
    apr1 = list(df[df["Class"] == "APR1"]["Average_ΔΔG"])
    apr2 = list(df[df["Class"] == "APR2"]["Average_ΔΔG"])
    apr3 = list(df[df["Class"] == "APR3"]["Average_ΔΔG"])
    apr4 = list(df[df["Class"] == "APR4"]["Average_ΔΔG"])
    non_apr = list(df[df["Class"] == "non-APR"]["Average_ΔΔG"])
    print("ΔΔG Mann Whitney U test APR1 vs non-APR:")
    print(stats.mannwhitneyu(apr1, non_apr))
    print("ΔΔG Mann Whitney U test APR1 vs APR2:")
    print(stats.mannwhitneyu(apr1, apr2))
    print("ΔΔG Mann Whitney U test APR1 vs APR3:")
    print(stats.mannwhitneyu(apr1, apr3))
    print("ΔΔG Mann Whitney U test APR1 vs APR4:")
    print(stats.mannwhitneyu(apr1, apr4))



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
    plot_foldx_heatmap(filename)
    plot_foldx_histogram_impact(filename)


if __name__ == '__main__':
    main()
