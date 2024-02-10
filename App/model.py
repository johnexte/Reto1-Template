"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
from datetime import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {"jobs": lt.newList("ARRAY_LIST"),
                    "multilocation": lt.newList("ARRAY_LIST"),
                    "skills": lt.newList("ARRAY_LIST"),
                    "employments": lt.newList("ARRAY_LIST")}
    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data, type):
    """
    Función para agregar nuevos elementos a la lista
    """
    if type == "jobs":
        data["published_at"] = datetime.strptime(data["published_at"], '%Y-%m-%dT%H:%M:%S')
        lt.addLast(data_structs["jobs"], data)
    elif type == "multilocation":
        lt.addLast(data_structs["multilocation"], data) 
    elif type == "skills":
        lt.addLast(data_structs["skills"], data)
    elif type == "employments":
        lt.addLast(data_structs["employments"], data)
    
# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs, type):
    """
    Retorna el tamaño de la lista de datos
    """
    if type == "jobs":
        return lt.size(data_structs["jobs"])
    elif type == "multilocation":
        return lt.size(data_structs["multilocation"])
    elif type == "skills":
        return lt.size(data_structs["skills"])
    elif type == "employments":
        return lt.size(data_structs["employments"])


def req_1(data_structs, codigo_pais, nivel_experiencia):
    """
    Función que soluciona el requerimiento 1
    """
    lista_ofertas = data_structs["jobs"]
    lista_filtrada = lt.newList("ARRAY_LIST")
    for oferta in lt.iterator(lista_ofertas):
        if oferta["country_code"] == codigo_pais and oferta["experience_level"] == nivel_experiencia:
            lt.addLast(lista_filtrada, oferta)
    return lista_filtrada


def req_2(data_structs, nombre_empresa, nombre_ciudad):
    """
    Función que soluciona el requerimiento 2
    """
    lista_ofertas = data_structs["jobs"]
    lista_filtrada = lt.newList("ARRAY_LIST")
    for oferta in lt.iterator(lista_ofertas):
        if oferta["company_name"] == nombre_empresa and oferta["city"] == nombre_ciudad:
            lt.addLast(lista_filtrada, oferta)
    return lista_filtrada


def req_3(data_structs, nombre_empresa, fecha_inicio, fecha_fin):
    """
    Función que soluciona el requerimiento 3
    """
    numero_junior = 0
    numero_mid = 0
    numero_senior = 0
    lista_ofertas = data_structs["employments"]
    lista_filtrada = lt.newList("ARRAY_LIST")
    for oferta in lt.iterator(lista_ofertas):
        if oferta["company_name"] == nombre_empresa:
            fecha_oferta = oferta["published_at"]
            if fecha_oferta >= fecha_inicio and fecha_oferta <= fecha_fin:
                lt.addLast(lista_filtrada, oferta)
                if oferta["experience_level"] == "Junior":
                    numero_junior += 1
                elif oferta["experience_level"] == "Mid":
                    numero_mid += 1
                elif oferta["experience_level"] == "Senior":
                    numero_senior += 1
    return lista_filtrada, numero_junior, numero_mid, numero_senior


def req_4(data_structs, codigo_pais, fecha_inicio, fecha_fin):
    """
    Función que soluciona el requerimiento 4
    """
    ciudades = {}
    empresas = {}
    lista_ofertas = data_structs["jobs"]
    lista_filtrada = lt.newList("ARRAY_LIST")
    for oferta in lt.iterator(lista_ofertas):
        fecha_oferta = oferta["published_at"]
        if fecha_oferta >= fecha_inicio and fecha_oferta <= fecha_fin and oferta["country_code"] == codigo_pais:
            lt.addLast(lista_filtrada, oferta)
            if oferta["city"] in ciudades:
                ciudades[oferta["city"]] += 1 
            else:
                ciudades[oferta["city"]] = 1
                
            if oferta["company_name"] in empresas:
                empresas[oferta["company_name"]] += 1
            else:
                empresas[oferta["company_name"]] = 1
    numero_ciudades = len(ciudades)
    numero_empresas = len(empresas)
    ciudad_mayor_ofertas = max(ciudades, key=ciudades.get)
    ciudad_menor_ofertas = min(ciudades, key=ciudades.get)

    return lista_filtrada, numero_empresas, numero_ciudades, ciudad_mayor_ofertas, ciudad_menor_ofertas


def req_5(data_structs, nombre_ciuadad, fecha_inicio, fecha_fin):
    """
    Función que soluciona el requerimiento 5
    """
    empresas = {}
    lista_ofertas = data_structs["jobs"]
    lista_filtrada = lt.newList("ARRAY_LIST")
    for oferta in lt.iterator(lista_ofertas):
        fecha_oferta = oferta["published_at"]
        if fecha_oferta >= fecha_inicio and fecha_oferta <= fecha_fin and oferta["city"] == nombre_ciuadad:
            lt.addLast(lista_filtrada, oferta)
            if oferta["company_name"] in empresas:
                empresas[oferta["company_name"]] += 1
            else:
                empresas[oferta["company_name"]] = 1
    numero_empresas = len(empresas)
    empresa_mas_ofertas = max(empresas, key=empresas.get)
    empresa_menos_ofertas = min(empresas, key=empresas.get)
    return lista_filtrada, numero_empresas, empresa_mas_ofertas, empresa_menos_ofertas


def req_6(data_structs, codigo_pais, nivel_experiencia, fecha_inicio, fecha_fin):
    """
    Función que soluciona el requerimiento 6
    """
    ciudades = {}
    empresas = {}
    salario_total = 0
    numero_ofertas = 0
    lista_ofertas = data_structs["jobs"]
    lista_filtrada = lt.newList("ARRAY_LIST")
    for oferta in lt.iterator(lista_ofertas):
        fecha_oferta = oferta["published_at"]
        if fecha_oferta >= fecha_inicio and fecha_oferta <= fecha_fin and oferta["country_code"] == codigo_pais and oferta["experience_level"] == nivel_experiencia:
            lt.addLast(lista_filtrada, oferta)
            numero_ofertas += 1
            salario_total += calcular_salario(oferta["id"],data_structs["employments"])
            if oferta["city"] in ciudades:
                ciudades[oferta["city"]] += 1 
            else:
                ciudades[oferta["city"]] = 1
                
            if oferta["company_name"] in empresas:
                empresas[oferta["company_name"]] += 1
            else:
                empresas[oferta["company_name"]] = 1
    numero_ciudades = len(ciudades)
    numero_empresas = len(empresas)
    promedio_salario = salario_total/numero_ofertas
    ciudad_mayor = max(ciudades, key=ciudades.get)
    numero_ciudades_mayor = ciudades[ciudad_mayor]
    ciudad_menor = min(ciudades, key=ciudades.get)
    numero_ciudades_menor = ciudades[ciudad_menor]
    return numero_ciudades, numero_empresas, promedio_salario, ciudad_mayor, numero_ciudades_mayor, ciudad_menor, numero_ciudades_menor

def calcular_salario(id, lista_empleos):
    for empleo in lt.iterator(lista_empleos):
        if empleo["id"] == id:
            salary_from = empleo["salary_from"]
            salary_to = empleo["salary_to"]
            if salary_from == 0 and salary_to == 0:
                return 0
            elif salary_from == 0:
                return salary_to
            elif salary_to == 0:
                return salary_from
            else:
                return (salary_from + salary_to)/2
    
def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria_jobs(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    return data_1["published_at"] > data_2["published_at"]

def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    merge = merg.sort(data_structs["jobs"], sort_criteria_jobs)
