args = "2 1 3 6 5 8"

intargs = [int(n) for n in args.split()]

stacka = []
stackb = []

a = stacka
b = stackb


def sa():
    if (stacka and stacka[0] and stacka[1]):
        tmp = stacka[0]
        stacka[0] = stacka[1]
        stacka[1] = tmp

def sb():
    if (stackb and stackb[0] and stackb[1]):
        tmp = stackb[0]
        stackb[0] = stackb[1]
        stackb[1] = tmp

def ss():
    sa()
    sb()


def pa():
    if stackb:
        stacka.insert(0, stackb[0])
        stackb.pop(0)

def pb():
    if stacka:
        stackb.insert(0, stacka[0])
        stacka.pop(0)

def ra():
    if stacka:
        tmp = stacka.pop(0)
        stacka.append(tmp)

def rb():
    if stackb:
        tmp = stackb.pop(0)
        stackb.append(tmp)

def rr():
    ra()
    rb()

def rra():
    if stacka:
        tmp = stacka.pop()
        stacka.insert(0, tmp)

def rrb():
    if stackb:
        tmp = stackb.pop()
        stackb.insert(0, tmp)

def rrr():
    rra()
    rrb()
