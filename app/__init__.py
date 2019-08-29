"""
    Project Summit es un programa relacionado con el parque Nacional SUMMIT, mostrando al usuario todos los animales que hay en el parque y su taxonomía.
"""
from app import Listas
import os

def clases(opc):
    """
    Clases es una función que despliega la lista de los 2 tipos de clases de animales que hay en el parque, en este caso Aves y Mamalia
    """
    num = 0
    n=0
    for n in range(24):
         """
        La lista de los animales esta compuesto por: 
        
            :param nombre: Nombre 
            :param clase: Clase
            :param especie: Especie
            :param familia: Familia
            :param genero: Genero
            :param nombre comun: Nombre Común
            :param orden: Orden
            
            :type n: int
            :type c: int
            :type e: int
            :type f: int
            :type g: int
            :type n_c: int
            :type o: int
            """ 
        if opc == 1:
          
            if Listas.clase[n] == 'Aves':
                num = num + 1
                print(str(num) + ".", Listas.nombre[n])
                print(Listas.especies[n])
                print(Listas.familia[n])
                print(Listas.genero[n])
                print(Listas.nombre_comun[n])
                print(Listas.orden[n])

        elif opc == 2:
            if Listas.clase[n] == "Mammalia":
                num = num + 1
                print(str(num) + ".", Listas.nombre[n])
                print(Listas.especies[n])
                print(Listas.familia[n])
                print(Listas.genero[n])
                print(Listas.nombre_comun[n])
                print(Listas.orden[n])

    return num


if __name__ == '__main__':

    print("Menu")
    print("1. Lista de animales")
    print("2. Lista de animales por clases")
    num = 0
    opm = int(input("Introduza una opcion: "))
    if opm == 1:
        n = 0
        for n in range(24):
            num = num + 1
            print(str(num) + ".", Listas.nombre[n])

        op = int(input("Introduzca una opcion: "))
        os.system('cls')
        print(Listas.nombre[op - 1])
        print(Listas.clase[op - 1])
        print(Listas.especies[op - 1])
        print(Listas.familia[op - 1])
        print(Listas.genero[op - 1])
        print(Listas.nombre_comun[op - 1])
        print(Listas.orden[op - 1])

    else:
        os.system('cls')
        print("1.Aves")
        print("2. Mammalia")
        opc = int(input("Introduzca una opcion: "))
        clases(opc)

