from ops import *

def smallest(stack):
    return min(stack)

def biggest(stack):
    return max(stack)

def set_ascending(stack):
    """[1, 2, 3]"""
    #TODO: use rr if more efficient
    while stack[0] !=  smallest(stack):
        r(stack)
        print("r")

def set_descending(stack, verbose=True):
    """[3, 2, 1]"""
    #TODO: use rr if more efficient
    if stack.index(biggest(stack)) > len(stack) // 2:
        while stack[0] != biggest(stack):
            rr(stack)
            if verbose:
                print("rr")
    else:
        while stack[0] != biggest(stack):
            r(stack)
            if verbose:
                print("r")

def set_orderb_for(newnum):
    # Can be a LOT more optimized
    set_ascending(stackb)
    while newnum > stackb[0]:
        rb()
    pb()

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

def bgearSort():
    if sorted(a) == a:
        return
    if giradaDetectorP(a):
        while giradaDetectorP(a):
            # set_ascending(a)
            ra() # rra might be more efficient in some cases
        return

    pb()
    while a:
        if giradaDetectorP(a):
            set_ascending(a)
            print("Unturned a")
        
        # if a is in order and everything is bigger than in b
        # then there is no need to pb
        # Just order b and pa!
        elif sorted(a) == a and smallest(a) > biggest(b):
            set_descending(b)
            while b:
                pa()
            print(stacka)
            print(stackb)
            return
        
        elif a[0] < smallest(b):
            set_descending(b)
            pb()
            rb()
            if giradaDetectorP(a):
                print("Turned")

        elif a[0] > biggest(b):
            set_descending(b)
            pb()
            if giradaDetectorP(a):
                print("Turned")

        else: # in the 
            #TODO: optmize this a lot!!!
            set_descending(b)
            while a[0] < b[0]:
                rb()
            pb()
            if giradaDetectorP(a):
                print("Turned")

        print(stacka)
        print(stackb)

    while b[0] != biggest(b):
        rb()
    print(stacka)
    print(stackb)

    while b:
        pa()

    print()
    #print(stacka)
    print(stackb)
