<<<<<<< HEAD
class Persona:
    def __init__(self, nombre, dni, sexo, direccion):
        self.nombre = nombre
        self.dni = dni
        self.sexo = sexo
        self.direccion = direccion

class Profesor(Persona):
    def __init__(self, nombre, dni, sexo, direccion, id):
        super().__init__(nombre, dni, sexo, direccion)
        self.id = id

class ProfesorAsociado(Profesor):
    def __init__(self, nombre, dni, sexo, direccion, id):
        super().__init__(nombre, dni, sexo, direccion, id)

class Investigador(Profesor):
    def __init__(self, nombre, dni, sexo, direccion, id):
        super().__init__(nombre, dni, sexo, direccion, id)

class ProfesorTitular(Investigador):
    def __init__(self, nombre, dni, sexo, direccion, id):
        super().__init__(nombre, dni, sexo, direccion, id)

class Estudiante(Persona):
    def __init__(self, nombre, dni, sexo, direccion, numero_expediente):
        super().__init__(nombre, dni, sexo, direccion)
        self.numero_expediente = numero_expediente
        self.listado_asignaturas = []

class Asignatura:
    def __init__(self, nombre, codigo_asignatura):
        self.nombre = nombre
        self.codigo_asignatura = codigo_asignatura

class MiembroDepartamento(Persona):
    def __init__(self, nombre, dni, sexo, direccion, departamento):
        super().__init__(nombre, dni, sexo, direccion)
        self.departamento = departamento


=======
print("hola mundo.")

<<<<<<< HEAD
print("como la estas")
=======
print("como estas")

for e in range(10):
    print(e)
>>>>>>> 0c87f5a28704c871b2f0c6f0bea6a61911e5ebcd
>>>>>>> f180f8577ee66f0c5b90bad8ba14309d7cd2c016


    




