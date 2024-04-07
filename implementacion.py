
############### Ejercicio de Programación Orientada a Objetos con Python ###################
####################### Grado en Ciencia e Ingenieria de Datos #######################

#------------------------- clases ---------------------------#

class ErrorDeFormato(Exception):
    """Excepción debida a errores en el formato de los datos."""
    pass

class Persona:
    lista_dni = []
    def __init__(self, nombre, dni, direccion, sexo):
        # Verificamos que el nombre no contenga valores numéricos
        if not nombre.isalpha():
            raise ErrorDeFormato("El nombre no puede contener valores numéricos.")

        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion

        # Verificamos que el sexo sea 'V' o 'M'
        if sexo not in ["V", "M"]:
            raise ErrorDeFormato("El sexo debe ser 'V' (varón) o 'M' (mujer).")
        else:
            self.sexo = sexo
  
        # Verificamos que el DNI sea único y tenga 9 dígitos
        if dni in Persona.lista_dni:
            raise ErrorDeFormato("El DNI debe ser único.")
        elif len(dni) != 9:
            raise ErrorDeFormato("El DNI debe tener 9 dígitos.")
        else:
            Persona.lista_dni.append(dni)


    def getNombre(self):
        """Devuelve el nombre de la persona."""
        return self.nombre

    def getDNI(self):
        """Devuelve el DNI de la persona."""
        return self.dni

    def getDireccion(self):
        """Devuelve la dirección de la persona."""
        return self.direccion

    def getSexo(self):
        """Devuelve el sexo de la persona."""
        return self.sexo

    def setNombre(self, nombre):
        """Establece el nombre de la persona."""
        self.nombre = nombre

    def setDireccion(self, direccion):
        """Establece la dirección de la persona."""
        self.direccion = direccion

    def setSexo(self, sexo):
        """Establece el sexo de la persona."""
        self.sexo = sexo


class Estudiante(Persona):
    numeros_expedientes = []

    def __init__(self, nombre, dni, direccion, sexo, numero_expediente):
        super().__init__(nombre, dni, direccion, sexo)
        self.numero_expediente = numero_expediente
        self.listado_asignaturas = []
        # Verificamos que el número de expediente sea único
        if numero_expediente in Estudiante.numeros_expedientes:
            raise ErrorDeFormato("El número de expediente debe ser único.")
        else:
            Estudiante.numeros_expedientes.append(numero_expediente)

    def getNumeroExpediente(self):
        """Devuelve el número de expediente del estudiante."""
        return self.numero_expediente

    def setNumeroExpediente(self, numero_expediente):
        """Establece el número de expediente del estudiante."""
        self.numero_expediente = numero_expediente

    def getListadoAsignaturas(self):
        """Devuelve el listado de asignaturas matriculadas por el estudiante."""
        return self.listado_asignaturas

    def setListadoAsignaturas(self, listado_asignaturas):
        """Establece el listado de asignaturas matriculadas por el estudiante."""
        self.listado_asignaturas = listado_asignaturas

    def matricular(self, asignatura):
        """Matricula al estudiante en una asignatura."""
        # Verificamos que la asignatura no esté ya matriculada
        if asignatura in self.listado_asignaturas:
            raise ErrorDeFormato("La asignatura ya está matriculada.")
        else:
            self.listado_asignaturas.append(asignatura)
        

    def desmatricular(self, asignatura):
        """Desmatricula al estudiante de una asignatura."""
        # Verificamos que la asignatura esté matriculada para desmatricular
        if asignatura not in self.listado_asignaturas:
            raise ErrorDeFormato("La asignatura no está matriculada.")
        else:
            self.listado_asignaturas.remove(asignatura)


class MiembroDepartamento(Persona):
    id_lista = []

    def __init__(self, nombre, dni, direccion, sexo, id, departamento):
        super().__init__(nombre, dni, direccion, sexo)
        self.id = id
        self.departamento = departamento

        # Verificamos que el ID sea único
        if id in MiembroDepartamento.id_lista:
            raise ErrorDeFormato("El ID debe ser único.")
        else:
            MiembroDepartamento.id_lista.append(id)

        departamentos = ["DIIC", "DITEC", "DIS"]
        # Verificamos que el departamento sea válido
        if departamento not in departamentos:
            raise ErrorDeFormato("El departamento no es válido")

    def getId(self):
        """Devuelve el ID del miembro del departamento."""
        return self.id

    def setId(self, id):
        """Establece el ID del miembro del departamento."""
        self.id = id

    def getDepartamento(self):
        """Devuelve el departamento del miembro del departamento."""
        return self.departamento

    def setDepartamento(self, departamento):
        """Establece el departamento del miembro del departamento."""
        self.departamento = departamento

    def devolverDatos(self):
        """Devuelve los datos del miembro del departamento."""
        return f"ID: {self.id}, Nombre: {self.nombre}, Departamento: {self.departamento}"


class Investigador(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, id, departamento)
        self.area_investigacion = area_investigacion

    def getAreaInvestigacion(self):
        """Devuelve el área de investigación del investigador."""
        return self.area_investigacion

    def setAreaInvestigacion(self, area_investigacion):
        """Establece el área de investigación del investigador."""
        self.area_investigacion = area_investigacion


class ProfesorTitular(Investigador):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, id, departamento, area_investigacion)
        self.listado_asignaturas = []

    def getListadoAsignaturas(self):
        """Devuelve el listado de asignaturas impartidas por el profesor titular."""
        return self.listado_asignaturas

    def setListadoAsignaturas(self, listado_asignaturas):
        """Establece el listado de asignaturas impartidas por el profesor titular."""
        self.listado_asignaturas = listado_asignaturas

    def impartirAsignatura(self, asignatura):
        """Imparte una asignatura el profesor titular."""
        # Verificamos que la asignatura no esté ya impartida
        if asignatura in self.listado_asignaturas:
            raise ErrorDeFormato("La asignatura ya está impartida")
        else:
            self.listado_asignaturas.append(asignatura)
    
    def dejarDeImpartirAsignatura(self, asignatura):
        """Deja de impartir una asignatura el profesor titular."""
        # Verificamos que la asignatura esté impartida para dejar de impartirla
        if asignatura not in self.listado_asignaturas:
            raise ErrorDeFormato("La asignatura no está impartida.")
        else:
            self.listado_asignaturas.remove(asignatura)


class ProfesorAsociado(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento):
        super().__init__(nombre, dni, direccion, sexo, id, departamento)
        self.listado_asignaturas = []

    def getListadoAsignaturas(self):
        """Devuelve el listado de asignaturas impartidas por el profesor asociado."""
        return self.listado_asignaturas

    def setListadoAsignaturas(self, listado_asignaturas):
        """Establece el listado de asignaturas impartidas por el profesor asociado."""
        self.listado_asignaturas = listado_asignaturas

    def impartirAsignatura(self, asignatura):
        """Imparte una asignatura el profesor asociado."""
        # Verificamos que la asignatura no esté ya impartida
        if asignatura in self.listado_asignaturas:
            raise ErrorDeFormato("La asignatura ya está impartida")
        else:
            self.listado_asignaturas.append(asignatura)

    def dejarDeImpartirAsignatura(self, asignatura):
        """Deja de impartir una asignatura el profesor asociado."""
        # Verificamos que la asignatura esté impartida para dejar de impartirla
        if asignatura not in self.listado_asignaturas:
            raise ErrorDeFormato("La asignatura no está impartida.")
        else:
            self.listado_asignaturas.remove(asignatura)


class Asignatura:
    def __init__(self, nombre, codigo_asignatura, creditos, carrera, curso, departamento):
        self.nombre = nombre
        self.codigo_asignatura = codigo_asignatura

        # Verificamos que los créditos sean un valor numérico
        if not str(creditos).isdigit():
            raise ErrorDeFormato("Los créditos deben ser un valor numérico.")
        self.creditos = creditos

        self.carrera = carrera

        # Verificamos que el curso sea un valor numérico
        if not str(curso).isdigit():
            raise ErrorDeFormato("El curso debe ser un valor numérico.")
        self.curso = curso

        self.departamento = departamento

    def getNombre(self):
        """Devuelve el nombre de la asignatura."""
        return self.nombre

    def setNombre(self, nombre):
        """Establece el nombre de la asignatura."""
        self.nombre = nombre

    def getCodigoAsignatura(self):
        """Devuelve el código de la asignatura."""
        return self.codigo_asignatura

    def setCodigoAsignatura(self, codigo_asignatura):
        """Establece el código de la asignatura."""
        self.codigo_asignatura = codigo_asignatura

    def getCreditos(self):
        """Devuelve los créditos de la asignatura."""
        return self.creditos

    def setCreditos(self, creditos):
        """Establece los créditos de la asignatura."""
        self.creditos = creditos

    def getCarrera(self):
        """Devuelve la carrera de la asignatura."""
        return self.carrera

    def setCarrera(self, carrera):
        """Establece la carrera de la asignatura."""
        self.carrera = carrera

    def getCurso(self):
        """Devuelve el curso de la asignatura."""
        return self.curso

    def setCurso(self, curso):
        """Establece el curso de la asignatura."""
        self.curso = curso

    def getDepartamento(self):
        """Devuelve el departamento de la asignatura."""
        return self.departamento

    def setDepartamento(self, departamento):
        """Establece el departamento de la asignatura."""
        self.departamento = departamento


class Universidad:
    def __init__(self):
        self.lista_miembros_departamento = []
        self.lista_estudiantes = []

    def añadirMiembroDepartamento(self, miembro):
        """Añade un miembro al departamento."""
        # Verificamos que el miembro no esté ya añadido
        if miembro in self.lista_miembros_departamento:
            raise ErrorDeFormato("El miembro ya está añadido")
        else:
            self.lista_miembros_departamento.append(miembro)
        
    def eliminarMiembroDepartamento(self, miembro):
        """Elimina un miembro del departamento."""
        # Verificamos que el miembro esté añadido antes de eliminarlo
        if miembro not in self.lista_miembros_departamento:
            raise ErrorDeFormato("El miembro no está añadido")
        else:
            self.lista_miembros_departamento.remove(miembro)    

    
    def cambiarMiembroDepartamento(self, miembro, nuevo_departamento):
        """Cambia el departamento de un miembro."""
        # Cambiamos el departamento de un miembro
        if miembro in self.lista_miembros_departamento:
            miembro.setDepartamento(nuevo_departamento)
        else:
            raise ErrorDeFormato("El miembro no está añadido al departamento.")


    def añadirEstudiante(self, estudiante):
        """Añade un estudiante a la universidad."""
        # Verificamos que el estudiante no esté ya añadido
        if estudiante in self.lista_estudiantes:
            raise ErrorDeFormato("El estudiante ya está añadido.")
        else:
            self.lista_estudiantes.append(estudiante)


    def eliminarEstudiante(self, estudiante):
        """Elimina un estudiante de la universidad."""
        # Verificamos que el estudiante esté añadido antes de eliminarlo
        if estudiante not in self.lista_estudiantes:
            raise ErrorDeFormato("El estudiante no está añadido")
        else:
            self.lista_estudiantes.remove(estudiante)



#---------------------------- PRUEBA DEL CODIGO ------------------------------#


departamento1 = "DIIC"
departamento2 = "DITEC"
departamento3 = "DIS"

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


 #-------------------------------------------------------------- #
 

       
                                # AUTORES #

#                                 Antonio Barea Rodríguez: a.barearodriguez@um.es
#                                 Javier Hernandez Rosique: javier.hernandezr@um.es

#  Copyright (c) All rights reserved.