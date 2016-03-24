#! /usr/bin/env python3

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
parser.parse_args()

args = parser.parse_args()
print(args.echo)


# print ("hello there")

print (type(os.environ['TUCK_HISTORY']))
print (os.environ['TUCK_HISTORY'])

print (os.environ['TUCK_LAST'])