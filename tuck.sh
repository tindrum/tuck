#!/bin/bash

#
# User will need to `source` this file from their .bashrc or .bash_profile 
#

# echo "in shell shim"
# someone says this will write temp history to .bash_history
# history -a
# http://unix.stackexchange.com/questions/145250/where-is-bashs-history-stored
# history -w

# history 2 | cat
# env TUCK_HISTORY=$(history) env TUCK_LAST=$(history 2) /Users/tindrum/.local/bin/tuck "$@"
# env TUCK_HISTORY=$(history) env TUCK_LAST=$(history 2) /Users/tindrum/Documents/Sp_2016_local/CS_462_local/TuckList/cli/tucklist/python-tucklist/tuck.py "$@"
# echo "*** function tuck loading ***"
function tuck () {
    if [ $# -gt 0 ]; then
        echo "Your command line contains $# arguments"
        echo "we need to see if the first one is -h"
        echo "and the third one could be a number or some word?"
    else
        last=`history 2`
        ~/bin/tucklist/tuck.py "$last $@"
        # echo "last command tucked"
    fi
}
bold=$(tput bold)
normal=$(tput sgr0)
echo ">>> ${bold}tuck${normal} command loaded"
