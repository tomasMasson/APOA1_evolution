#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


def plot_selection_type(hyphy_results):
    """
    Plot a rectangle with colors scheme based on the
    selection regimes affecting protein sequence
    inferred with HyPhy.
    """

    # Open Hyphy results and store them into a list
    with open(hyphy_results, "r") as fh:
        data = [line for line in fh]
    fel = [item.split(",")[0] for item in data]
    fubar = [item.split(",")[1] for item in data]
    meme = [item.split(",")[2] for item in data]
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
    plt.savefig("natural_selection_regimes.svg")


def main():
    """Command line argument parser."""

    parser = argparse.ArgumentParser(
            description="""
            Plot HyPhy natural selection classes
            """,
            usage="python3 plot_hyphy_selection.py <hyphy>"
            )
    parser.add_argument('hyphy', help='HyPhy residues selection regimes')
    args = parser.parse_args()
    plot_selection_type(args.hyphy)


if __name__ == "__main__":
    main()
