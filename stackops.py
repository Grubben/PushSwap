# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 13:57:12 2022

@author: fc53519
"""
import copy
from ops import *


def is_ascendingP(stack):
    return sorted(stack) == stack

def is_descendingP(stack):
    return sorted(stack, reverse=True) == stack

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

def turnedP(stack):
    """Returns whether the stack is Turned or not"""
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

def miniswitchedP(stack, verifierF):
    """Checks whether a single swap
        orders the stack in the order
        specified by verifierF
        eg: verifierF can be is_ascendingP"""
    s(stack)
    ordered = verifierF(stack)
    s(stack) # undoes the swap
    return ordered



def switchedP(stack, verifierF):
    """A switched stack is in the order specified by
        verifierF with a single swap"""
    if len(stack) < 2:
        return (-1)
    replica = copy.deepcopy(stack)
    index = 0
    rotates = 0
    while index < len(replica):
        rotates = index
        while rotates:
            r(replica)
            rotates -= 1

        s(replica)

        while rotates < index:
            rr(replica)
            rotates += 1

        if verifierF(replica):
            return index
        
        # Goes back to undo the swap
        while rotates:
            r(replica)
            rotates -= 1

        s(replica)

        while rotates < index:
            rr(replica)
            rotates += 1
        index += 1
    return (-1)
    
def swap_at(stack, index, verbChar=""):
    #TODO: Can be more optimized!!! rr might be better
    # than r and vice versa
    if not stack and not index:
        raise Exception()
    moves = 0
    rotates = index
    while rotates:
        moves += r(stack, verbChar)
        rotates -= 1
    moves += s(stack, verbChar)
    while rotates < index:
        moves += rr(stack, verbChar)
        rotates += 1
    # s(stack[index:]) in C
    return moves

# def set_orderb_for(newnum):
#     # Can be a LOT more optimized
#     set_ascending(stackb)
#     while newnum > stackb[0]:
#         rb()
#     pb()

def prepTop(stack, chunks=5):
    """Rotates the given stack to get the more efficient
        lower number to the top"""
    # No negative numbers!
    smallest = min(stack)
    biggest = max(stack)
    chunkSize = (biggest - smallest + chunks) // chunks

    lookChunk = 0
    while lookChunk < chunks:
        found = False
        topi = 0
        while topi < len(stack): 
            if (stack[topi] >= smallest + chunkSize * lookChunk and 
                stack[topi] < smallest + chunkSize * (lookChunk + 1)):
                found = True
                break
            topi += 1

        boti = len(stack) - 1
        while boti >= 0:
            if (stack[boti] >= smallest + chunkSize * lookChunk and 
                stack[boti] < smallest + chunkSize * (lookChunk + 1)):
                found = True
                break
            boti -= 1

        if found:
            boti = len(stack) - boti
            if topi <= boti:
                rotate(stack, topi, "?")
            else:
                revRotate(stack, boti, "?")
            return True

        lookChunk += 1
    # Shouldn't happen
    return False

if __name__ == "__main__":
    a = [75, 68, 100, 43, 23, 2, 98, 77]
    print(prepTop(a))
    print(a)