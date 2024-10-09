A = [-9, 3, 5, -2, 9, -7, 4, 8, 6]

mayor = A[0] * A[1]
for i in A:
    for j in A:
        mult = i * j
        if mult > mayor:
            mayor = mult
            print(f"Los numeros cuyo producto es mas alto, son: {i} x{j}={mayor}")