#! /usr/bin/env python
from random import choice, randint
import sys

try:
    l = int(sys.argv[1])
except:
    l = 4
try: 
    n = int(sys.argv[2])
except:
    n = 10

with open('eff_large_wordlist.txt') as wordfile:
    wL = [line.split()[1] for line in wordfile]

for i in range(n):
    print(("{}-"*l+"{:03}").format(*[choice(wL) for x in range(l)], randint(0,1000)))
    
