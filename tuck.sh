#!/bin/bash

#
# User will need to `source` this file from their .bashrc or .bash_profile 
#

function tuck () {
    last=`history 50`
    ~/.tuck/tuck.py "$@" "$last"
}

bold=$(tput bold)
normal=$(tput sgr0)
echo ">>> ${bold}tuck${normal} command loaded"
