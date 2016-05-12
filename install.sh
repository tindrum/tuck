#!/bin/bash

mkdir -p ~/.tuck
# Copy your files to ~/.tuck
cp tuck.sh ~/.tuck
cp tuck.py ~/.tuck
cp .tuck_config ~/.tuck
cp requirements.txt ~/.tuck

pyvenv ~/.tuck/.venv
source ~/.tuck/.venv/bin/activate
pip install ~/.tuck/requirements.txt

# Do something to update the PATH variable in ~/.bashrc, or
# just print out info to user:
echo "Please source ~/.tuck.sh in your bash startup script."
echo "On Mac, you can add this code to your .bash_profile file:"
echo " "
echo "if [ -f ~/.tuck/tuck.sh ]; then"
echo "    source ~/.tuck/tuck.sh"
echo "fi"
echo " "
echo "On Linux, it should go in the .bashrc file."
echo " "
echo "Then run 'tuck --configure' to set your username and secret word."
