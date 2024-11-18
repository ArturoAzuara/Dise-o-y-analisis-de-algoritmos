import heapq

def cargar_matriz():
    with open('laberinto.csv', 'r') as archivo:
        matriz = []
        for linea in archivo:
            fila = linea.strip().split(',')
            matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    for indice, fila in enumerate(matriz):
        print(f"{indice:2d} {fila}")

def es_movimiento_valido(matriz, fila, columna):
    total_filas = len(matriz)
    total_columnas = len(matriz[0]) if total_filas > 0 else 0
    return 0 <= fila < total_filas and 0 <= columna < total_columnas and matriz[fila][columna] != 'p'

def localizar_puntos(matriz, inicio, objetivo):
    coordenada_inicio = None
    coordenada_objetivo = None
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == inicio:
                coordenada_inicio = [fila, columna]
            if matriz[fila][columna] == objetivo:
                coordenada_objetivo = [fila, columna]
    return coordenada_inicio, coordenada_objetivo

def calcular_manhattan(actual, objetivo):
    return abs(actual[0] - objetivo[0]) + abs(actual[1] - objetivo[1])

def ejecutar_busqueda():
    matriz = cargar_matriz()  # Cargar matriz del archivo
    inicio, objetivo = localizar_puntos(matriz, 'E', 's')  # Buscar inicio y objetivo
    if inicio is None or objetivo is None:
        print("La matriz no tiene un inicio o un objetivo válidos.")
        return

    print("Matriz inicial:")
    mostrar_matriz(matriz)

    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio[0], inicio[1]))
    explorados = set()
    explorados.add((inicio[0], inicio[1]))
    matriz[inicio[0]][inicio[1]] = "Y"

    solucion_encontrada = False
    contador_movimientos = 0

    while cola_prioridad and not solucion_encontrada:
        _, fila_actual, columna_actual = heapq.heappop(cola_prioridad)

        if [fila_actual, columna_actual] == objetivo:
            matriz[fila_actual][columna_actual] = 'O'
            solucion_encontrada = True
            break

        direcciones = [
            (fila_actual - 1, columna_actual),
            (fila_actual + 1, columna_actual),
            (fila_actual, columna_actual - 1),
            (fila_actual, columna_actual + 1)
        ]

        for nueva_fila, nueva_columna in direcciones:
            if es_movimiento_valido(matriz, nueva_fila, nueva_columna) and (nueva_fila, nueva_columna) not in explorados:
                prioridad = calcular_manhattan((nueva_fila, nueva_columna), objetivo)
                heapq.heappush(cola_prioridad, (prioridad, nueva_fila, nueva_columna))
                explorados.add((nueva_fila, nueva_columna))
                matriz[nueva_fila][nueva_columna] = "Y"
                contador_movimientos += 1

    if solucion_encontrada:
        print("Solución encontrada:")
        mostrar_matriz(matriz)
        print(f"Número de movimientos: {contador_movimientos}")
    else:
        print("No se encontró una solución.")

if __name__ == '__main__':
    ejecutar_busqueda()
