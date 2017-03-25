#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Header en donde contiene codigo para imprimir texto con "ñ" en UTF-8

print("Impresion de un String") #esto es un string

print(3) #ejemplo de una Literalpri
print("""Podemos escribir lo que sea dentro de """ +
      """tres comillas o dobles comillas\" """)
        
numero1 = 2.3
numero2 = 3

#ejemplo de operaciones aritmeticas

suma = numero1 + numero2
print("La suma es: ")
print(suma)

#uso de format
age = 24
name = "Alexis Abraham Araujo Moreno"

print("tengo {1} años y mi nombre es {0}".format(name, age))

#impresion de decimal con 3 numeros decimales para un float
print("{0:.3f}".format(1.0/3))

#llena de _ con el texto centrado
print("{0:_^13}".format("hello"))

#otro ejemplo
print("{name} wrote {book}".format(name="Swaroop", book="A Byte of python"))






