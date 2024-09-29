class Alumno:
    def __init__(self, n_cuenta, nombre, edad, email, semestre, materias, promedio):
        # O(1): Inicialización de atributos, no depende del tamaño de los datos
        self.__n_cuenta = n_cuenta
        self.__nombre = nombre
        self.__edad = edad
        self.__email = email
        self.__semestre = semestre
        self.__materias = materias
        self.__promedio = promedio

    @property
    def n_cuenta(self):
        return self.__n_cuenta

    def __str__(self):
        return f"{self.__n_cuenta}, {self.__nombre}, {self.__edad}, {self.__email}, {self.__semestre}, {self.__materias}, {self.__promedio}"


def crear_nodo(alumno):
    # O(1): Crear un nodo nuevo, operación constante
    return {"valor": alumno, "izquierdo": None, "derecho": None}


def insertar(raiz, alumno):
    if raiz is None:
        # O(1): Inserción en un árbol vacío
        return crear_nodo(alumno)

    if alumno.n_cuenta < raiz["valor"].n_cuenta:
        # Promedio: O(log n): Reduciendo el árbol por la mitad
        raiz["izquierdo"] = insertar(raiz["izquierdo"], alumno)
    elif alumno.n_cuenta > raiz["valor"].n_cuenta:
        # Promedio: O(log n): Reduciendo el árbol por la mitad
        raiz["derecho"] = insertar(raiz["derecho"], alumno)
    else:
        print(f"Error: El número de cuenta {alumno.n_cuenta} ya existe.")
        return raiz
    # Promedio: O(log n), Peor caso: O(n): si el árbol está desbalanceado
    return raiz


def buscar(raiz, n_cuenta):
    if raiz is None or raiz["valor"].n_cuenta == n_cuenta:
        # O(1): Comparación directa
        return raiz

    if n_cuenta < raiz["valor"].n_cuenta:
        # Promedio: O(log n)
        return buscar(raiz["izquierdo"], n_cuenta)

    # Promedio: O(log n)
    return buscar(raiz["derecho"], n_cuenta)


def inorden(raiz):
    if raiz:
        # O(n): Se recorre cada nodo exactamente una vez
        inorden(raiz["izquierdo"])
        print(raiz["valor"])
        inorden(raiz["derecho"])


def cargar_datos_desde_txt(ruta_archivo):
    raiz = None
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        registros = file.readlines()  # O(m): Leer líneas del archivo

    for registro in registros:
        campos = registro.strip().split(", ")
        n_cuenta = int(campos[0])
        nombre = campos[1]
        edad = int(campos[2])
        email = campos[3]
        semestre = int(campos[4].split()[1])  # O(1): Extraer el semestre
        materias = ", ".join(campos[5:-1])  # O(k): Donde k es el número de materias
        promedio = float(campos[-1].split(": ")[1])  # O(1): Extraer promedio

        alumno = Alumno(n_cuenta, nombre, edad, email, semestre, materias, promedio)
        # Promedio: O(log n): Inserción en un BST equilibrado
        raiz = insertar(raiz, alumno)

    # Promedio: O(m log n): Insertar m registros en un BST equilibrado
    return raiz


def insertar_usuario(raiz):
    n_cuenta = int(input("Número de cuenta: "))
    if buscar(raiz, n_cuenta):
        print(f"El número de cuenta {n_cuenta} ya existe.")
        return raiz

    nombre = input("Nombre completo: ")
    edad = int(input("Edad: "))
    email = input("Email: ")
    semestre = int(input("Semestre: "))
    materias = input("Materias (separadas por comas): ")
    promedio = float(input("Promedio: "))

    alumno = Alumno(n_cuenta, nombre, edad, email, semestre, materias, promedio)
    # Promedio: O(log n): Inserción en un BST equilibrado
    return insertar(raiz, alumno)


def menu_principal():
    # Carga inicial de datos
    raiz = cargar_datos_desde_txt("registros_alumnos.txt")  # O(m log n) promedio

    while True:
        print("\n--- Menú Principal ---")
        print("1. Insertar nuevo alumno")
        print("2. Buscar alumno por número de cuenta")
        print("3. Mostrar todos los alumnos")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            raiz = insertar_usuario(raiz)  # O(log n) promedio
        elif opcion == "2":
            n_cuenta = int(input("Introduce el número de cuenta a buscar: "))
            resultado = buscar(raiz, n_cuenta)  # O(log n) promedio
            if resultado:
                print(f"Alumno encontrado: {resultado['valor']}")
            else:
                print(f"No se encontró ningún alumno con el número de cuenta {n_cuenta}.")
        elif opcion == "3":
            print("Lista de alumnos en orden :")
            inorden(raiz)  # O(n)
        elif opcion == "4":
            print("Gracias, vuelva pronto")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu_principal()
