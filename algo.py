from ops import *

def sorted(list):
    i = len(list) - 1 # last index of list
    while i:
        if list[i - 1] > list[i]:
            return False
        i -= 1
    return True


def algoSort():
    while a[0] > a[-1]:
        ra()

    if a[0] > a[1]:
        sa()
        return algoSort()

    while len(a) > 1 and a[0] < a[1]:
        pb()
    
    if sorted(a):
        while b:
            pa()
        return
    else:
        return algoSort()



a.extend([2,1,3,6,5,8])

algoSort()
