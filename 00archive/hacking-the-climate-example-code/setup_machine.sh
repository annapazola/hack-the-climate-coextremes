#!/bin/bash

#Add a symbolic link for the data directory
ln -s /shared/groups/jrole001/geog0121/UKCP18 $HOME/UKCP18

# Discover the prebuilt environments
conda config --add envs_dirs /shared/groups/jrole001/geog0121/envs

# Load the hackathon environment
# conda activate jupyter_japsy

# Add the hackathon environment to your main screen
# python -m ipykernel install --name=jupyter_japsy  --display-name 'hackathon' --user
