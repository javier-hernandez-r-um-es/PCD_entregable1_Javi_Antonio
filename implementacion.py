############## EXCEPCIONES #####3

class ErrorDeFormato(Exception):
    """Excepción debida a errores en el formato de los datos."""
    pass



class Persona:
    lista_dni = []
    def __init__(self, nombre, dni, direccion, sexo):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion

        if sexo not in ["V", "M"]:
            raise ErrorDeFormato("El sexo debe ser 'V' (varón) o 'M' (mujer).")
        else:
            self.sexo = sexo
  
        if dni in Persona.lista_dni:
            raise ErrorDeFormato("El DNI debe ser único.")
        elif len(dni)!= 9:
            raise ErrorDeFormato("El DNI debe tener 9 dígitos.")
        else:
            Persona.lista_dni.append(dni)


    def getNombre(self):
        return self.nombre

    def getDNI(self):
        return self.dni

    def getDireccion(self):
        return self.direccion

    def getSexo(self):
        return self.sexo

    def setNombre(self, nombre):
        self.nombre = nombre

    def setDireccion(self, direccion):
        self.direccion = direccion

    def setSexo(self, sexo):
        self.sexo = sexo


class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo, numero_expediente):
        super().__init__(nombre, dni, direccion, sexo)
        self.numero_expediente = numero_expediente
        self.listado_asignaturas = []

    def getNumeroExpediente(self):
        return self.numero_expediente

    def setNumeroExpediente(self, numero_expediente):
        self.numero_expediente = numero_expediente

    def getListadoAsignaturas(self):
        return self.listado_asignaturas

    def setListadoAsignaturas(self, listado_asignaturas):
        self.listado_asignaturas = listado_asignaturas

    def matricular(self, asignatura):

        if asignatura in self.listado_asignaturas:
            raise ErrorDeFormato("La asignatura ya está matriculada.")
        else:
            self.listado_asignaturas.append(asignatura)
        

    def desmatricular(self, asignatura):

        if asignatura not in self.listado_asignaturas:
            raise ErrorDeFormato("La asignatura no está matriculada.")
        else:
            self.listado_asignaturas.remove(asignatura)



class MiembroDepartamento(Persona):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento):
        super().__init__(nombre, dni, direccion, sexo)
        self.id = id
        self.departamento = departamento

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getDepartamento(self):
        return self.departamento

    def setDepartamento(self, departamento):
        self.departamento = departamento

    def devolverDatos(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Departamento: {self.departamento}"
    
class Departamento:
    DIIC = "DIIC"
    DITEC = "DITEC"
    DIS = "DIS"



class Investigador(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, id, departamento)
        self.area_investigacion = area_investigacion

    def getAreaInvestigacion(self):
        return self.area_investigacion

    def setAreaInvestigacion(self, area_investigacion):
        self.area_investigacion = area_investigacion


class ProfesorTitular(Investigador):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, id, departamento, area_investigacion)
        self.listado_asignaturas = []

    def getListadoAsignaturas(self):
        return self.listado_asignaturas

    def setListadoAsignaturas(self, listado_asignaturas):
        self.listado_asignaturas = listado_asignaturas

    def impartirAsignatura(self, asignatura):
        self.listado_asignaturas.append(asignatura)

    def dejarDeImpartirAsignatura(self, asignatura):
        if asignatura in self.listado_asignaturas:
            self.listado_asignaturas.remove(asignatura)

class ProfesorAsociado(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento):
        super().__init__(nombre, dni, direccion, sexo, id, departamento)
        self.listado_asignaturas = []

    def getListadoAsignaturas(self):
        return self.listado_asignaturas

    def setListadoAsignaturas(self, listado_asignaturas):
        self.listado_asignaturas = listado_asignaturas

    def impartirAsignatura(self, asignatura):
        self.listado_asignaturas.append(asignatura)

    def dejarDeImpartirAsignatura(self, asignatura):
        if asignatura in self.listado_asignaturas:
            self.listado_asignaturas.remove(asignatura)


class Asignatura:
    def __init__(self, nombre, codigo_asignatura, creditos, carrera, curso, departamento):
        self.nombre = nombre
        self.codigo_asignatura = codigo_asignatura
        self.creditos = creditos
        self.carrera = carrera
        self.curso = curso
        self.departamento = departamento

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getCodigoAsignatura(self):
        return self.codigo_asignatura

    def setCodigoAsignatura(self, codigo_asignatura):
        self.codigo_asignatura = codigo_asignatura

    def getCreditos(self):
        return self.creditos

    def setCreditos(self, creditos):
        self.creditos = creditos

    def getCarrera(self):
        return self.carrera

    def setCarrera(self, carrera):
        self.carrera = carrera

    def getCurso(self):
        return self.curso

    def setCurso(self, curso):
        self.curso = curso

    def getDepartamento(self):
        return self.departamento

    def setDepartamento(self, departamento):
        self.departamento = departamento


class Universidad:
    def __init__(self):
        self.lista_miembros_departamento = []
        self.lista_estudiantes = []

    def añadirMiembroDepartamento(self, miembro):
        self.lista_miembros_departamento.append(miembro)

    def eliminarMiembroDepartamento(self, miembro):
        if miembro in self.lista_miembros_departamento:
            self.lista_miembros_departamento.remove(miembro)

    def añadirEstudiante(self, estudiante):

        if estudiante in self.lista_estudiantes:
            raise ErrorDeFormato("El estudiante ya está añadido.")
        else:
            self.lista_estudiantes.append(estudiante)


    def eliminarEstudiante(self, estudiante):

        if estudiante not in self.lista_estudiantes:
            raise ErrorDeFormato("El estudiante no está añadido")
        else:
            self.lista_estudiantes.remove(estudiante)

###### PRUEBA ##########3
departamento1 = Departamento.DIIC
departamento2 = Departamento.DITEC
departamento3 = Departamento.DIS

persona1 = Persona("Juan", "12345678A", "Calle Mayor 1", "V")
persona2 = Persona("María", "12355678A", "Avenida Principal 10", "M")



estudiante1 = Estudiante("Pedro", "98765432C", "Plaza España 5", "V", "2021001")
estudiante2 = Estudiante("Ana", "65432109D", "Paseo de la Castellana 20", "M", "2021002")

profesor_asociado1 = ProfesorAsociado("Carlos", "45678901E", "Avenida Libertad 15", "V", 1, departamento1)
profesor_asociado2 = ProfesorAsociado("Elena", "34567890F", "Calle Real 30", "M", 2, departamento2)

profesor_titular1 = ProfesorTitular("Luis", "21098765G", "Calle Mayor 2", "V", 3, departamento3, "Inteligencia Artificial")
profesor_titular2 = ProfesorTitular("Laura", "10987654H", "Avenida Principal 11", "M", 4, departamento1, "Redes de Computadoras")

asignatura1 = Asignatura("Programación", "PROG101", 6, "Informática", 1, departamento1)
asignatura2 = Asignatura("Base de Datos", "BD101", 6, "Informática", 2, departamento2)

universidad = Universidad()

# añadimos y eliminamos miembros de departamentosx y estudiantes
universidad.añadirMiembroDepartamento(profesor_asociado1)
universidad.añadirMiembroDepartamento(profesor_asociado2)
universidad.añadirMiembroDepartamento(profesor_titular1)
universidad.añadirMiembroDepartamento(profesor_titular2)

universidad.eliminarMiembroDepartamento(profesor_titular2)

universidad.añadirEstudiante(estudiante1)
universidad.añadirEstudiante(estudiante2)

universidad.eliminarEstudiante(estudiante2)

print("Lista de miembros de departamento:")
for miembro in universidad.lista_miembros_departamento:
    print(miembro.getNombre())

print("\nLista de estudiantes:")
for estudiante in universidad.lista_estudiantes:
    print(estudiante.getDNI())
