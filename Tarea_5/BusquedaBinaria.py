def busqueda_binaria(data, num_buscar):
    izquierda = 0
    derecha = len(data) - 1
    while izquierda <= derecha:
        div = (izquierda + derecha) // 2
        if data[div] == num_buscar:
            return div
        elif data[div] < num_buscar:
            izquierda = div + 1
        else:
            derecha = div - 1
    return -1


datos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''      0  1  2  3  4  5  6  7  8'''
print(busqueda_binaria(datos, 1))
