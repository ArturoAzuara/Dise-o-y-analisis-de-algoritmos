def busqueda_lineal(data, num_buscar):
    for i in range(len(data)):
        if num_buscar == data[i]:
            return print(f"El numero {num_buscar}, se encuentra en la posición {i}")

    return print(f"El numero {num_buscar}, no se encuentra en {data} ")


numeros = [4, 5, 1, 8, 6, 9, 3]
'''        0  1  2  3  4  5  6        '''
busqueda_lineal(numeros, 200)
