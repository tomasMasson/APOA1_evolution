#!/usr/bin/env python3

import argparse
import subprocess
from Bio import SeqIO


def create_TANGO_configuration(alignment, start, end):
    """
    Takes a fasta alignment and returns a list
    containing a TANGO configuration string
    for each sequence.
    """

    # Read sequences from a fasta alignment
    align = SeqIO.parse(alignment, "fasta")
    # Create a configuration list from sequences
    config = {seq.id: f"nt='N' ct='N' ph='7' te='310' io='0.1' seq='{seq.seq[start:end].rstrip()}'"
              for seq in align}
    return config


def run_tango(bin, configurations, output):
    """
    Runs a set of configurations stored
    in the variable <config>.

    The <bin> variable specifies which
    Tango binary is going to be used.
    """

    for key in configurations:
        command = f"{bin} " + configurations[key]
        # Run Tango for this configuraton and
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        # Decode result from binary to utf-8
        result_decoded = result.stdout.decode("utf-8")
        # Retain only succesful results
        if result_decoded.startswith("AGG"):
            print(f"{key},{result_decoded.split()[1]},{output}")


def main():
    """Command line argument parser"""

    parser = argparse.ArgumentParser()
    parser.add_argument("alignment",
                        help="Sequence alignment in fasta format")
    parser.add_argument("start", type=int,
                        help="Start position")
    parser.add_argument("end", type=int,
                        help="End position")
    parser.add_argument("bin",
                        help="TANGO binary")
    parser.add_argument("output",
                        help="Name assigned to predicted value")

    args = parser.parse_args()
    # Arguments unpacking
    align, start, end, bin, output = args.alignment, args.start, args.end, args.bin, args.output
    # Create configuration orders
    config = create_TANGO_configuration(align, start, end)
    # Run Tango
    run_tango(bin, config, output)


if __name__ == "__main__":
    main()
