camino = []

def cargar_laberinto():
    with open('labe.csv', 'r') as archivo:
        laberinto = []
        for linea in archivo:
            fila = linea.strip().split(',')
            laberinto.append(fila)
    return laberinto

def mostrar_laberinto(laberinto):
    for i in range(len(laberinto)):
        print(f"{i} {laberinto[i]}")

def movimiento_valido(laberinto, fila, columna):
    total_filas = len(laberinto)
    total_columnas = len(laberinto[0]) if total_filas > 0 else 0
    return 0 <= fila < total_filas and 0 <= columna < total_columnas and laberinto[fila][columna] != 'm'

def mover_arriba(laberinto, fila, columna):
    if movimiento_valido(laberinto, fila - 1, columna):
        return fila - 1, columna
    return None

def mover_abajo(laberinto, fila, columna):
    if movimiento_valido(laberinto, fila + 1, columna):
        return fila + 1, columna
    return None

def mover_izquierda(laberinto, fila, columna):
    if movimiento_valido(laberinto, fila, columna - 1):
        return fila, columna - 1
    return None

def mover_derecha(laberinto, fila, columna):
    if movimiento_valido(laberinto, fila, columna + 1):
        return fila, columna + 1
    return None

def buscar_inicio(laberinto, inicio):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == inicio:
                return i, j
    return None

def principal():
    laberinto = cargar_laberinto()
    fila_inicio, columna_inicio = buscar_inicio(laberinto, 'A')

    if fila_inicio is None or columna_inicio is None:
        print("El laberinto no tiene un punto de inicio.")
        return

    camino.append((fila_inicio, columna_inicio))
    laberinto[fila_inicio][columna_inicio] = 'v'

    solucion_encontrada = False
    pasos = 0

    while camino and not solucion_encontrada:
        pasos += 1
        fila, columna = camino[-1]

        nueva_pos = mover_izquierda(laberinto, fila, columna)
        if nueva_pos:
            nueva_fila, nueva_columna = nueva_pos
            if laberinto[nueva_fila][nueva_columna] == 'f':
                laberinto[nueva_fila][nueva_columna] = 'S'
                solucion_encontrada = True
            elif laberinto[nueva_fila][nueva_columna] == 'l':
                laberinto[nueva_fila][nueva_columna] = 'v'
                camino.append((nueva_fila, nueva_columna))
                continue

        nueva_pos = mover_arriba(laberinto, fila, columna)
        if nueva_pos:
            nueva_fila, nueva_columna = nueva_pos
            if laberinto[nueva_fila][nueva_columna] == 'f':
                laberinto[nueva_fila][nueva_columna] = 'S'
                solucion_encontrada = True
            elif laberinto[nueva_fila][nueva_columna] == 'l':
                laberinto[nueva_fila][nueva_columna] = 'v'
                camino.append((nueva_fila, nueva_columna))
                continue

        nueva_pos = mover_derecha(laberinto, fila, columna)
        if nueva_pos:
            nueva_fila, nueva_columna = nueva_pos
            if laberinto[nueva_fila][nueva_columna] == 'f':
                laberinto[nueva_fila][nueva_columna] = 'S'
                solucion_encontrada = True
            elif laberinto[nueva_fila][nueva_columna] == 'l':
                laberinto[nueva_fila][nueva_columna] = 'v'
                camino.append((nueva_fila, nueva_columna))
                continue

        nueva_pos = mover_abajo(laberinto, fila, columna)
        if nueva_pos:
            nueva_fila, nueva_columna = nueva_pos
            if laberinto[nueva_fila][nueva_columna] == 'f':
                laberinto[nueva_fila][nueva_columna] = 'S'
                solucion_encontrada = True
            elif laberinto[nueva_fila][nueva_columna] == 'l':
                laberinto[nueva_fila][nueva_columna] = 'v'
                camino.append((nueva_fila, nueva_columna))
                continue

        if not solucion_encontrada:
            laberinto[fila][columna] = 'X'
            camino.pop()

    if solucion_encontrada:
        print(f"La solución cuenta con {pasos} pasos:")
    else:
        print("No se encontró ninguna solución.")

    mostrar_laberinto(laberinto)

if __name__ == "__main__":
    principal()
