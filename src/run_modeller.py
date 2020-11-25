#!/usr/bin/env python3

import argparse
import os
from pathlib import Path
from Bio import AlignIO


def create_modeller_alignment(target, alignment):
    """
    Takes a fasta multiple sequence alignment
    and return a pir alignment with only the
    template and the target sequences.
    """

    # Open sequence alignment
    aln = AlignIO.read(alignment, "fasta")
    # Create PIR file inside a new folder for the target
    with open(f"{target}/{target}.pir", "w") as fh:
        for seq in aln:
            # Write template sequence
            if seq.id == "template":
                template_seq = f">P1;{seq.id}\nstructureX:template:1:A:243:A::::\n{seq.seq}*\n"
                fh.write(template_seq)
            # Write target sequence
            if seq.id == target:
                target_seq = f">P1;{seq.id}\nsequence:{target}::::::::\n{seq.seq}*"
                fh.write(target_seq)


def create_modeller_config(target):
    """
    Creates a modeller configuration file.
    """

    # Configuration file
    config = f"""
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the automodel class

log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in

# directories for input atom files
env.io.atom_files_directory = ['.', '../']

a = automodel(env,
              alnfile='{target}.pir',      # Sequences alignment in .pir format
              knowns='template',  # Template structure
              sequence='{target}',  # Target sequence
              assess_methods=(assess.DOPE, assess.DOPEHR))  # Evaluation methods
a.starting_model = 1    # index of the first model
a.ending_model = 4      # index of the last model
a.make()                # Run comparative modeling
    """
    # Write config to file inside a new folder for the target
    config_file = f"{target}/modeller_config.py"
    with open(config_file, "w") as fh:
        fh.write(config)


def main():
    """Command line argument parser"""

    parser = argparse.ArgumentParser()
    parser.add_argument("target",
                        help="target sequence to model")
    parser.add_argument("alignment",
                        help="sequence alignment between target and template")
    args = parser.parse_args()
    target = args.target
    alignment = args.alignment
    # Make a new folder for each target
    target_folder = Path.cwd() / target
    Path.mkdir(target_folder)
    # Create PIR alignment
    create_modeller_alignment(target, alignment)
    # Create Modeller configuration file
    create_modeller_config(target)
    # Run Modeller
    os.chdir(target_folder)
    command = "python modeller_config.py"
    os.system(command)


if __name__ == "__main__":
    main()
