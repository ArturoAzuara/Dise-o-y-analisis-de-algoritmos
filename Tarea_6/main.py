class Alumno:
    def __init__(self, n_cuenta, nombre, edad, email, semestre, materias, promedio):
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
    return {"valor": alumno, "izquierdo": None, "derecho": None}


def insertar(raiz, alumno):
    if raiz is None:
        return crear_nodo(alumno)
    if alumno.n_cuenta < raiz["valor"].n_cuenta:
        raiz["izquierdo"] = insertar(raiz["izquierdo"], alumno)
    elif alumno.n_cuenta > raiz["valor"].n_cuenta:
        raiz["derecho"] = insertar(raiz["derecho"], alumno)
    else:
        print(f"Error: El número de cuenta {alumno.n_cuenta} ya existe.")
        return raiz
    return raiz


def buscar(raiz, n_cuenta):
    if raiz is None or raiz["valor"].n_cuenta == n_cuenta:
        return raiz
    if n_cuenta < raiz["valor"].n_cuenta:
        return buscar(raiz["izquierdo"], n_cuenta)
    return buscar(raiz["derecho"], n_cuenta)


def inorden(raiz):
    if raiz:
        inorden(raiz["izquierdo"])
        print(raiz["valor"])
        inorden(raiz["derecho"])


def cargar_datos_desde_txt(ruta_archivo):
    raiz = None
    with open(ruta_archivo, "r", encoding="utf-8") as file:
        registros = file.readlines()

    for registro in registros:
        campos = registro.strip().split(", ")

        n_cuenta = int(campos[0])
        nombre = campos[1]
        edad = int(campos[2])
        email = campos[3]

        # Extraer solo el número del semestre
        semestre = int(campos[4].split()[1])  # Esto tomará el segundo elemento que es el número

        # Las materias abarcan desde el índice 5 hasta el penúltimo elemento
        materias = ", ".join(campos[5:-1])

        # Extraer solo el número del promedio
        promedio = float(campos[-1].split(": ")[1])  # Esto tomará el número después de "Promedio: "

        alumno = Alumno(n_cuenta, nombre, edad, email, semestre, materias, promedio)
        raiz = insertar(raiz, alumno)

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
    return insertar(raiz, alumno)


def menu_principal():
    raiz = cargar_datos_desde_txt("registros_alumnos.txt")

    while True:
        print("\n--- Menú Principal ---")
        print("1. Insertar nuevo alumno")
        print("2. Buscar alumno por número de cuenta")
        print("3. Mostrar todos los alumnos (Inorden)")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            raiz = insertar_usuario(raiz)
        elif opcion == "2":
            n_cuenta = int(input("Introduce el número de cuenta a buscar: "))
            resultado = buscar(raiz, n_cuenta)
            if resultado:
                print(f"Alumno encontrado: {resultado['valor']}")
            else:
                print(f"No se encontró ningún alumno con el número de cuenta {n_cuenta}.")
        elif opcion == "3":
            print("Lista de alumnos en orden (Inorden):")
            inorden(raiz)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu_principal()
