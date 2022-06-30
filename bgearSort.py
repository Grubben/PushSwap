from ops import s, p, r, rr
from stackops import set_ascending, set_descending, giradaDetectorP

def bgearSort(a, b):
    if sorted(a) == a:
        return
    if giradaDetectorP(a):
        while giradaDetectorP(a):
            # set_ascending(a)
            r(a, "a") # rra might be more efficient in some cases
        return

    p(b, a, "b")
    while a:
        if giradaDetectorP(a):
            print("Turned")
            set_ascending(a)
            print("Unturned a")
        
        # if a is in order and everything is bigger than in b
        # then there is no need to pb
        # Just order b and pa!
        elif sorted(a) == a and min(a) > max(b):
            set_descending(b)
            while b:
                p(a, b, "a")
            print(a)
            print(b)
            return
        
        elif a[0] < min(b):
            set_descending(b)
            p(b, a, "b")
            r(b, "b")
            if giradaDetectorP(a):
                print("Turned")

        elif a[0] > max(b):
            set_descending(b)
            p(b, a, "b")

        else: # in the 
            #TODO: optmize this a lot!!!
            set_descending(b)
            while a[0] < b[0]:
                r(b, "b")
            p(b, a, "b")
# 1
        print(a)
        print(b)

    while b[0] != max(b):
        r(b, "b")
    print(a)
    print(b)

    while b:
        p(a, b, "a")

    print()
    #print(a)
    print(b)
