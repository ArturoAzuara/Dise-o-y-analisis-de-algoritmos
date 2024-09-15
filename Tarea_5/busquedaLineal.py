def busqueda_lineal(data, num_buscar):
    for i in range(len(data)):
        if num_buscar == data[i]:
            return i

    return -1


