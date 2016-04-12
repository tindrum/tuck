#! /usr/bin/env python3

import sys, os
import argparse
import re
import urllib.request
import json

# Colors that can be used in terminal output
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


hist_len = len(sys.argv)
history_glob = sys.argv[hist_len - 1]
sys.argv[hist_len - 1] = "--foo"

print("The history_glob is: \n" + history_glob)

parser = argparse.ArgumentParser()

# parser.add_argument('--foo', nargs='?', const='c', default='d')
parser.add_argument('--foo', nargs='?', const='bar', default='baz')
parser.add_argument('--note', '-n', nargs=1)
parser.add_argument('--back', '-b', nargs=1)
# parser.add_argument('history', nargs='+')
# parser.add_argument('--hist_item', required=False)
parser.parse_args()
# parser.parse_args(arguments_glob)

# get the last command from the parse object
args = parser.parse_args()
# print("hist_item is: " + args.hist_item)
# print("last is: " + args.last)

if args.note:
    note = args.note[0]
else:
    note = "no note"
print("***** The note: " + str(note))
    
if args.back:
    back = args.back[0]
    print("***** The back number: " + str(back))
else:
    back = None
    print("***** We have to pick the penultimate item")

    
history_array = history_glob.splitlines()
history_dict = {}
history_pattern = re.compile(r"^\s*(\d+)\s*(.*)\s*")
print("history_array is a " + str(type(history_array)))
print("listing of history_array")
for item in history_array:
    # print(item + " is a " + str(type(item)))
    this_history = re.match(history_pattern, item)
    # print("match: " + this_history.group(1) + " : " + this_history.group(2))
    history_dict[this_history.group(1)] = this_history.group(2)

print("There are " + str(len(history_dict)) + " items in the dictionary")
    
if back:
    user_selected_item = history_dict[back]
    print("if user_selected_item: " + str(user_selected_item))
else:
    print("history_array[0]")
    print(history_array[0])
    this_history = re.match(history_pattern, history_array[0])
    user_selected_item = this_history.group(2)
    print("else user_selected_item: " + str(user_selected_item))

print("We think the thing you want is: " + user_selected_item)

# regex to strip off the history number
# command = re.match(r"\s*\d+\s+(\w.+)", argarray[0])
# print(" ")
# print("the actual command from the user")
# print(" ")
# print(command.group(1))
# cli_command = command.group(1)
user = "tindrum"

base_command = "tuck"
DATA=str.encode("cli_command=" + user_selected_item + "&user=" + user + "&note=" + note + "&base_command=" + base_command)

print(DATA)
# go to the url
try:
    req = urllib.request.Request(url='http://192.168.99.100:8000/tuck/cli/add/tindrum', data=DATA, method='POST')
    with urllib.request.urlopen(req) as f:
        print(f.read(300).decode('utf-8'))
except Exception as e:
    raise e
# print ("hello there")

# print (last)

