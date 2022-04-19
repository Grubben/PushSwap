stacka = []
stackb = []

a = stacka
b = stackb


def sa():
    print("sa")
    if (stacka and stacka[0] and stacka[1]):
        tmp = stacka[0]
        stacka[0] = stacka[1]
        stacka[1] = tmp

def sb():
    print("sb")
    if (stackb and stackb[0] and stackb[1]):
        tmp = stackb[0]
        stackb[0] = stackb[1]
        stackb[1] = tmp

def ss():
    sa()
    sb()


def pa():
    print("pa")
    if stackb:
        stacka.insert(0, stackb[0])
        stackb.pop(0)

def pb():
    print("pb")
    if stacka:
        stackb.insert(0, stacka[0])
        stacka.pop(0)

def ra():
    print("ra")
    if stacka:
        tmp = stacka.pop(0)
        stacka.append(tmp)

def rb():
    print("rb")
    if stackb:
        tmp = stackb.pop(0)
        stackb.append(tmp)

def rr():
    ra()
    rb()

def rra():
    print("rra")
    if stacka:
        tmp = stacka.pop()
        stacka.insert(0, tmp)

def rrb():
    print("rrb")
    if stackb:
        tmp = stackb.pop()
        stackb.insert(0, tmp)

def rrr():
    rra()
    rrb()
