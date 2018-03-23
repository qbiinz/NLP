These scripts attempt to correct spelling errors based on various N-gram model variants

Training and testing will be on a misspelling tagged corpus by David Holbrook

Run:

Sanity check

py -2 EditModel.py

This script should run each edit for minimum distance and return 100% overlap with 0 missing edits and 0 extra edits

Performance

py -2 SpellCorecct.py

make sure ./data/ is the current working directory

This script verifies the performance of each model runs through a training and test sets located in ./data

no need for input arguments
