n = 7  # Número de filas
m = 7  # Número de columnas

rutas = []

def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)

# Función de backtracking para encontrar todas las rutas posibles sin repetir casillas
def backtrack(x, y, ruta_actual, visitadas):
    # Si llegamos a la esquina inferior derecha, guardamos la ruta y mostramos el talblero
    if x == n - 1 and y == m - 1:
        rutas.append(ruta_actual.copy())
        print(f"\nRuta completada: {ruta_actual}")
        mostrar_tablero_con_camino(ruta_actual)
        return

    # Marcar la casilla actual como visitada
    visitadas.add((x, y))

    # Mover hacia la derecha 3 casillas si está dentro del límite y la casilla no ha sido visitada
    if y + 3 < m and (x, y + 3) not in visitadas:
        ruta_actual.append((x, y + 3))
        backtrack(x, y + 3, ruta_actual, visitadas)
        ruta_actual.pop()

    # Mover hacia abajo 2 casillas si está dentro del límite y la casilla no ha sido visitada
    if x + 2 < n and (x + 2, y) not in visitadas:
        ruta_actual.append((x + 2, y))
        backtrack(x + 2, y, ruta_actual, visitadas)
        ruta_actual.pop()

    # Desmarcar la casilla actual al regresar
    visitadas.remove((x, y))

# Función para mostrar el tablero con el camino marcado
def mostrar_tablero_con_camino(ruta):
    tablero_visual = [[0 for _ in range(m)] for _ in range(n)]

    for (x, y) in ruta:
        tablero_visual[x][y] = 1

    imprimir_tablero(tablero_visual)

ruta_inicial = [(0, 0)]
visitadas = set()
backtrack(0, 0, ruta_inicial, visitadas)

print(f"\nTotal de rutas encontradas: {len(rutas)}")





