def busqueda_binaria(data, num_buscar):
    izquierda = 0               #T(n) = 1
    derecha = len(data) - 1     #T(n) = 1
    while izquierda <= derecha: #T(n) = log n
        div = (izquierda + derecha) // 2
        if data[div] == num_buscar:
            return div  #T(n) = 1
        elif data[div] < num_buscar:
            izquierda = div + 1 #T(n) = 1
        else:
            derecha = div - 1 #T(n) = 1
    return -1 #T(n) = 1

#T(n) = 2 + log n + 4 
#Complejidad = O(log n)