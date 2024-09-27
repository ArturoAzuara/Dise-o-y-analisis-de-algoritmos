class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.centro = None
        self.derecho = None


head = Nodo(20)
nodo_23 = Nodo(23)
nodo_19 = Nodo(19)
nodo_57 = Nodo(57)
nodo_67 = Nodo(67)
nodo_99 = Nodo(99)

head.izquierda = None
head.centro = nodo_19
head.derecho = nodo_23

nodo_23.centro = nodo_57
nodo_19.izquierda = nodo_67
nodo_67.centro = nodo_99

# Busqueda de nodo 99

nodo_99 = head.centro.izquierda.centro
print(f"El Nodo buscado es el siguiente: {nodo_99.valor}")

# Busqueda de nodo 57

nodo_57 = head.derecho.centro
print(f"El Nodo buscado es el siguiente: {nodo_57.valor}")