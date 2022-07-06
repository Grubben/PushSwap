from ops import s, p, r, rr
from stackops import set_ascending, set_descending, drain, turnedP

def bgearSort(a, b):
    moves = 0

    if sorted(a) == a:
        return 0
    if turnedP(a):
        while turnedP(a):
            # set_ascending(a)
            r(a, "a") # rra might be more efficient in some cases
            moves += 1
        return moves

    p(b, a, "b")
    moves += 1

    while a:
        if turnedP(a):
            print("Turned.")
            moves += set_ascending(a)
            print("Unturned a")
        
        # if a is in order and everything is bigger than in b
        # then there is no need to pb
        # Just order b and pa!
        elif sorted(a) == a and min(a) > max(b):
            moves += drain(b, a, "a")
            return moves

        elif a[0] < min(b):
            moves += set_descending(b)
            p(b, a, "b")
            r(b, "b")
            moves += 2

        elif a[0] > max(b):
            moves += set_descending(b)
            p(b, a, "b")
            moves += 1

        else: # in the 
            #TODO: optmize this a lot!!!
            moves += set_descending(b)
            while a[0] < b[0]:
                r(b, "b")
                moves += 1
            p(b, a, "b")
            moves += 1

        print(a)
        print(b)


    while b[0] != max(b):
        r(b, "b")
        moves += 1
    print(a)
    print(b)


    while b:
        p(a, b, "a")
        moves += 1

    print()
    #print(a)
    print(b)
    return moves
