#! /usr/bin/env python3
from random import choice, randint
import argparse

# Parse commandline arguments
parser = argparse.ArgumentParser(description="Generate passwords in the style of XKCD 936")
parser.add_argument("-w",  "--words", type=int, help="Number of words per password. Default 4.", default=4)
parser.add_argument("-p", "--passwords", type=int, help="Number of passwords to generate. Default 10", default=10)
args = parser.parse_args()

with open('eff_large_wordlist.txt') as wordfile:
    wL = [line.split()[1] for line in wordfile]

for i in range(args.passwords):
    print(("{}-"*args.words+"{:03}").format(*[choice(wL) for x in range(args.words)], randint(0,1000)))
    
