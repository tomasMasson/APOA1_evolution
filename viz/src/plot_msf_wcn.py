#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


def read_df(data):
    """
    Plot the MSF and WCN into a boxplot.

    Data must come from the aggregated csv files
    created by the Snakefile pipeline.

    Residues are discriminated into two classes: APR and non-APR.
    """

    # Read input data
    df = pd.read_csv(data, sep="\t")
    # Compute the average MSF/WCN value for each position
    df["Average"] = df.mean(axis=1)
    # Add APR/non-APR labels
    df["Class"] = "non-APR"
    df.iloc[13:19, -1] = "APR"
    df.iloc[52:58, -1] = "APR"
    df.iloc[66:72, -1] = "APR"
    df.iloc[226:232, -1] = "APR"

    return df


def mannwhitneyu_test(df):
    """
    Performs a Wilcoxon-Mann U to asses if the
    difference between APR and non-APR are
    significant.
    """

    apr = list(df[df["Class"] == "APR"]["Average"])
    non_apr = list(df[df["Class"] == "non-APR"]["Average"])
    print(stats.mannwhitneyu(apr, non_apr))


def plot_msf_wcn(df_msf, df_wcn):

    # Set font size to 10
    matplotlib.rcParams.update({'font.size': 10})
    # Create a figure object
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 3))
    # Plot MSF values
    sns.boxplot(x="Average",
                y="Class",
                data=df_msf,
                whis=[0, 100],
                palette="vlag",
                ax=ax1)
    # Plot MSF data points
    sns.stripplot(x="Average",
                  y="Class",
                  data=df_msf,
                  size=4,
                  color=".3",
                  linewidth=0,
                  alpha=0.5,
                  ax=ax1)
    # Set Axis name
    ax1.set(xlabel="Mean Squared Fluctuation (MSF)",
            ylabel="")

    # Plot WCN values
    sns.boxplot(x="Average",
                y="Class",
                data=df_wcn,
                whis=[0, 100],
                palette="vlag",
                ax=ax2)
    # Plot MSF data points
    sns.stripplot(x="Average",
                  y="Class",
                  data=df_wcn,
                  size=4,
                  color=".3",
                  linewidth=0,
                  alpha=0.5,
                  ax=ax2)
    # Set Axis name
    ax2.set(xlabel="Weighted Contact Number (WCN)",
            ylabel="")

    # Save figure
    plt.savefig("aprs_flexibility.svg")

    return f


def plot_profiles(df_msf, df_wcn):

    # Compute mean value over 5 residues
    df_msf = df_msf.rolling(5).mean()
    df_wcn = df_wcn.rolling(5).mean()
    # Set font size to 10
    matplotlib.rcParams.update({'font.size': 10})
    # Create a figure object
    f, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
    # Plot MSF values distribution
    print(df_msf)
    for node in df_msf.columns[:8]:
        sns.lineplot(x=df_msf.index,
                     y=df_msf[node],
                     palette="vlag",
                     ax=ax1)
    # Set Axis name
    ax1.set(xlabel="Sequence Position",
            ylabel="Mean Squared Fluctuation (MSF)")

    # Plot WCN values distribution
    for node in df_wcn.columns[:8]:
        sns.lineplot(x=df_wcn.index,
                     y=df_wcn[node],
                     palette="vlag",
                     ax=ax2)
    # Set Axis name
    ax2.set(xlabel="Sequence Position",
            ylabel="Weighted Contact Number (WCN)")

    # Save figure
    plt.savefig("aprs_flexibility_profiles.svg")

    return f


def main():
    """Command line argument parser."""

    parser = argparse.ArgumentParser(
            description="""
            Plot APRs MSF and WCN profiles.
            """,
            usage="python3 plot_msf_wcn.py <msf> <wcn>"
            )
    parser.add_argument('msf', help='MSF csv file')
    parser.add_argument('wcn', help='WCN csv file')
    args = parser.parse_args()
    df_msf, df_wcn = read_df(args.msf), read_df(args.wcn)
    plot_msf_wcn(df_msf, df_wcn)
    # Close previous figure
    plt.close()
    plot_profiles(df_msf, df_wcn)
    # Calculate P value for MSF
    print("Mann Whitney U test for MSF")
    mannwhitneyu_test(df_msf)
    # Calculate P value for WCN
    print("Mann Whitney U test for WCN")
    mannwhitneyu_test(df_wcn)


if __name__ == "__main__":
    main()
