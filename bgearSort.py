from ops import *

def smallest(stack):
    return min(stack)

def biggest(stack):
    return max(stack)

def set_ascending(stack):
    stack.sort()

def set_descending(stack):
    stack.sort(reverse=True)

def set_orderb_for(newnum):
    # Can be a LOT more optimized
    set_ascending(stackb)
    while newnum > stackb[0]:
        rb()
    pb()


def in_order(stack):
    return sorted(stack) == stack or sorted(stack, reverse=True) == stack

def bgearSort():
    pb()
    while not in_order(a):
        if a[0] < smallest(b):
            set_ascending(b)
            pb()
        elif a[0] > biggest(b):
            set_descending(b)
            pb()
        else: # in the midst
            set_orderb_for(a[0])
            pb()
        print(stacka)
        print(stackb)

    while a != sorted(a): ## if descending
        # TODO: could be rra. Hv to make a way to get the best option
        ra()

    while b:
        pa()
