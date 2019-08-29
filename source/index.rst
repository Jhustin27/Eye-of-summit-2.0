.. summit proyect documentation master file, created by
   sphinx-quickstart on Tue Aug 20 11:11:29 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bienvenido a la documentacion del Proyecto Eye of Summit!
=========================================================

.. image:: _static/LOGO.jpeg
   :align: center
   :alt: LOGO


**Eyes of Summit** es un programa relacionado con el Parque Nacional Summit, mostrando
al usuario todos los animales que estan dentro del Parque con su respectiva
taxonomia.

El programa cuenta con una Documentacion y un Unit Test.

Una funcion principal que es:

- Clases
   def clases(opc):
    num=0
   for n in range(24):
      if opc == 1:
            if Listas.clase[n]=='Aves':

            num = num+1

            print(str(num) +".", Listas.nombre[n])

            print(Listas.especies[n])
            print(Listas.familia[n])

            print(Listas.genero[n])
            print(Listas.nombre_comun[n])
            print(Listas.orden[n])

        elif opc == 2:
            if Listas.clase[n]== "Mammalia" :
                num = num + 1

                print(str(num) + ".", Listas.nombre[n])

                print(Listas.especies[n])
                print(Listas.familia[n])

                print(Listas.genero[n])
                print(Listas.nombre_comun[n])
                print(Listas.orden[n])

.. toctree::
   :maxdepth: 2
   :caption: Contents:
.. automodule:: app
    :members:

:Autor: Jhustin Martinez, Francisco Deras, Eduardo Paris, Wilfredo Whitaker, Juan Samudio, Carlos Albendras


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
