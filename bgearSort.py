from ops import *

def smallest(stack):
    return min(stack)

def biggest(stack):
    return max(stack)

def set_ascending(stack):
    """[1, 2, 3]"""
    stack.sort()

def set_descending(stack):
    """[3, 2, 1]"""
    stack.sort(reverse=True)

def set_orderb_for(newnum):
    # Can be a LOT more optimized
    set_ascending(stackb)
    while newnum > stackb[0]:
        rb()
    pb()


def bgearSort():
    pb()
    while a:
        if a[0] < smallest(b):
            set_ascending(b)
            pb()

        if a[0] > biggest(b):
            set_descending(b)
            pb()

        else: # in the midst
            while a[0] < b[0]:
                rb()
            pb()
        print(stacka)
        print(stackb)

    while b:
        pa()
