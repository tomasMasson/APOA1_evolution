#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


def plot_apr_impact(filename):
    """
    Plot ΔΔG values associated with each APR region
    """

    df = pd.read_csv(filename)
    # Compute average ΔΔG values for each position
    df["Average_ΔΔG"] = df.iloc[:,1:].mean(axis=1)
    df = df[df["Average_ΔΔG"] < 12]
    # Add APR/non-APR labels
    df["Class"] = "non-APR"
    df.loc[13:18, "Class"] = "APR1"
    df.loc[52:57, "Class"] = "APR2"
    df.loc[66:71, "Class"] = "APR3"
    df.loc[226:231, "Class"] = "APR4"
    # Set figure size
    fig, ax = plt.subplots(1, 1, figsize=(5.5, 3))
    # Plot ΔΔG data points for each APR
    sns.boxplot(
            x='Class',
            y='Average_ΔΔG',
            data=df,
            fliersize=0,
#            whis=[0, 100],
            palette="vlag",
            ax=ax
            )
    # Plot ΔΔG single data points for each APR
    sns.stripplot(x="Class",
                  y="Average_ΔΔG",
                  data=df,
                  size=4,
                  color=".3",
                  linewidth=0,
                  alpha=0.5,
                  ax=ax)
    ax.set(xlabel="",
           ylabel="FoldX ΔΔG (kcal/mol)",
           ylim=(-3, 12))

    plt.savefig('aprs_impact.svg')

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
    parser.add_argument('foldx',
                        type=str,
                        help='List')
    args = parser.parse_args()
    return args.foldx


def main():
    foldx = arguments_parser()
    plot_apr_impact(foldx)


if __name__ == '__main__':
    main()
