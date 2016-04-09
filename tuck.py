#! /usr/bin/env python3

import sys, os
import argparse
import re
import urllib.request


# last = (os.environ['TUCK_LAST'])

parser = argparse.ArgumentParser()
parser.add_argument("last", help="last commands issued")
parser.parse_args()

# get the last command from the parse object
args = parser.parse_args()
print(args.last)
print(type(args))
print(vars(args))
argarray = vars(args).get('last').splitlines()
print(argarray)
print(argarray[0])

# regex to strip off the history number
command = re.match(r"\s*\d+\s+(\w.+)", argarray[0])
print("the actual command from the user")
print(command.group(1))


# go to the url
try:
    with urllib.request.urlopen("http://192.168.99.100:8000/tuck/cli/add/tindrum") as f:
        print(f.read(300).decode('utf-8'))
except Exception as e:
    raise e
# print ("hello there")

# print (last)

