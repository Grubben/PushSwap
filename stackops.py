# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 13:57:12 2022

@author: fc53519
"""

from ops import s, p, r, rr

def set_ascending(stack):
    """[1, 2, 3]"""
    #TODO: use rr if more efficient
    while stack[0] !=  min(stack):
        r(stack)
        print("r")
        

def set_descending(stack, verbChar=""):
    """[3, 2, 1]"""
    #TODO: use rr if more efficient
    if stack.index(max(stack)) > len(stack) // 2:
        while stack[0] != max(stack):
            rr(stack, verbChar)
    else:
        while stack[0] != max(stack):
            r(stack, verbChar)


def giradaDetectorP(stack):
    """Returns whether the stack is girada or not"""

    if len(stack) < 2:
        return False
    exceptions = 0;
    if stack[0] < stack[-1]:
        return False
    i = 0;
    while ( i < len(stack) - 1):
        if stack[i] > stack[i + 1]:
            exceptions += 1;
            if exceptions > 1:
                return False
        i += 1;
    return True


# def set_orderb_for(newnum):
#     # Can be a LOT more optimized
#     set_ascending(stackb)
#     while newnum > stackb[0]:
#         rb()
#     pb()
