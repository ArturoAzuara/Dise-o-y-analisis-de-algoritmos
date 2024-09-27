def busqueda_centinela(data, num_buscar):
    tmp = data[-1]          #T(n) = 1
    data[-1] = num_buscar   #T(n) = 1
    i = 0                   #T(n) = 1
    while data[i] != num_buscar: #T(n) = n
        i += 1
    data[-1] = tmp          #T(n) = 1
    if i < len(data) - 1 or data[-1] == num_buscar:
        return i            #T(n) = 1
    return -1               #T(n) = 1

#T(n) = n + 3 + 3 = n + 6
#Complejidad = O(n)

