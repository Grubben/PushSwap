from ops import *

def sorted(list):
    i = len(list) - 1 # last index of list
    while i:
        if list[i - 1] > list[i]:
            return False
        i -= 1
    return True


def algoSort():
    while not sorted(a):
        while a[0] > a[-1]:
            ra()

        if a[0] > a[1]:
            sa()
            continue

        while len(a) > 1 and a[0] < a[1]:
            pb()

    while b:
        pa()
    if not sorted(a):
        return algoSort()
    
    # print("Sorted!")



# a.extend([2,1,3,6,5,8])

# algoSort()
