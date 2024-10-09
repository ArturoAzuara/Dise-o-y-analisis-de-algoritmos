A = [-9, 3, 5, -2, 9, -7, 4, 8, 6]

mayor = A[0] * A[1]  
num1 = A[0]
num2 = A[1]

for i in range(len(A)):
    for j in range(i + 1, len(A)):  
        mult = A[i] * A[j]
        if mult > mayor:
            mayor = mult
            num1 = A[i]
            num2 = A[j]

print(f"Los números cuyo producto es más alto, son: {num1} x {num2} = {mayor}")
