#!/usr/bin/env python3

import sys
from algo import *
from bgearSort import *


if sys.argv[1]:
    args = [int(i) for i in sys.argv[1:]]
    a.clear()
    a.extend(args)
    #algoSort()
    bgearSort()
    print(a)
else:
    print("No args given")