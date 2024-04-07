import pytest
from implementacion import *



def test_añadir_estudiante():
    Uni = Universidad()
    estudiante1 = Estudiante("Pedro", "98705432C", "Plaza España 5", "V", "2025001")

    Uni.añadirEstudiante(estudiante1)
    assert(estudiante1.dni) == "98705432C"
    



def test_añadir_miembrodepartame():
    Uni= Universidad()
    profesor_asociado1 = ProfesorAsociado("Carlos", "45678201E", "Avenida Libertad 15", "V", "22", "DIS")

    Uni.añadirMiembroDepartamento(profesor_asociado1)
    assert(profesor_asociado1.dni) == "45678201E"



def test_eliminar_estudiante():
    Uni = Universidad()
    estudiante1 = Estudiante("Pedro", "98705222C", "Plaza España 5", "V", "2022201")
    Uni.añadirEstudiante(estudiante1)
    Uni.eliminarEstudiante(estudiante1)
    assert(estudiante1 not in Uni.lista_estudiantes)



def test_profesor_titular_impartir_asignatura():
    profesor = ProfesorTitular("Nombre", "123456789", "Dirección", "V", "IiD", "DIIC", "Área")
    asignatura = Asignatura("Asignatura", "COD", 3, "Carrera", 1, "DIIC")
    profesor.impartirAsignatura(asignatura)
    assert asignatura in profesor.getListadoAsignaturas()




def test_profesor_titular_dejar_de_impartir_asignatura():
    profesor = ProfesorTitular("Nombre", "123426789", "Dirección", "V", "IiiD", "DIIC", "Área")
    asignatura = Asignatura("Asignatura", "COD", 3, "Carrera", 1, "DIIC")
    profesor.impartirAsignatura(asignatura)
    profesor.dejarDeImpartirAsignatura(asignatura)
    assert asignatura not in profesor.getListadoAsignaturas()




def test_profesor_asociado_impartir_asignatura():
    profesor = ProfesorAsociado("Nombre", "122456789", "Dirección", "V", "IiiiD", "DIIC")
    asignatura = Asignatura("Asignatura", "COD", 3, "Carrera", 1, "DIIC")
    profesor.impartirAsignatura(asignatura)
    assert asignatura in profesor.getListadoAsignaturas()




def test_profesor_asociado_dejar_de_impartir_asignatura():
    profesor = ProfesorAsociado("Nombre", "122456289", "Dirección", "V", "IiiiiD", "DIIC")
    asignatura = Asignatura("Asignatura", "COD", 3, "Carrera", 1, "DIIC")
    profesor.impartirAsignatura(asignatura)
    profesor.dejarDeImpartirAsignatura(asignatura)
    assert asignatura not in profesor.getListadoAsignaturas()


def test_dni_unico():
    # Creamos una instancia de Universidad
    universidad = Universidad()
    
    # Creamos dos estudiantes con el mismo DNI
    estudiante1 = Estudiante("juan", "122252789", "Dirección 1", "V", "001")
    estudiante2 = Estudiante("javi", "123222789", "Dirección 2", "M", "002")
    
    # Añadimos el primer estudiante a la universidad
    universidad.añadirEstudiante(estudiante1)
    
    # Intentamos añadir el segundo estudiante con el mismo DNI a la universidad
    with pytest.raises(ErrorDeFormato):
        universidad.añadirEstudiante(estudiante2)