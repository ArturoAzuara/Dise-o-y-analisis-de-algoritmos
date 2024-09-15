def busqueda_centinela(data, num_buscar):
    tmp = data[-1]
    data[-1] = num_buscar
    i = 0
    while data[i] != num_buscar:
        i += 1
    data[-1] = tmp
    if i < len(data) - 1 or data[-1] == num_buscar:
        return i
    return -1


datos = [3, 4, 7, 9, 2, 5]
'''      0  1  2  3  4  5      '''
print(busqueda_centinela(datos, 8))
