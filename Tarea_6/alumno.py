class Alumno:
    descripcion = "This is the first prototipe of class student"

    def __init__(self, n_cuenta, nombre, edad, email, semestre, materias, promedio):
        self.__n_cuenta = n_cuenta
        self.__nombre = nombre
        self.__edad = edad
        self.__email = email
        self.__semestre = semestre
        self.__materias = materias
        self.__promedio = promedio

    @property
    def n_cuenta(self) -> int:
        return self.__n_cuenta

    @n_cuenta.setter
    def n_cuenta(self, n_cuenta: int) -> None:
        self.__n_cuenta = n_cuenta

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self, edad: int) -> None:
        self.__edad = edad

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def semestre(self) -> int:
        return self.__semestre

    @semestre.setter
    def semestre(self, semestre: int) -> None:
        self.__semestre = semestre

    @property
    def materias(self) -> str:
        return self.__materias

    @materias.setter
    def materias(self, materias: str) -> None:
        self.__materias = materias

    @property
    def promedio(self) -> float:
        return self.__promedio

    @promedio.setter
    def promedio(self, promedio: float) -> None:
        self.__promedio = promedio
