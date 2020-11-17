#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_aprs_scores(df):
    """
    Creates two graphs:

    - One showing the score distribution for each aggregation
      prone region (APR) as boxplot and includes the individual
      data points as stripplot.

    - The other displays a barplot with the conservation values
      for each APR.
    """

    # Convert input to a pd DataFrame
    df = pd.read_csv(df)
    # Set APRs name to uppercase
    df.APR = df.APR.str.upper()
    # Normalize APR score to residue score
    df.Aggregation_score = df.Aggregation_score / 8

    # Create a new DataFrame to store the conservation value for each APR.
    # Initialize it with the number of sequences analyzed
    df_counts = df.groupby("APR").count()
    # Fix column name
    df_counts.columns = ["Sequences"]
    # Filter APRs with an average tango score of at least 5
    # and store them into another column
    df_counts["APRs"] = df[df.Aggregation_score >= 5].groupby("APR").count()
    # Fill NaN values
    df_counts = df_counts.fillna(0)
    # Compute the conservation of APRs relative to total number of sequences
    df_counts["Conservation"] = df_counts.APRs / df_counts.Sequences * 100

    # Create a figure object
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Plot APRs scores distribution
    sns.boxplot(x="Aggregation_score",
                y="APR",
                data=df,
                whis=[0, 100],
                palette="vlag",
                ax=ax1)

    # Plot APRs scores data points
    sns.stripplot(x="Aggregation_score",
                  y="APR",
                  data=df,
                  size=4,
                  color=".3",
                  linewidth=0,
                  alpha=0.5,
                  ax=ax1)

    # Set axis labels
    ax1.set(xlabel="TANGO average score per residue",
            ylabel="")

    # Plot APR conservation fractions
    sns.barplot(x="Conservation",
                y=df_counts.index,
                linewidth=1,
                edgecolor=".3",
                palette="vlag",
                data=df_counts,
                ax=ax2)

    # Set axis labels
    ax2.set(xlabel="% APR retained",
            ylabel="")

    # Save figure
    plt.savefig("aprs_conservation.svg")

    return f


def main():
    """Command line argument parser."""

    parser = argparse.ArgumentParser(
            description="""
            Plot APRs scores and conservation.
            """,
            usage="python3 plot_aprs_conservation.py <sequences>"
            )
    parser.add_argument('scores', help='APRs scores file')
    args = parser.parse_args()
    plot_aprs_scores(args.scores)


if __name__ == "__main__":
    main()
