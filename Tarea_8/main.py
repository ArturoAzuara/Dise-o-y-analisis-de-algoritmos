def div_list(lista_numeros):
    if len(lista_numeros) < 2:  # O(1)
        return 0, 0, 0  # Retornar valores por defecto

    mitad = len(lista_numeros) // 2  # O(1)

    # Dividir la lista en dos mitades
    mitad_izquierda = lista_numeros[:mitad]  # O(n)
    mitad_derecha = lista_numeros[mitad:]  # O(n)

    # Llamar recursivamente a la función para ambas mitades
    max_prod_izq, num1_izq, num2_izq = div_list(mitad_izquierda)  # T(n/2)
    max_prod_der, num1_der, num2_der = div_list(mitad_derecha)  # T(n/2)

    # Calcular el producto cruzado
    if len(lista_numeros) < 2:  # O(1)
        return 0, 0, 0  # Retornar valores por defecto si hay menos de 2 elementos

    max_producto = lista_numeros[0] * lista_numeros[1]  # O(1)
    num1, num2 = lista_numeros[0], lista_numeros[1]  # O(1)

    for i in range(len(lista_numeros)):  # O(n)
        for j in range(i + 1, len(lista_numeros)):  # O(n)
            producto = lista_numeros[i] * lista_numeros[j]  # O(1)
            if producto > max_producto:  # O(1)
                max_producto = producto  # O(1)
                num1 = lista_numeros[i]  # O(1)
                num2 = lista_numeros[j]  # O(1)

    # Determinar el producto máximo y los números correspondientes
    if max_prod_izq >= max_prod_der and max_prod_izq >= max_producto:  # O(1)
        return max_prod_izq, num1_izq, num2_izq  # O(1)
    elif max_prod_der >= max_prod_izq and max_prod_der >= max_producto:  # O(1)
        return max_prod_der, num1_der, num2_der  # O(1)
    else:  # O(1)
        return max_producto, num1, num2  # O(1)


A = []
max_producto, num1, num2 = div_list(A)  # O(n^2)
print(f"Los números cuyo producto es más alto son: {num1} x {num2} = {max_producto}")


