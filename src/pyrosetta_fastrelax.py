#!/usr/bin/env python3

import argparse
from pyrosetta import *

def fastrelax_refinement(pdb):
    """
    Uses the Fast Relax protocol from PyRosetta
    to refine a PDB file.

    Output structure is saved to <pdb>_relaxed.pdb.
    """

    # Initialize PyRosetta sessions
    init()
    # Get score function
    sfxn = get_score_function()
    # Create a Pose instance from the input PDB file
    pose = pose_from_pdb(pdb)
    # Create a FastRelax instance
    relax = pyrosetta.rosetta.protocols.relax.FastRelax()
    relax.set_scorefxn(sfxn)
    relax.apply(pose)
    # Save relaxed structure to a new PDB file
    outfile = f"{pdb.split('.')[0]}_relaxed.pdb"
    pose.dump_pdb(outfile)


def main():
    """Command line argument parser"""

    parser = argparse.ArgumentParser()
    parser.add_argument("pdb",
                        help="PDB file to refine")
    args = parser.parse_args()
    fastrelax_refinement(args.pdb)


if __name__ == "__main__":
    main()
