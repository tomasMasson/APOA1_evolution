#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_md_dataset(dataset):
    """
    Creates two barplots, one for the gyration radius and other
    for the APR1 SASA values.
    """

    palette = {
        'WT': '#6b8abe',
        'G26R': '#ffffb3',
        'L60R': '#8dd3c7',
        'Δ107': '#dd8452',
        'R173P': '#c2a5cf'
        }

    df = pd.read_csv(dataset)
    fig, ax = plt.subplots(1, 1, figsize=(5, 4))
    sns.barplot(
            x="system",
            y="apr1_sasa",
            data=df,
            palette=palette,
            edgecolor=".2",
            ax=ax
            )
    ax.set(xlabel="System",
           ylabel="APR1 SASA (nm$2$)",
           ylim=(0, 1.6))
    plt.tight_layout()
    plt.savefig("md_figure.svg")


def main():
    "Command line argument parser"
    parser = argparse.ArgumentParser(description="Creates two barplots, one for the gyration radius and other for the APR1 SASA values",
            usage="plot_md-dataset <dataset>")
    parser.add_argument("dataset", help="CSV file with molecular dynamics-derived data")
    args = parser.parse_args()
    plot_md_dataset(args.dataset)


if __name__ == "__main__":
    main()
