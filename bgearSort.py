from ops import s, p, r, rr
from stackops import turnedP, is_ascendingP, swap_at, switchedP, prepTop, set_ascending, set_descending, drain


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

    if switchedP(a, is_ascendingP) > (-1):
            return swap_at(a, switchedP(a, is_ascendingP), "a")

    # chunks = len(a) // 2 + 1
    if len(a) < 50:
        chunks = 3
    elif len(a) <= 100:
        chunks = 7
    # if len(a) > 100:
    else:
        # chunks = len(a) // 100 * 7
        chunks = 10

    moves += prepTop(a, chunks)
    p(b, a, "b")
    moves += 1

    while a:
        if turnedP(a):
            print("Turned.")
            moves += set_ascending(a, 'a')
            print("Unturned a")
        
        if switchedP(a, is_ascendingP) > (-1):
           swap_at(a, switchedP(a, is_ascendingP), "a")
        
        # if a is in order and everything is bigger than in b
        # then there is no need to pb
        # Just order b and pa!
        if sorted(a) == a and min(a) > max(b):
            moves += drain(b, a, "a")
            print(a)
            # return moves
            break

        # Put smallest number on top by rev/rotating
        moves += prepTop(a, chunks)

        # Top of A is smaller than everything in B
        if a[0] < min(b):
            moves += set_descending(b, "b")
            p(b, a, "b")
            r(b, "b")
            moves += 2

        # Top of A is bigger than everythin in B
        elif a[0] > max(b):
            moves += set_descending(b, "b")
            p(b, a, "b")
            moves += 1

        # Top of A is not smaller nor bigger than numbers in B
        else:
            #TODO: optmize this a lot!!!
            moves += set_descending(b, "b")
            while a[0] < b[0]:
                r(b, "b")
                moves += 1
            p(b, a, "b")
            moves += 1

        # print(a)
        # print(b)


    while sorted(a) != a and b and b[0] != max(b):
        r(b, "b")
        moves += 1
    print(a)
    print(b)


    while b:
        p(a, b, "a")
        moves += 1

    print()
    print(a)
    # print(b)
    return moves
