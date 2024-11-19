n = 7  # Número de filas
m = 7  # Número de columnas

camino = []

def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)

def backtrack(x, y, ruta_actual, visitadas):
    if x == n - 1 and y == m - 1:
        ruta_actual.append((x, y))
        camino.extend(ruta_actual)
        print(f"\nCamino encontrado: {ruta_actual}")
        mostrar_tablero_con_camino(ruta_actual)
        return True

    visitadas.add((x, y))
    ruta_actual.append((x, y))

    if y + 3 < m and (x, y + 3) not in visitadas:
        if backtrack(x, y + 3, ruta_actual, visitadas):
            return True


    if x + 2 < n and (x + 2, y) not in visitadas:
        if backtrack(x + 2, y, ruta_actual, visitadas):
            return True


    ruta_actual.pop()
    visitadas.remove((x, y))
    return False

def mostrar_tablero_con_camino(ruta):
    tablero_visual = [[0 for _ in range(m)] for _ in range(n)]

    for (x, y) in ruta:
        tablero_visual[x][y] = 1

    imprimir_tablero(tablero_visual)

ruta_inicial = []
visitadas = set()

if not backtrack(0, 0, ruta_inicial, visitadas):
    print("\nNo se encontró un camino válido.")
else:
    print("\nSe encontró un camino válido.")

#