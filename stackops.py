# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 13:57:12 2022

@author: fc53519
"""

from ops import s, p, r, rr

def set_ascending(stack, verbChar=""):
    """[1, 2, 3]"""
    moves = 0
    #TODO: use rr if more efficient
    if stack.index(max(stack)) > len(stack) // 2:
        while stack[0] != min(stack):
            rr(stack, verbChar)
            moves += 1

    else:
        while stack[0] != min(stack):
            r(stack, verbChar)
            moves += 1
    return moves


def set_descending(stack, verbChar=""):
    """[3, 2, 1]"""
    moves = 0
    #TODO: use rr if more efficient
    if stack.index(max(stack)) > len(stack) // 2:
        while stack[0] != max(stack):
            rr(stack, verbChar)
            moves += 1
    else:
        while stack[0] != max(stack):
            r(stack, verbChar)
            moves += 1
    return moves


def drain(giver, receiver, verbChar=""):
    """Drains all nums in giver to receiver with p"""
    moves = 0
    moves += set_descending(giver)
    while giver:
        p(receiver, giver, verbChar)
        moves += 1
    print(receiver)
    print(giver)
    return moves

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