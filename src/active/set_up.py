import os
from pathlib import Path

#Set up project directory structure
rootdir = os.path.dirname((os.path.dirname(os.getcwd())))
datdir = Path(rootdir, "data")
resdir = Path(rootdir, "results")
srcdir = Path(rootdir, 'src')