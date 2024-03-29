def s(stack, verbChar=""):
    """Swap the first 2 elements at the top of stack"""
    if stack and len(stack) > 1:
        tmp = stack[0]
        stack[0] = stack[1]
        stack[1] = tmp
        if verbChar:
            print("s" + verbChar)
        return 1
    return 0

# # def sa():
# #     print("sa")
# #     # s(a)

# def sb():
#     print("sb")
#     s(b)

# def ss():
#     sa()
#     sb()


def p(stack1, stack2, verbChar=""):
    """Take the first element at the top of b and put it at the top of a"""
    if stack2:
        stack1.insert(0, stack2[0])
        stack2.pop(0)
        if verbChar:
            print("p" + verbChar)
        return 1
    return 0

# def pa():
#     print("pa")
#     p(a, b)

# def pb():
#     print("pb")
#     p(b, a)


def r(stack, verbChar=""):
    """The first element becomes the last one"""
    if stack:
        tmp = stack.pop(0)
        stack.append(tmp)
        if verbChar:
            print("r" + verbChar)
        return 1
    return 0

def rotate(stack, howMany, verbChar=""):
    """Normal rotates the stack
        the amount specified"""
    q = howMany
    while howMany > 0:
        r(stack, verbChar)
        howMany -= 1
    return q

# def ra():
#     print("ra")
#     r(a)

# def rb():
#     print("rb")
#     r(b)

# def rr():
#     ra()
#     rb()


def rr(stack, verbChar=""):
    """The last element becomes the first one"""
    if stack:
        tmp = stack.pop()
        stack.insert(0, tmp)
        if verbChar:
            print("rr" + verbChar)
        return 1
    return 0

def revRotate(stack, howMany, verbChar=""):
    """Reverse rotates the stack
        the amount specififed"""
    q = howMany
    while howMany > 0:
        rr(stack, verbChar)
        howMany -= 1
    return q

# def rra():
#     print("rra")
#     rr(a)

# def rrb():
#     print("rrb")
#     rr(b)

# def rrr():
#     rra()
    # rrb()
