#! /usr/bin/env python3

import sys, os
import argparse
import re
import urllib.request
import json


# set up the url for the site
# TODO: change for production to tuck.magentabackpack.com
site_url = "http://192.168.99.100:8000"

# set up REST endpoints for commands
tuck_cli_action = "/tuck/cli_add/"
tuck_search_action = "/everlist/cleverlist/"

# TODO: create REST endpoint for searching

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


parser = argparse.ArgumentParser()

parser.add_argument('--foo', nargs='?', const='bar', default='baz')
parser.add_argument('--note', '-n', nargs=1)
parser.add_argument('--back', '-b', nargs=1)
parser.add_argument('--username', '-u', nargs=1)
parser.add_argument('--suite', '-s', nargs=1)
parser.add_argument('--find', '-f', nargs='+')
parser.parse_args()

args = parser.parse_args()

# TODO: read the user from a config file
user = "tindrum"

# fake a tuck from another user easily
# TODO: disable this from production code
if args.username:
    user_url = site_url + tuck_cli_action + args.username[0]
    user = args.username[0]
    print("****************************************")
    print("Using a different username for this one:")
    print(user)
    print("****************************************")
    

# concatenate the whole url that will be used
user_url = site_url + tuck_cli_action + user
search_url = site_url + tuck_search_action + user
# Data itself is in POST data




if args.find:
    print(args.find)
    find_args = ' '.join(args.find)
    
    # build POST data
    DATA=str.encode("user=" + user + "&find=" + find_args)

    # go to the url
    try:
        req = urllib.request.Request(url=search_url, data=DATA, method='POST')
        with urllib.request.urlopen(req) as f:
            print(f.read(300).decode('utf-8'))
    except Exception as e:
        print("search is busted.")
        # TODO: better error handling
        # Perhaps tucking should be written to a yaml file in the user's tuck dir,
        # and when the exception does not occur, 
        # the contents of this file are tucked at that time.
        raise e


if (args.back or args.note):
    # history number or note exists, assuming it's a tucking
    if args.note:
        note = args.note[0]
    else:
        note = "no note"
    
    if args.back:
        back = args.back[0]
    else:
        back = None

    
    history_array = history_glob.splitlines()
    history_dict = {}
    history_pattern = re.compile(r"^\s*(\d+)\s*(.*)\s*")

    for item in history_array:
        this_history = re.match(history_pattern, item)
        history_dict[this_history.group(1)] = this_history.group(2)

    if back:
        user_selected_item = history_dict[back]
    else:
        this_history = re.match(history_pattern, history_array[-2])
        user_selected_item = this_history.group(2)

    if args.suite:
        command_suite = args.suite[0]
    else:
        command_suite = user_selected_item.split(' ', 1)[0]
    
    print(color.GREEN + "*******  tucking " + color.BOLD + color.PURPLE + user_selected_item + color.END)
    if note != "":
        print(color.GREEN + "**     with note "  + color.BOLD + color.DARKCYAN + ((note[0:35] + " ...") if len(note) > 35 else note) + color.END)
    else:
        print(color.GREEN + "**     with no note ")
    print(color.GREEN + "** command suite " + color.BOLD + color.DARKCYAN + command_suite + color.END)

    # build POST data
    DATA=str.encode("cli_command=" + user_selected_item + "&user=" + user + "&note=" + note + "&base_command=" + command_suite)

    # go to the url
    try:
        req = urllib.request.Request(url=user_url, data=DATA, method='POST')
        with urllib.request.urlopen(req) as f:
            print(f.read(300).decode('utf-8'))
    except Exception as e:
        print("something musta happened to it, man.")
        # TODO: better error handling
        # Perhaps tucking should be written to a yaml file in the user's tuck dir,
        # and when the exception does not occur, 
        # the contents of this file are tucked at that time.
        raise e

