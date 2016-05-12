#!/bin/bash
​
mkdir -p ~/.tuck
# Copy your files to ~/.tuck
cp tuck.sh ~/.tuck
cp tuck.py ~/.tuck
cp .tuck_config ~/.tuck

pyvenv ~/.tuck/.venv
source ~/.tuck/.venv/bin/activate
pip install ~/.tuck/requirements.txt
​
# Do something to update the PATH variable in ~/.bashrc, or
# just print out info to user:
echo "Please add ~/.tuck/bin to your PATH"
echo "export PATH=$PATH:~/.tuck/bin"
​
# Put all your scripts there...
