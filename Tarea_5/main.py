from busquedaLineal import busqueda_lineal
from busquedaLinealCentinela import busqueda_centinela
from BusquedaBinaria import busqueda_binaria

numeros = [4, 5, 1, 8, 6, 9, 3]
'''        0  1  2  3  4  5  6        '''

print(f"Busqueda lineal: {busqueda_lineal(numeros, 9)}")
print(f"Busqueda con centinela: {busqueda_centinela(numeros, 6)}")

datos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''      0  1  2  3  4  5  6  7  8'''

print(f"Busqueda binaria: {busqueda_binaria(datos, 8)}")

