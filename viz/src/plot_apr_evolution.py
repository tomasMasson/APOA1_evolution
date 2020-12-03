#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


def plot_aprs_scores(aggregation, entropy):
    """
    Creates two graphs:

    - Boxplot showing the score distribution for each aggregation
      prone region (APR), including the individual data points as
      stripplot.

    - Boxplot displaying the entropy values for each APR.

    """

    # Convert aggregation input to a pd DataFrame
    agg_df = pd.read_csv(aggregation)
    # Convert entropy input to a pd DataFrame
    ent_df = pd.read_csv(entropy)
    # Drop non-apr data
    ent_df = ent_df[ent_df.Class != "Non-APR"]
    # Normalize APR score to residue score
    agg_df.Aggregation_score = agg_df.Aggregation_score / 8

    # Create a new DataFrame to store the conservation value for each APR.
    # Initialize it with the number of sequences analyzed
    counts = agg_df.groupby("APR").count()
    # Fix column name
    counts.columns = ["Sequences"]
    # Filter APRs with an average tango score of at least 5
    # and store them into another column
    counts["APR"] = agg_df[agg_df.Aggregation_score >= 5].groupby("APR").count()
    # Fill NaN values
    counts = counts.fillna(0)
    # Compute the conservation of APRs relative to total number of sequences
    counts["Conservation"] = counts.APR / counts.Sequences * 100

    # Set font size to 10
    matplotlib.rcParams.update({'font.size': 10})
    # Create a figure object
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3))

    # Plot APRs scores distribution
    sns.barplot(x="Conservation",
                y=["APR1", "APR2", "APR3", "APR4"],
                data=counts,
                linewidth=0.5,
                palette="vlag",
                ax=ax1)

    # Set axis labels
    ax1.set(xlabel="% Amyloid Sequences",
            ylabel="")

    # Plot Entropy values for each APR
    sns.boxplot(x="Entropy",
                y="Class",
                data=ent_df,
                whis=[0, 100],
                palette="vlag",
                ax=ax2)

    # Plot Entropy data points for each APR
    sns.stripplot(x="Entropy",
                  y="Class",
                  data=ent_df,
                  size=4,
                  color=".3",
                  linewidth=0,
                  alpha=0.5,
                  ax=ax2)
    # Set axis labels
    ax2.set(xlabel="Sequence Entropy (H)",
            ylabel="")

    # Save figure
    plt.savefig("aprs_conservation.svg")

    return f


def plot_selection_type(hyphy_results):
    """
    Plot a rectangle with colors scheme based on the
    selection regimes affecting protein sequence 
    inferred with HyPhy.
    """

    # Open Hyphy results and store them into a list
    with open(hyphy_results, "r") as fh:
        data = [line for line in fh]
    fel = [item.split()[0] for item in data]
    fubar = [item.split()[1] for item in data]
    meme = [item.split()[2] for item in data]
    # Create a new figure
    f, ax = plt.subplots(1, 1, figsize=(6, 4))
    # Set Axis limits
    ax.set_xlim([0, 250])
    ax.set_ylim([0, 100])
    # Remove Y axis
    ax.axes.get_yaxis().set_visible(False)
    # Set X axis label
    ax.set_xlabel("Sequence Position")
    # Hide all the spines except for the one of the bottom
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    # Plot FEL sites
    for index, sel in enumerate(fel):
        color = "#1f78b4"
        if "Diver" in sel:
            color = "#fdc086"
        elif "Neutral" in sel:
            color = "#a6cee3"
        rect = plt.Rectangle((index, 80), 1, 10, color=color)
        ax.add_artist(rect)
    ax.text(-30, 83, 'FEL')
    # Plot FUBAR sites
    for index, sel in enumerate(fubar):
        color = "#1f78b4"
        if "Diver" in sel:
            color = "#fdc086"
        elif "Neutral" in sel:
            color = "#a6cee3"
        rect = plt.Rectangle((index, 50), 1, 10, color=color)
        ax.add_artist(rect)
    ax.text(-30, 53, 'FUBAR')
    # Plot MEME sites
    for index, sel in enumerate(meme):
        color = "#1f78b4"
        if "Episodic" in sel:
            color = "#fdc086"
        rect = plt.Rectangle((index, 20), 1, 10, color=color)
        ax.add_artist(rect)
    ax.text(-30, 23, 'MEME')
    ax.vlines(14, 0, 90, colors='Black', linestyles='dashed', linewidth=0.8)
    ax.vlines(19, 0, 90, colors='Black', linestyles='dashed', linewidth=0.8)
    ax.vlines(53, 0, 90, colors='Black', linestyles='dashed', linewidth=0.8)
    ax.vlines(58, 0, 90, colors='Black', linestyles='dashed', linewidth=0.8)
    ax.vlines(67, 0, 90, colors='Black', linestyles='dashed', linewidth=0.8)
    ax.vlines(72, 0, 90, colors='Black', linestyles='dashed', linewidth=0.8)
    ax.vlines(227, 0, 90, colors='Black', linestyles='dashed', linewidth=0.8)
    ax.vlines(232, 0, 90, colors='Black', linestyles='dashed', linewidth=0.8)
    ax.add_artist(rect)
    # Show plot
    plt.savefig("selection_pressure.svg")


def main():
    """Command line argument parser."""

    parser = argparse.ArgumentParser(
            description="""
            Plot APRs scores and Entropy.
            """,
            usage="python3 plot_aprs_conservation.py <agg_scores> <entropies> <hyphy>"
            )
    parser.add_argument('agg_scores', help='APRs scores file')
    parser.add_argument('entropies', help='Residues entropy values')
    parser.add_argument('hyphy', help='HyPhy residues selection regimes')
    args = parser.parse_args()
    plot_aprs_scores(args.agg_scores, args.entropies)
    plot_selection_type(args.hyphy)


if __name__ == "__main__":
    main()
