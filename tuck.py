#! /usr/bin/env python3

import sys, os
import argparse
import re


# last = (os.environ['TUCK_LAST'])

parser = argparse.ArgumentParser()
parser.add_argument("last", help="last commands issued")
parser.parse_args()

args = parser.parse_args()
print(args.last)


# print ("hello there")

# print (last)

