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


