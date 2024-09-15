def busqueda_lineal(data, num_buscar):
    for i in range(len(data)):      #T(n) = n
        if num_buscar == data[i]:
            return i                #T(n) = 1

    return -1                       #T(n) = 1

#T(n) = n + 1 + 1 = n + 2
#Complejidad = O(n)


