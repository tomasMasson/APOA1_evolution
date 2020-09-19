#!usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_rmsf_dataset(dataset):
    """
    """
    systems = ["WT", "G26R", "L60R", "delta107", "R173P"]

    palette = {
        'WT': '#6b8abe',
        'G26R': '#fdb462',
        'L60R': '#8dd3c7',
        'delta107': '#dd8452',
        'R173P': '#c2a5cf'
        }

    df = pd.read_csv(dataset)
    sns.set(style="ticks")
    fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(12,16))
    for ax, system in zip(axes, systems):
        data = df[df['System'] == system]
        sns.lineplot(
                x="Position",
                y="RMSF",
                data=data,
                ax=ax,
                color=palette[system]
                )
        ax.set(xlabel="Sequence Position", ylabel="RMSF (Å)")

    plt.tight_layout()
    plt.savefig("rmsf_figure.svg")


def main():
    "Command line argument parser"
    parser = argparse.ArgumentParser(description="Creates two barplots, one for the gyration radius and other for the APR1 SASA values",
            usage="plot_md-dataset <dataset>")
    parser.add_argument("dataset", help="CSV file with molecular dynamics-derived data")
    args = parser.parse_args()
    plot_rmsf_dataset(args.dataset)


if __name__ == "__main__":
    main()
