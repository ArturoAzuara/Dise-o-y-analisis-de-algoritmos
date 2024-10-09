def encontrar_patron(array, patron):
    tamanio_array = len(array)
    tamanio_patron = len(patron)
    contador = 0
    for i in range((tamanio_array - tamanio_patron) + 1):
        for j in range(tamanio_patron):
            if array[i + j] == patron[j]:
                contador += 1
                if contador == tamanio_patron:
                    return True
            else:
                contador = 0
                break
    return False