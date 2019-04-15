#! /usr/bin/env python3
from random import choice, randint
import argparse

# Parse commandline arguments
parser = argparse.ArgumentParser(description="Generate passwords in the style of XKCD 936")
parser.add_argument("-w",  "--words", type=int, help="Number of words per password. Default 4.", default=4)
parser.add_argument("-p", "--passwords", type=int, help="Number of passwords to generate. Default 10", default=10)
parser.add_argument("-s", "--separator", type=str, help="Character(s) to separate words with. Default '-'", default='-')
parser.add_argument("-a", "--append-numbers", 
    help="If given, a three digit number is appended to the end of each password", action="store_true")
args = parser.parse_args()

with open('eff_large_wordlist.txt') as wordfile:
    
    wL = [line.split()[1] for line in wordfile]

for i in range(args.passwords):
    if args.append_numbers:
        print(("{}"*args.words+"{:03}").format(*[choice(wL) + args.separator for x in range(args.words)], randint(0,1000)))
    else:  
         print(("{}"*(args.words-1)+"{}").format(*[choice(wL) + args.separator for x in range(args.words-1)], choice(wL)))
        
