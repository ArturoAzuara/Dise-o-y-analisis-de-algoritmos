def busqueda_lineal(data, num_buscar):
    for i in range(len(data)):
        if num_buscar == data[i]:
            return i

    return -1


numeros = [4, 5, 1, 8, 6, 9, 3]
'''        0  1  2  3  4  5  6        '''
print(busqueda_lineal(numeros, 3))
