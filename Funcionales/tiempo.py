#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Jandi Ramirez, Paula Lemus, Camilo Viedma
# Creation date: 2023-12-01
# Edition date: 2023-12-18

# Description: Programa para medir el tiempo de ejecución de generar_calendario por algoritmo y por sol_ingenua.


import time
import random

from calendario import generar_calendario
from sol_ingenua import generar_calendario as generar_calendario2

def generar_matriz_aleatoria(n):
    """ 
    Función para generar una matriz aleatoria de tamaño n x n
    con valores entre 1 y 1000.
    
    :param n: tamaño de la matriz
    :return: matriz aleatoria de tamaño n x n
    :rtype: list"""
    return [[random.randint(1, 1000) for _ in range(n)] for _ in range(n)]

# Función para medir el tiempo de ejecución de generar_calendario por algoritmo
def medir_tiempo1(n_equipos, num_pruebas):
    """ 
    Función para medir el tiempo de ejecución de generar_calendario por algoritmo
    
    :param n_equipos: tamaño de la matriz
    :return: tiempo promedio de ejecución en segundos
    :rtype: float
    :param tiempos: lista de tiempos de ejecución
    :type tiempos: list
    :param distancias: matriz de distancias
    :type distancias: list
    :param start_time: tiempo de inicio
    :type start_time: float
    :param elapsed_time: tiempo de ejecución
    :type elapsed_time: float
    :param tiempo_promedio: tiempo promedio de ejecución
    :type tiempo_promedio: float
    """
    tiempos = []

    for _ in range(num_pruebas):
        distancias = generar_matriz_aleatoria(n_equipos)

        start_time = time.time()
        generar_calendario(n_equipos, 1, n_equipos-1, distancias)
        elapsed_time = time.time() - start_time
        tiempos.append(elapsed_time)

    tiempo_promedio = sum(tiempos) / num_pruebas
    return tiempo_promedio

# Función para medir el tiempo de ejecución de generar_calendario por sol_ingenua
def medir_tiempo2(n_equipos, num_pruebas):
    """ 
    Función para medir el tiempo de ejecución de generar_calendario por sol_ingenua
    
    :param n_equipos: tamaño de la matriz
    :return: tiempo promedio de ejecución en segundos
    :rtype: float
    :param tiempos: lista de tiempos de ejecución
    :type tiempos: list
    :param distancias: matriz de distancias
    :type distancias: list
    :param start_time: tiempo de inicio
    :type start_time: float
    :param elapsed_time: tiempo de ejecución
    :type elapsed_time: float
    :param tiempo_promedio: tiempo promedio de ejecución
    :type tiempo_promedio: float
    """
    tiempos = []

    for _ in range(num_pruebas):
        distancias = generar_matriz_aleatoria(n_equipos)

        start_time = time.time()
        generar_calendario2(n_equipos, 1, n_equipos-1, distancias)
        elapsed_time = time.time() - start_time
        tiempos.append(elapsed_time)

    tiempo_promedio = sum(tiempos) / num_pruebas
    return tiempo_promedio

    
if __name__ == "__main__":
    """ 
    Función para medir el tiempo de ejecución de generar_calendario por algoritmo y por sol_ingenua
    
    :param n_equipos: tamaño de la matriz
    :return: tiempo promedio de ejecución en segundos
    :rtype: float
    :param tamano_matrices: lista de tamaños de matrices
    :type tamano_matrices: list
    :param tiempo_promedio: tiempo promedio de ejecución
    :type tiempo_promedio: float
    :param n_equipos: tamaño de la matriz
    :type n_equipos: int
    :param num_pruebas: número de pruebas
    :type num_pruebas: int
    """
    
    # Ejecutar pruebas para diferentes tamaños de matriz
    tamanos_matrices = [4, 6, 8, 10, 12, 14, 16, 18, 20,30,36]

    print("Cantidad de pruebas por cantidad de equipos: 1000\n")
    print("Tiempo por Algoritmo calendario\n")
    for n_equipos in tamanos_matrices:
        tiempo_promedio = medir_tiempo1(n_equipos, num_pruebas=1000)
        print(f"Número de equipos: {n_equipos}, Tiempo promedio de ejecución: {tiempo_promedio:.8f} segundos")
    
    
    print("\nCantidad de pruebas por cantidad de equipos: 1000\n")
    print("Tiempo por Solucion ingenua\n")
    for n_equipos in tamanos_matrices:
        tiempo_promedio = medir_tiempo2(n_equipos, num_pruebas=1000)
        print(f"Número de equipos: {n_equipos}, Tiempo promedio de ejecución: {tiempo_promedio:.8f} segundos")