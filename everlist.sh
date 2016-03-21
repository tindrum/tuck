#!/bin/bash
echo "in shell shim"
# someone says this will write temp history to .bash_history
history -a
# http://unix.stackexchange.com/questions/145250/where-is-bashs-history-stored
history -w

env TUCK_HISTORY=$(history) env TUCK_LAST=$(history 2) /Users/tindrum/.local/bin/tuck "$@"