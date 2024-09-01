def secfibrec(n):
    if n == 0:
        return n
    else:
        secfibrec((n - 1) + (n - 2))


print(secfibrec(5))