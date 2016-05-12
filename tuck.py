#! /usr/bin/env python3

import sys, os
import argparse
import re
import urllib.request
import configparser

# read config file settings
config = configparser.ConfigParser()
config.read('~/.tuck/.tuck_config')
user = config['TUCK']['Username']
site_url = config['TUCK']['Server']
echo_level = config.getint('TUCK', 'EchoLevel', fallback=2)
secret = config.get('TUCK', 'security_string', fallback="secret")


# set up REST endpoints for commands
tuck_cli_action = "/tuck/cli_add/"
tuck_search_action = "/everlist/cleverlist/"

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

    
# this and the -foo flag are a kludge 
# to accept all params from parent bash script
hist_len = len(sys.argv)
history_glob = sys.argv[hist_len - 1]
sys.argv[hist_len - 1] = "--foo"


parser = argparse.ArgumentParser()

# If you want to change the single-character flags, 
# just don't change the word ones. 
parser.add_argument('--foo', action="store_true")
parser.add_argument('--note', '-n', nargs=1)
parser.add_argument('--back', '-b', nargs=1)
parser.add_argument('--suite', '-s', nargs=1)
parser.add_argument('--find', '-f', nargs='+')
parser.add_argument('--configure', action="store_true")

args = parser.parse_args()


if args.configure:
    print('Set your username and secret code here')
    newUserName = input("Please enter your username: ")
    newSecretWord = input("Please enter your secret word: ")
    config['TUCK']['Username'] = newUserName
    config['TUCK']['security_string'] = newSecretWord
    print("Make sure you have set the same secret word at " + site_url + "/users/~update/")
    f = open('/Users/tindrum/bin/tucklist/.tuck_config', mode='w')
    if f:
        config.write(f)
    else:
        print("File didn't open. You can always edit .tuck_config yourself.")
    
    exit
    
# concatenate the whole url that will be used
user_url = site_url + tuck_cli_action + user
search_url = site_url + tuck_search_action + user
# Data itself is in POST data

if args.find:
    print(args.find)
    find_args = ' '.join(args.find)
    
    # build POST data
    DATA=str.encode("user=" + user + "&find=" + find_args + "&secret=" + secret)

    # go to the url
    try:
        req = urllib.request.Request(url=search_url, data=DATA, method='POST', headers={'User-Agent':"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"})
        with urllib.request.urlopen(req) as f:
            print(f.read(3000).decode('utf-8'))
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
        if ( this_history ):
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
    
    if echo_level:
        print(color.GREEN + "*******  tucking " + color.BOLD + color.PURPLE + user_selected_item + color.END)
        if note != "":
            print(color.GREEN + "**     with note "  + color.BOLD + color.DARKCYAN + ((note[0:35] + " ...") if len(note) > 35 else note) + color.END)
        else:
            print(color.GREEN + "**     with no note ")
        print(color.GREEN + "** command suite " + color.BOLD + color.DARKCYAN + command_suite + color.END)

    # build POST data
    DATA=str.encode("cli_command=" + user_selected_item + "&user=" + user + "&note=" + note + "&base_command=" + command_suite + "&secret=" + secret)

    # go to the url
    try:
        req = urllib.request.Request(url=user_url, data=DATA, method='POST', headers={'User-Agent':"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"})
        with urllib.request.urlopen(req) as f:
            print(f.read(300).decode('utf-8'))
    except Exception as e:
        print("something musta happened to it, man.")
        # TODO: better error handling
        # Perhaps tucking should be written to a yaml file in the user's tuck dir,
        # and when the exception does not occur, 
        # the contents of this file are tucked at that time.
        raise e

