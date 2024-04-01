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

class Departamento:
    DIIC = 'Departamento de Ingeniería Informática y de Computadores'
    DITEC = 'Departamento de Ingeniería Telemática'
    DIS = 'Departamento de Ingeniería de Sistemas Telemáticos'

class Universidad:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.listado_estudiantes = []
        self.listado_profesores = []
        self.listado_investigadores = []
        self.listado_asignaturas = []

    def devolverMiembro(self, identificador):
        for profesor in self.listado_profesores:
            if profesor.id == identificador:
                return profesor
        for investigador in self.listado_investigadores:
            if investigador.id == identificador:
                return investigador
        return None

    def devolverEstudiante(self, numero_expediente):
        for estudiante in self.listado_estudiantes:
            if estudiante.numero_expediente == numero_expediente:
                return estudiante
        return None

    def devolverAsignatura(self, codigo_asignatura):
        for asignatura in self.listado_asignaturas:
            if asignatura.codigo_asignatura == codigo_asignatura:
                return asignatura
        return None
    
    def incorporar_asignatura(self, nombre, codigo_asignatura, creditos, carrera, curso, departamento):
        asignatura = Asignatura(nombre, codigo_asignatura)
        self.listado_asignaturas.append(asignatura)

    def incorporar_estudiante(self, nombre_estudiante, direccion, dni, numero_expediente, sexo):
        estudiante = Estudiante(nombre_estudiante, dni, sexo, direccion, numero_expediente)
        self.listado_estudiantes.append(estudiante)

    def incorporar_profesor(self, nombre, direccion, dni, identificador, sexo, tipo, departamento, area_investigacion=None):
        if tipo == 'Titular':
            profesor = ProfesorTitular(nombre, dni, sexo, direccion, identificador)
            self.listado_profesores.append(profesor)
            self.listado_investigadores.append(profesor)
        elif tipo == 'Asociado':
            profesor = ProfesorAsociado(nombre, dni, sexo, direccion, identificador)
            self.listado_profesores.append(profesor)
        else:
            raise ValueError("Tipo de profesor no válido")

    def incorporar_investigador(self, nombre, direccion, dni, identificador, sexo, departamento, area_investigacion):
        investigador = Investigador(nombre, dni, sexo, direccion, identificador)
        self.listado_investigadores.append(investigador)

    def mostrar_estudiantes(self):
        for estudiante in self.listado_estudiantes:
            print(estudiante.nombre, estudiante.numero_expediente)

    def mostrar_investigadores(self):
        for investigador in self.listado_investigadores:
            print(investigador.nombre, investigador.id)

    def mostrar_profesores_titulares(self):
        for profesor in self.listado_profesores:
            if isinstance(profesor, ProfesorTitular):
                print(profesor.nombre, profesor.id)

    def mostrar_profesores_asociados(self):
        for profesor in self.listado_profesores:
            if isinstance(profesor, ProfesorAsociado):
                print(profesor.nombre, profesor.id)

    def mostrar_profesores(self):
        for profesor in self.listado_profesores:
            print(profesor.nombre, profesor.id)

    def mostrar_asignaturas_departamento(self):
        # Implementación según necesidad
        pass

    def mostrar_miembros_departamento(self):
        # Implementación según necesidad
        pass

    def eliminar_estudiante(self, numero_expediente):
        for estudiante in self.listado_estudiantes:
            if estudiante.numero_expediente == numero_expediente:
                self.listado_estudiantes.remove(estudiante)

    def eliminar_miembro(self, identificador):
        for profesor in self.listado_profesores:
            if profesor.id == identificador:
                self.listado_profesores.remove(profesor)
                if isinstance(profesor, ProfesorTitular):
                    self.listado_investigadores.remove(profesor)
                break
        for investigador in self.listado_investigadores:
            if investigador.id == identificador:
                self.listado_investigadores.remove(investigador)
                break

    def eliminar_asignatura(self, codigo_asignatura):
        for asignatura in self.listado_asignaturas:
            if asignatura.codigo_asignatura == codigo_asignatura:
                self.listado_asignaturas.remove(asignatura)

    def cambiarDepartamento(self, departamentoActual, departamentoNuevo):
        # Implementación según necesidad
        pass

    def matricular(self, numero_expediente, codigo_asignatura):
        estudiante = self.devolverEstudiante(numero_expediente)
        asignatura = self.devolverAsignatura(codigo_asignatura)
        if estudiante and asignatura:
            estudiante.listado_asignaturas.append(asignatura)

    def desmatricular(self, identificadorEstudiante, codigo_asignatura):
        estudiante = self.devolverEstudiante(identificadorEstudiante)
        if estudiante:
            for asignatura in estudiante.listado_asignaturas:
                if asignatura.codigo_asignatura == codigo_asignatura:
                    estudiante.listado_asignaturas.remove(asignatura)
                    break

    def vincularProfesorAsignatura(self, codigo_asignatura, identificadorProfesor):
        # Implementación según necesidad
        pass

    def eliminarProfesorAsignatura(self, codigo_asignatura, identificadorProfesor):
        # Implementación según necesidad
        pass

    def cambiarIdentificador(self, identificador, nuevo_identificador):
        # Implementación según necesidad
        pass

    def cambiarNumeroExpediente(self, numero_expediente, nuevo_numero_expediente):
        # Implementación según necesidad
        pass

    def cambiarCodigoAsignatura(self, codigo, codigo_nuevo):
        # Implementación según necesidad
        pass

    def calcularMatricula(self, numero_expediente):
        # Implementación según necesidad
        pass

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de Universidad
    universidad = Universidad("Universidad Ejemplo", "Dirección Ejemplo")

    # Agregar estudiantes, profesores, investigadores, asignaturas, etc.
    universidad.incorporar_estudiante("Juan", "Calle Falsa 123", "12345678A", "EST001", "M")
    universidad.incorporar_estudiante("María", "Calle Falsa 456", "87654321B", "EST002", "F")

    universidad.incorporar_profesor("Pedro", "Calle Real 789", "98765432C", "PROF001", "M", "Titular", Departamento.DIIC)
    universidad.incorporar_profesor("Luisa", "Calle Principal 1", "45678901D", "PROF002", "F", "Asociado", Departamento.DITEC)

    universidad.incorporar_investigador("Juan", "Calle Falsa 123", "12345678A", "INV001", "M", Departamento.DIIC, "Área A")

    universidad.incorporar_asignatura("Matemáticas", "MAT001", 6, "Ingeniería", 1, Departamento.DIIC)

    # Utilizar otras funciones según sea necesario
    universidad.mostrar_estudiantes()
    universidad.mostrar_profesores()
    universidad.mostrar_investigadores()

=======
print("hola mundo.")

print("como estas")

for e in range(10):
    print(e)
>>>>>>> 0c87f5a28704c871b2f0c6f0bea6a61911e5ebcd





