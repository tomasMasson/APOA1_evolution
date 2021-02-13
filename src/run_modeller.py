#!/usr/bin/env python3

import argparse
import os
from shutil import copyfile
from pathlib import Path
from Bio import AlignIO


def get_targets(alignment):
    """
    Extract the sequence identifiers from a fasta alignment
    """

    # Read sequence alignment
    seqs = AlignIO.read(alignment, "fasta")
    # Extract sequences identifiers (will be used as targets for modelling)
    targets = [seq.id for seq in seqs]

    return targets


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
                template_seq = f">P1;template\nstructureX:template:1:A:243:A::::\n{seq.seq}*\n"
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
import sys
from shutil import copyfile
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
a.ending_model = 10      # index of the last model
a.make()                # Run comparative modeling

# Get a list of all successfully built models from a.outputs
ok_models = [x for x in a.outputs if x['failure'] is None]

# Rank the models by DOPE score
key = 'DOPE score'
if sys.version_info[:2] == (2,3):
    # Python 2.3's sort doesn't have a 'key' argument
    ok_models.sort(lambda a,b: cmp(a[key], b[key]))
else:
    ok_models.sort(key=lambda a: a[key])

# Get top model
m = ok_models[0]
# Copy model to a new file
copyfile(m["name"], '{target}_best_model.pdb')
    """

    # Set config file inside a specific modelling folder
    config_file = f"{folder}/{target}_modeller_config.py"
    # Write config file
    with open(config_file, "w") as fh:
        fh.write(config)


def run_modeller(template, target, align, template_structure):
    """
    Wrapper function to run modeller
    """

    # Set the base path
    base_path = Path.cwd()
    # Create a separate path for modelling results
    target_folder = base_path /"ancestral_reconstruction" 
    # Create a PIR alignment
    create_modeller_alignment(template, target, align, target_folder)
    # Create Modeller configuration file
    create_modeller_config(target, target_folder)
    # Copy template structure
    copyfile(template_structure, target_folder / "template.pdb")
    # Move to the modelling folder
    os.chdir(target_folder)
    # Set the modeller command
    command = f"python {target}_modeller_config.py"
    # Run modeller
    os.system(command)
    # Return to the base path
    os.chdir(base_path)


def main():
    """Command line argument parser"""

    parser = argparse.ArgumentParser()
    parser.add_argument("template",
                        help="template sequence to model")
    parser.add_argument("alignment",
                        help="sequence alignment between target and template")
    parser.add_argument("template_structure",
                        help="template PDB structure")
    args = parser.parse_args()
    template, align, template_structure = args.template, args.alignment, args.template_structure

    # Get the sequences ids
    targets = get_targets(align)

    # Run Modeller for each target sequence
    for target in targets:
        run_modeller(template, target, align, template_structure)


if __name__ == "__main__":
    main()
