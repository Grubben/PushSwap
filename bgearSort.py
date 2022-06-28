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

def giradaDetectorP(stack):
    """Returns wether the stack is girada or not"""

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
            ra() # rra might be more efficient in some cases
        return

    pb()
    while a:
        if a[0] < smallest(b):
            #set_descending(b) # rb
            pb()
            rb()
            if giradaDetectorP(a):
                print("Turned")

        elif a[0] > biggest(b):
            #set_descending(b)
            pb()
            if giradaDetectorP(a):
                print("Turned")

        else: # in the midst
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
