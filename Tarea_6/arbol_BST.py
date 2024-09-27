# Función para crear un nodo
def crear_nodo(valor):
    return {"valor": valor, "izquierdo": None, "derecho": None}

# Función para insertar un valor en el BST
def insertar(raiz, valor):
    if raiz is None:
        return crear_nodo(valor)
    if valor < raiz["valor"]:
        raiz["izquierdo"] = insertar(raiz["izquierdo"], valor)
    elif valor > raiz["valor"]:
        raiz["derecho"] = insertar(raiz["derecho"], valor)
    return raiz

# Función para buscar un valor en el BST
def buscar(raiz, valor):
    if raiz is None or raiz["valor"] == valor:
        return raiz
    if valor < raiz["valor"]:
        return buscar(raiz["izquierdo"], valor)
    return buscar(raiz["derecho"], valor)

# Función para recorrer el BST en inorden (de menor a mayor)
def inorden(raiz):
    if raiz:
        inorden(raiz["izquierdo"])
        print(raiz["valor"], end=" ")
        inorden(raiz["derecho"])

# Ejemplo de uso
raiz = None
valores = [50, 30, 70, 20, 40, 60, 80]

# Insertar los valores en el BST
for valor in valores:
    raiz = insertar(raiz, valor)

# Mostrar el árbol en inorden
print("Recorrido inorden del árbol BST:")
inorden(raiz)
