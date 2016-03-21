#!/bin/bash
echo "in shell shim"
history -a
history -w

env TUCK_HISTORY=$(history) env TUCK_LAST=$(history 2) /Users/tindrum/.local/bin/tuck "$@"