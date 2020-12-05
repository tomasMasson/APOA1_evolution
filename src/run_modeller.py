#!/usr/bin/env python3

import argparse
import os
import shutil
from pathlib import Path
from Bio import AlignIO


def create_modeller_alignment(template, target, alignment, folder):
    """
    Takes a fasta multiple sequence alignment
    and return a pir alignment with only the
    template and the target sequences.
    """

    # Open sequence alignment
    aln = AlignIO.read(alignment, "fasta")
    # Create PIR file inside a new folder for the target
    with open(f"{folder}/{target}.pir", "w") as fh:
        for seq in aln:
            # Write template sequence
            if template == seq.id:
                template_seq = f">P1;template\nstructureX:template:1:A:243:A::::\n{seq.seq[24:]}*\n"
                fh.write(template_seq)
        for seq in aln:
            # Write target sequence
            if target == seq.id:
                target_seq = f">P1;{seq.id}\nsequence:{target}::::::::\n{seq.seq}*\n"
                fh.write(target_seq)


def create_modeller_config(target, folder):
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
    config_file = f"{folder}/modeller_config.py"
    with open(config_file, "w") as fh:
        fh.write(config)


def main():
    """Command line argument parser"""

    parser = argparse.ArgumentParser()
    parser.add_argument("template",
                        help="template sequence to model")
    parser.add_argument("target",
                        help="target sequence to model")
    parser.add_argument("alignment",
                        help="sequence alignment between target and template")
    parser.add_argument("template_structure",
                        help="template PDB structure")
    args = parser.parse_args()
    template, target, align, template_structure = args.template, args.target, args.alignment, args.template_structure
    # Create a separate path for each modelling
    target_folder = Path.cwd() / "ancestral_reconstruction" / target
    # Remove folder from previous runs
    if Path.exists(target_folder):
        for file in target_folder.iterdir():
            Path.unlink(file)
        Path.rmdir(target_folder)
    # Make a new folder for each target
    Path.mkdir(target_folder)
    # Create PIR alignment
    create_modeller_alignment(template, target, align, target_folder)
    # Create Modeller configuration file
    create_modeller_config(target, target_folder)
    # Copy template structure
    shutil.copyfile(template_structure, target_folder / "template.pdb")
    # Run Modeller
    os.chdir(target_folder)
    command = "python modeller_config.py"
    os.system(command)


if __name__ == "__main__":
    main()
