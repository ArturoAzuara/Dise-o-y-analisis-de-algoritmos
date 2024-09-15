def secfibrec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return secfibrec(n - 1) + secfibrec(n - 2)


print(secfibrec(6))
