n = 7  # Número de filas
m = 7  # Número de columnas

rutas = []

def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)

def backtrack(x, y, ruta_actual, visitadas):
    if x == n - 1 and y == m - 1:
        rutas.append(ruta_actual.copy())
        print(f"\nRuta completada: {ruta_actual}")
        mostrar_tablero_con_camino(ruta_actual)
        return

    visitadas.add((x, y))

    if y + 3 < m and (x, y + 3) not in visitadas:
        ruta_actual.append((x, y + 3))
        backtrack(x, y + 3, ruta_actual, visitadas)
        ruta_actual.pop()

    if x + 2 < n and (x + 2, y) not in visitadas:
        ruta_actual.append((x + 2, y))
        backtrack(x + 2, y, ruta_actual, visitadas)
        ruta_actual.pop()

    visitadas.remove((x, y))

def mostrar_tablero_con_camino(ruta):
    tablero_visual = [[0 for _ in range(m)] for _ in range(n)]

    for (x, y) in ruta:
        tablero_visual[x][y] = 1

    imprimir_tablero(tablero_visual)

ruta_inicial = [(0, 0)]
visitadas = set()
backtrack(0, 0, ruta_inicial, visitadas)

print(f"\nTotal de rutas encontradas: {len(rutas)}")





