stacka = []
stackb = []

a = stacka
b = stackb

def s(stack):
    if stack and stack[0] and stack[1]:
        tmp = stack[0]
        stack[0] = stack[1]
        stack[1] = tmp

def sa():
    print("sa")
    s(a)

def sb():
    print("sb")
    s(b)

def ss():
    sa()
    sb()


def p(stack1, stack2):
    if stack2:
        stack1.insert(0, stack2[0])
        stack2.pop(0)

def pa():
    print("pa")
    p(a, b)

def pb():
    print("pb")
    p(b, a)


def r(stack):
    if stack:
        tmp = stack.pop(0)
        stack.append(tmp)
        
def ra():
    print("ra")
    r(a)

def rb():
    print("rb")
    r(b)

def rr():
    ra()
    rb()


def rr(stack):
    if stack:
        tmp = stack.pop()
        stack.insert(0, tmp)

def rra():
    print("rra")
    rr(a)

def rrb():
    print("rrb")
    rr(b)

def rrr():
    rra()
    rrb()
