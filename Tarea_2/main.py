numeros = [1, 2, 3]  # Asignacion, T(n) = 1

print(f"Entrada: {numeros}")  # Asignacion, T(n) = 1

combinaciones = 0  # Asignacion, T(n) = 1

for n_1 in numeros:  # Asignacion, T(n) = n
    for n_2 in numeros:  # Asignacion, T(n) = n
        print(n_1, n_2)  # Asignacion, T(n) = 1
        combinaciones += 1  # Asignacion, T(n) = 1

print(f"Final: {combinaciones}")  # Asignacion, T(n) = 1

# T(n) = 1+1+1+n*n+1+1+1 = n^2 + 6
