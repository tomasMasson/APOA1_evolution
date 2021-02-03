#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from Bio import AlignIO


def filter_gapped_positions(df, alignment):
    '''
    Filters a Dataframe to retain only the rows
    corresponding to the non-gap characters on
    the Human sequence.
    '''

    # Load sequence alignment
    algn = AlignIO.read(alignment, 'fasta')
    # Iterate over each sequence
    for sequence in algn:
        # For the Human sequence
        if sequence.id == "Homo_sapiens_ENSP00000364472":
            # Store the position of the gaps
            gaps = [index for index, position in enumerate(sequence.seq)
                    if position == "-"]
    # Filter the dataframe rows using the gap positions
    df = df.drop(df.index[gaps])

    return df


def plot_aprs_scores(aggregation, entropy, alignment):
    """
    Creates two graphs:

    - Boxplot showing the score distribution for each aggregation
      prone region (APR), including the individual data points as
      stripplot.

    - Boxplot displaying the entropy values for each APR.

    """

    # Convert aggregation input to a pd DataFrame
    agg_df = pd.read_csv(aggregation, names=["Specie", "Aggregation_score", "Class"])
    agg_df = agg_df.drop(columns=["Specie"])
    # Normalize APR score to residue score
    agg_df.Aggregation_score = agg_df.Aggregation_score / 8

    # Convert entropy input to a pd DataFrame
    ent_df = pd.read_csv(entropy, names=["Entropy"])
    # Filter out the gap positions
    ent_df = filter_gapped_positions(ent_df, alignment)
    # Reset index values
    ent_df = ent_df.reset_index(drop=True)
    # Add APR/non-APR labels
    ent_df["Class"] = "non-APR"
    ent_df.loc[37:43, "Class"] = "APR1"
    ent_df.loc[76:82, "Class"] = "APR2"
    ent_df.loc[90:96, "Class"] = "APR3"
    ent_df.loc[250:256, "Class"] = "APR4"
    # Drop non-apr data
    ent_df = ent_df[ent_df.Class != "non-APR"]

    # Create a new DataFrame to store the conservation value for each APR.
    # Initialize it with the number of sequences analyzed
    counts = agg_df.groupby("Class").count()
    # Fix column name
    counts.columns = ["Sequences"]
    # Filter APRs with an average tango score of at least 5
    # and store them into another column
    counts["Class"] = agg_df[agg_df.Aggregation_score >= 5].groupby("Class").count()
    # Fill NaN values
    counts = counts.fillna(0)
    # Compute the conservation of APRs relative to total number of sequences
    counts["Conservation"] = counts.Class / counts.Sequences * 100

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
    parser.add_argument('alignment', help='Protein alignment used to remove gapped positions')
    # Parse command line arguments
    args = parser.parse_args()
    agg_scores, entropies, alignment = args.agg_scores, args.entropies, args.alignment
    plot_aprs_scores(agg_scores, entropies, alignment)


if __name__ == "__main__":
    main()
