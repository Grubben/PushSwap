#!/usr/bin/env python3

import sys
#from algo import *
from bgearSort import bgearSort


# args = [int(i) for i in sys.argv[1:]]

#algoSort()
count = bgearSort([int(i) for i in sys.argv[1:]], [])

# print()
print("Number of moves: ", count)