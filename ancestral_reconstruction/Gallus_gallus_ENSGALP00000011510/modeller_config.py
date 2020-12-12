
import sys
from shutil import copyfile
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the automodel class

log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in

# directories for input atom files
env.io.atom_files_directory = ['.', '../']

a = automodel(env,
              alnfile='Gallus_gallus_ENSGALP00000011510.pir',      # Sequences alignment in .pir format
              knowns='template',  # Template structure
              sequence='Gallus_gallus_ENSGALP00000011510',  # Target sequence
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
copyfile(m["name"], 'best_model.pdb')
    