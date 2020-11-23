#!/usr/bin/env python3

import argparse
import numpy as np
from Bio import AlignIO


def shannon_entropy(array):
    """
    Takes a numpy array and returns its Shannon entropy
    """

    # Compute the probability associated with each element in the array
    p = [np.count_nonzero(array == i) / len(array) for i in set(array)]
    # Compute Entropy according to Shannon formulae
    h = float(- np.sum(p * np.log2(p)))

    return h


def msa_entropy_profile(msa):
    """
    Takes a fasta sequence alignment and returns its entropy profile
    """

    aln = AlignIO.read(msa, "fasta")
    aln_array = np.array([list(rec) for rec in aln])
    profile = [shannon_entropy(aln_array[:, i])
               for i in range(len(aln_array[0, :]))]

    return profile


def main():
    """Command line argument parser"""

    parser = argparse.ArgumentParser()
    parser.add_argument("alignment",
                        help="sequence alignment in fasta")
    args = parser.parse_args()
    profile = msa_entropy_profile(args.alignment)
    for entropy in profile:
        print(entropy)


if __name__ == "__main__":
    main()
