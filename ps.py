#!/usr/bin/env python3

import sys
#from algo import *
from bgearSort import bgearSort


args = [int(i) for i in sys.argv[1:]]

args.extend([2, 3, 1, 5, 6, 4])
#algoSort(), 
count = bgearSort(args, [])

# print()
print("Number of moves: ", count)