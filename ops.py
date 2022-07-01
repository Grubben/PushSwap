def s(stack, verbChar=""):
    if stack and stack[0] and stack[1]:
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
    if stack:
        tmp = stack.pop(0)
        stack.append(tmp)
        if verbChar:
            print("r" + verbChar)
        return 1
    return 0

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
    if stack:
        tmp = stack.pop()
        stack.insert(0, tmp)
        if verbChar:
            print("rr" + verbChar)
        return 1
    return 0

# def rra():
#     print("rra")
#     rr(a)

# def rrb():
#     print("rrb")
#     rr(b)

# def rrr():
#     rra()
    # rrb()
