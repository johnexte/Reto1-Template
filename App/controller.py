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
 """

import config as cf
import model
import time
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    return model.new_data_structs()


# Funciones para la carga de datos

def load_data(control, prefix):
    """
    Carga los datos del reto
    """
    number_jobs = load_jobs(control, prefix)
    number_multilocation = load_multilocation(control, prefix)
    number_skills = load_skills(control, prefix)
    number_employments = load_employments(control, prefix)
    return number_jobs, number_multilocation, number_skills, number_employments

def load_jobs(control, prefix):
    """
    Carga los datos de los trabajos
    """
    file_name = prefix + '-jobs.csv'
    input_file = csv.DictReader(open(file_name, encoding='utf-8'))
    for job in input_file:
        model.add_data(control, job, 'jobs')
    sort(control["jobs"])
    return model.data_size(control, 'jobs')

def load_multilocation(control, prefix):
    """
    Carga los datos de los trabajos
    """
    file_name = prefix + '-multilocation.csv'
    input_file = csv.DictReader(open(file_name, encoding='utf-8'))
    for multilocation in input_file:
        model.add_data(control, multilocation, 'multilocation')
    return model.data_size(control, 'multilocation')

def load_skills(control, prefix):
    """
    Carga los datos de los trabajos
    """
    file_name = prefix + '-skills.csv'
    input_file = csv.DictReader(open(file_name, encoding='utf-8'))
    for skill in input_file:
        model.add_data(control, skill, 'skills')
    return model.data_size(control, 'skills')

def load_employments(control, prefix):
    """
    Carga los datos de los trabajos
    """
    file_name = prefix + '-employments.csv'
    input_file = csv.DictReader(open(file_name, encoding='utf-8'))
    for employment in input_file:
        model.add_data(control, employment, 'employments')
    return model.data_size(control, 'employments')
    
# Funciones de ordenamiento

def sort(lista):
    """
    Ordena los datos del modelo
    """
    model.sort(lista)


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, codigo_pais, nivel_experiencia):
    """
    Retorna el resultado del requerimiento 1
    """
    return model.req_1(control, codigo_pais, nivel_experiencia)


def req_2(control, nombre_empresa, nombre_ciudad):
    """
    Retorna el resultado del requerimiento 2
    """
    return model.req_2(control, nombre_empresa, nombre_ciudad)


def req_3(control, nombre_empresa, fecha_inicio, fecha_fin):
    """
    Retorna el resultado del requerimiento 3
    """
    return model.req_3(control, nombre_empresa, fecha_inicio, fecha_fin)


def req_4(control, codigo_pais, fecha_inicio, fecha_fin):
    """
    Retorna el resultado del requerimiento 4
    """
    return model.req_4(control, codigo_pais, fecha_inicio, fecha_fin)


def req_5(control, nombre_ciuadad, fecha_inicio, fecha_fin):
    """
    Retorna el resultado del requerimiento 5
    """
    return model.req_5(control, nombre_ciuadad, fecha_inicio, fecha_fin)

def req_6(control, codigo_pais, nivel_experiencia, fecha_inicio, fecha_fin):
    """
    Retorna el resultado del requerimiento 6
    """
    return model.req_6(control, codigo_pais, nivel_experiencia, fecha_inicio, fecha_fin)


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
