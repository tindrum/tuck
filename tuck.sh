#!/bin/bash
# echo "in shell shim"
# someone says this will write temp history to .bash_history
# history -a
# http://unix.stackexchange.com/questions/145250/where-is-bashs-history-stored
# history -w

# history 2 | cat
# env TUCK_HISTORY=$(history) env TUCK_LAST=$(history 2) /Users/tindrum/.local/bin/tuck "$@"
# env TUCK_HISTORY=$(history) env TUCK_LAST=$(history 2) /Users/tindrum/Documents/Sp_2016_local/CS_462_local/TuckList/cli/tucklist/python-tucklist/tuck.py "$@"
echo "*** function tuck loading ***"
function tuck {
    # Get the last 2 history commands.
    # This will generate a string like this:
    # NNN command  NNN+1 tuck
    # Python will see a single argument, with 2 strings
    # separated by newline
    # It will use the first, since the 2nd will be 'tuck'
    last=`history 2`
    /Users/tindrum/Documents/Sp_2016_local/CS_462_local/TuckList/cli/tucklist/python-tucklist/tuck.py "$last $@"
}
echo "*** tuck loaded ***"