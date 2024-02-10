"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    return controller.new_controller()


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    prefix = select_size()
    number_jobs, number_multilocation, number_skills, number_employments = controller.load_data(control, prefix)
    lista_jobs = controller["jobs"]
    lista = primeros_y_ultimos_n(lista_jobs, 3)
    return lista, number_jobs, number_multilocation, number_skills, number_employments

def select_size():
    """
    Selecciona el tamaño de la muestra
    """
    print("Seleccione el tamaño de la muestra")
    print("1- Small")
    print("2- 10%")
    print("3- 20%")
    print("4- 30%")
    print("5- 40%")
    print("6- 50%")
    print("7- medium")
    print("8- 60%")
    print("9- 70%")
    print("10- 80%")
    print("11- 90%")
    print("12- Large")

    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 1:
        return "small"
    elif int(inputs) == 2:
        return "10"
    elif int(inputs) == 3:
        return "20"
    elif int(inputs) == 4:
        return "30"
    elif int(inputs) == 5:
        return "40"
    elif int(inputs) == 6:
        return "50"
    elif int(inputs) == 7:
        return "medium"
    elif int(inputs) == 8:
        return "60"
    elif int(inputs) == 9:
        return "70"
    elif int(inputs) == 10:
        return "80"
    elif int(inputs) == 11:
        return "90"
    elif int(inputs) == 12:
        return "large"
    else:
        print("Opción errónea, vuelva a elegir.\n")
        return select_size()
    
def primeros_y_ultimos_n(lista, n):
    """
    Retorna los primeros y últimos n elementos de una lista
    """
    primeros = lt.subList(lista, 1, n)
    ultimos = lt.subList(lista, lt.size(lista)-n, n)
    for i in range(lt.size(ultimos)):
        lt.addLast(primeros, lt.getElement(ultimos, i))
    return primeros

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    numero_ofertas = int(input("Ingrese el número de ofertas que desea filtrar: "))
    codigo_pais = input("Ingrese el código del país que desea filtrar: ")
    nivel_experiencia = input("Ingrese el nivel de experiencia que desea filtrar: ")
    lista = controller.req_1(control, codigo_pais, nivel_experiencia)
    lista_n = lt.subList(lista, 1, numero_ofertas)
    print("El numero de ofertas encontradas es: " + str(lt.size(lista)))
    print(tabulate(lt.iterator(lista_n), headers="keys", tablefmt="grid"))
    


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    numero_ofertas = int(input("Ingrese el número de ofertas que desea filtrar: "))
    nombre_empresa = input("Ingrese el nombre de la empresa que desea filtrar: ")
    nombre_ciudad = input("Ingrese el nombre de la ciudad que desea filtrar: ")
    lista = controller.req_2(control, nombre_empresa, nombre_ciudad)
    lista_n = lt.subList(lista, 1, numero_ofertas)
    print("El numero de ofertas encontradas es: " + str(lt.size(lista)))
    print(tabulate(lt.iterator(lista_n), headers="keys", tablefmt="grid"))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    nombre_empresa = input("Ingrese el nombre de la empresa que desea filtrar: ")
    fecha_inicio = input("Ingrese la fecha de inicio que desea filtrar: ")
    fecha_fin = input("Ingrese la fecha de fin que desea filtrar: ")
    lista, numero_junior, numero_mid, numero_senior = controller.req_3(control, nombre_empresa, fecha_inicio, fecha_fin)
    print("El numero de empleados encontrados es: " + str(lt.size(lista)))
    print("El numero de empleados junior es: " + str(numero_junior))
    print("El numero de empleados mid es: " + str(numero_mid))
    print("El numero de empleados senior es: " + str(numero_senior))
    print(tabulate(lt.iterator(lista), headers="keys", tablefmt="grid"))

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    codigo_pais = input("Ingrese el código del país que desea filtrar: ")
    fecha_inicio = input("Ingrese la fecha de inicio que desea filtrar: ")
    fecha_fin = input("Ingrese la fecha de fin que desea filtrar: ")
    lista, numero_empresas, numero_ciudades, ciudad_mayor_ofertas, ciudad_menor_ofertas = controller.req_4(control, codigo_pais, fecha_inicio, fecha_fin)
    print("El numero de ofertas encontradas es: " + str(lt.size(lista)))
    print("El numero de empresas encontradas es: " + str(numero_empresas))
    print("El numero de ciudades encontradas es: " + str(numero_ciudades))
    print("La ciudad con mayor número de ofertas es: " + ciudad_mayor_ofertas)
    print("La ciudad con menor número de ofertas es: " + ciudad_menor_ofertas)
    print(tabulate(lt.iterator(lista), headers="keys", tablefmt="grid"))
    


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    nombre_ciuadad = input("Ingrese el nombre de la ciudad que desea filtrar: ")
    fecha_inicio = input("Ingrese la fecha de inicio que desea filtrar: ")
    fecha_fin = input("Ingrese la fecha de fin que desea filtrar: ")
    lista, numero_empresas, empresa_mas_ofertas, empresa_menos_ofertas = controller.req_5(control, nombre_ciuadad, fecha_inicio, fecha_fin)
    print("El numero de ofertas encontradas es: " + str(lt.size(lista)))
    print("El numero de empresas encontradas es: " + str(numero_empresas))
    print("La empresa con mayor número de ofertas es: " + empresa_mas_ofertas)
    print("La empresa con menor número de ofertas es: " + empresa_menos_ofertas)
    print(tabulate(lt.iterator(lista), headers="keys", tablefmt="grid"))


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    numero_ofertas = int(input("Ingrese el número de ofertas que desea filtrar: "))
    codigo_pais = input("Ingrese el código del país que desea filtrar: ")
    nivel_experiencia = input("Ingrese el nivel de experiencia que desea filtrar: ")
    fecha_inicio = input("Ingrese la fecha de inicio que desea filtrar: ")
    fecha_fin = input("Ingrese la fecha de fin que desea filtrar: ")
    numero_ciudades, numero_empresas, promedio_salario, ciudad_mayor, numero_ciudades_mayor, ciudad_menor, numero_ciudades_menor = controller.req_6(control, codigo_pais, nivel_experiencia, fecha_inicio, fecha_fin)
    lista_n = lt.subList(lista, 1, numero_ofertas)
    print("El numero de ciudades encontradas es: " + str(numero_ciudades))
    print("El numero de empresas encontradas es: " + str(numero_empresas))
    print("El promedio de salario es: " + str(promedio_salario))
    print("La ciudad con mayor número de ofertas es: " + ciudad_mayor + " con " + str(numero_ciudades_mayor) + " ofertas")
    print("La ciudad con menor número de ofertas es: " + ciudad_menor + " con " + str(numero_ciudades_menor) + " ofertas")
    print(tabulate(lt.iterator(lista_n), headers="keys", tablefmt="grid"))
    


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            lista, number_jobs, number_multilocation, number_skills, number_employments = load_data(control)
            print("Se cargaron " + str(number_jobs) + " trabajos")
            print("Se cargaron " + str(number_multilocation) + " multilocalizaciones")
            print("Se cargaron " + str(number_skills) + " habilidades")
            print("Se cargaron " + str(number_employments) + " empleos")
            print("Los primeros y últimos 3 trabajos son: ")
            print(tabulate(lt.iterator(lista), headers="keys", tablefmt="grid"))
            
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
