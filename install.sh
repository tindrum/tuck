#!/bin/bash

mkdir -p ~/.tuck
# Copy your files to ~/.tuck
cp tuck.sh ~/.tuck
cp tuck.py ~/.tuck
cp .tuck_config ~/.tuck
cp requirements.txt ~/.tuck

pyvenv ~/.tuck/.venv
source ~/.tuck/.venv/bin/activate
pip install -r ~/.tuck/requirements.txt

# Do something to update the PATH variable in ~/.bashrc, or
# just print out info to user:
echo "Please source ~/.tuck.sh in your bash startup script."
echo "On Mac, you can add this code to your .bash_profile file"
echo "to source it every time you open a terminal app:"
echo " "
echo "if [ -f ~/.tuck/tuck.sh ]; then"
echo "    source ~/.tuck/tuck.sh"
echo "fi"
echo " "
echo "On Linux, it should go in the .bashrc file."
echo " "
echo "After you source the file,"
echo "you may need to quit and restart your terminal app."
echo " "
echo "When you see '>>> tuck command loaded' in your terminal,"
echo "run 'tuck --configure' to set your username and secret word."
echo "*** NOTICE ***"
echo "This is a student project. Security is non-existent."
echo "In particular, 50 lines of your history are sent via INSECURE http"
echo "to the web server every time you tuck a command."
echo "If you have run commands with ssh keys or other sensitive info,"
echo "this info will be available to any 'man in the middle'"
echo "**************"
