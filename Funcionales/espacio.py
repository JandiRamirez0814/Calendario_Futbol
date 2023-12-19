#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Jandi Ramirez, Paula Lemus, Camilo Viedma
# Creation date: 2023-12-01
# Edition date: 2023-12-18

# Description: Programa para medir el uso de memoria de generar_calendario por algoritmo y por sol_ingenua.


import random
import os
import psutil

from calendario import generar_calendario
from sol_ingenua import generar_calendario as generar_calendario2

def generar_matriz_aleatoria(n):
    """ 
    Función para generar una matriz aleatoria de tamaño n x n
    con valores entre 1 y 1000.
    
    :param n: tamaño de la matriz
    :return: matriz aleatoria de tamaño n x n
    """
    return [[random.randint(1, 1000) for _ in range(n)] for _ in range(n)]

def medir_memoria1(n_equipos):
    """ 
    Función para medir el uso de memoria de generar_calendario por algoritmo
    
    :param n_equipos: tamaño de la matriz
    :return: uso de memoria promedio en kilobytes
    :param distancias: matriz de distancias
    :type distancias: list
    :param memoria_antes: memoria antes de llamar a la función
    :type memoria_antes: int
    :param memoria_despues: memoria después de llamar a la función
    :type memoria_despues: int
    :param memoria_total: memoria total
    :type memoria_total: int
    """
    
    distancias = generar_matriz_aleatoria(n_equipos)

    # Medir el uso de memoria antes de llamar a la función
    memoria_antes = psutil.Process(os.getpid()).memory_info().rss / 1024  # en kilobytes

    # Llamar a la función para generar_calendario
    generar_calendario(n_equipos, 1, n_equipos-1, distancias)

    # Medir el uso de memoria después de llamar a la función
    memoria_despues = psutil.Process(os.getpid()).memory_info().rss / 1024  # en kilobytes

    # Acumular la memoria después de llamar a la función
    memoria_total = memoria_despues - memoria_antes

    # Imprimir con 8 decimales
    return f"Uso de memoria promedio: {memoria_total:.8f} kilobytes"

def medir_memoria2(n_equipos):
    """ 
    Función para medir el uso de memoria de generar_calendario por sol_ingenua
    
    :param n_equipos: tamaño de la matriz
    :return: uso de memoria promedio en kilobytes
    :param distancias: matriz de distancias
    :type distancias: list
    :param memoria_antes: memoria antes de llamar a la función
    :type memoria_antes: int
    :param memoria_despues: memoria después de llamar a la función
    :type memoria_despues: int
    :param memoria_total: memoria total
    :type memoria_total: int
    """
    
    distancias = generar_matriz_aleatoria(n_equipos)

    # Medir el uso de memoria antes de llamar a la función
    memoria_antes = psutil.Process(os.getpid()).memory_info().rss / 1024  # en kilobytes

    # Llamar a la función para generar_calendario
    generar_calendario2(n_equipos, 1, n_equipos-1, distancias)

    # Medir el uso de memoria después de llamar a la función
    memoria_despues = psutil.Process(os.getpid()).memory_info().rss / 1024  # en kilobytes

    # Acumular la memoria después de llamar a la función
    memoria_total = memoria_despues - memoria_antes

    # Imprimir con 8 decimales
    return f"Uso de memoria promedio: {memoria_total:.8f} kilobytes"

    
if __name__=="__main__":
    # Ejecutar pruebas para diferentes tamaños de matriz
    tamanos_matrices = [4, 6, 8, 10, 12, 14, 18, 20, 30, 36]
    """ 
    Función para medir el uso de memoria de generar_calendario por algoritmo y por sol_ingenua.
    
    :var memoria_promedio: memoria promedio
    :type memoria_promedio: str
    :param z: tamaño de la matriz
    :type z: int
    :param i: contador
    :type i: int
    :param tamanos_matrices: lista de tamaños de matrices
    :type tamanos_matrices: list
    """

    print("Espacio por Algoritmo calendario\n")

    for z in tamanos_matrices:
        for i in range (0,10):
            memoria_promedio = medir_memoria1(z)
            print(f"Número de equipos: {z}, {memoria_promedio}")
        print("----------------------------------------------------")
        print("----------------------------------------------------")
    
    print("Espacio por Algoritmo sol_ingenua\n")
    for z in tamanos_matrices:
        for i in range (0,10):
            memoria_promedio = medir_memoria2(z)
            print(f"Número de equipos: {z}, {memoria_promedio}")
        print("----------------------------------------------------")
        print("----------------------------------------------------")