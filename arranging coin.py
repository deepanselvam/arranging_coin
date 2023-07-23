def scase(a):
    b = 0
    while a >= b + 1:
        a -= b + 1
        b += 1
    return b

a = int(input())
c = scase(a)
print(c)
