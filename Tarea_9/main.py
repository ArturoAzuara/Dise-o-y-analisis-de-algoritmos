camino = []


def cargar_laberinto():
    laberinto = []
    archivo = open('labe.csv', 'r')
    for linea in archivo:
        laberinto.append(linea.strip().split(','))
    archivo.close()
    return laberinto


def mostrar_laberinto(laberinto):
    for indice, fila in enumerate(laberinto):
        print(f"{indice} {fila}")


def movimiento_valido(laberinto, fila, columna):
    if fila < 0 or fila >= len(laberinto) or columna < 0 or columna >= len(laberinto[0]):
        return False
    return laberinto[fila][columna] != 'm'


def mover(laberinto, fila, columna, direccion):
    movimientos = {
        "arriba": (-1, 0),
        "abajo": (1, 0),
        "izquierda": (0, -1),
        "derecha": (0, 1)
    }
    cambio_fila, cambio_columna = movimientos[direccion]
    nueva_fila, nueva_columna = fila + cambio_fila, columna + cambio_columna

    if movimiento_valido(laberinto, nueva_fila, nueva_columna):
        return nueva_fila, nueva_columna
    return fila, columna


def buscar_inicio(laberinto, inicio):
    for fila in range(len(laberinto)):
        if inicio in laberinto[fila]:
            columna = laberinto[fila].index(inicio)
            return fila, columna
    return -1, -1


def principal():
    laberinto = cargar_laberinto()
    fila_inicio, columna_inicio = buscar_inicio(laberinto, 'A')

    if fila_inicio == -1:
        print("El laberinto no tiene un punto de inicio.")
        return

    camino.append((fila_inicio, columna_inicio))
    laberinto[fila_inicio][columna_inicio] = 'v'

    solucion_encontrada = False
    pasos = 0

    while camino and not solucion_encontrada:
        pasos += 1
        fila, columna = camino[-1]

        for direccion in ["izquierda", "arriba", "derecha", "abajo"]:
            nueva_fila, nueva_columna = mover(laberinto, fila, columna, direccion)

            if (nueva_fila, nueva_columna) != (fila, columna):
                if laberinto[nueva_fila][nueva_columna] == 'f':
                    laberinto[nueva_fila][nueva_columna] = 'S'
                    solucion_encontrada = True
                    break
                elif laberinto[nueva_fila][nueva_columna] == 'l':
                    laberinto[nueva_fila][nueva_columna] = 'v'
                    camino.append((nueva_fila, nueva_columna))
                    break
        else:
            laberinto[fila][columna] = 'X'
            camino.pop()

    if solucion_encontrada:
        print(f"La solución cuenta con {pasos} pasos:")
    else:
        print("No se encontró ninguna solución.")

    mostrar_laberinto(laberinto)


if __name__ == "__main__":
    principal()
