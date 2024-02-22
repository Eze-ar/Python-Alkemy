"""
Crear una clase llamada Animal, otra llamada Perro y otra llamada Águila.
La clase Animal tiene:
    atributo cantidad_patas: numérico
    atributo tipo: vertebrado/invertebrado
    método comer(): retorna un string "estoy comiendo"

La clase Perro hereda de Animal y agrega:
    atributo nombre: texto
    atributo raza: texto
    método correr(): retorna un string "estoy corriendo"

La clase Aguila hereda de Animal y agrega:
    método volar(): retorna un string "estoy volando"

Guardarlo en un archivo llamado ejercicio2.py
"""

from enum import Enum

class Tipo(Enum):
    V = "vertebrado"
    I = "invertebrado"

class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo

    def comer(self):
        return "estoy comiendo"

class Perro(Animal):
    def __init__(self, cantidad_patas, tipo, nombre, raza):
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza

class Aguila(Animal):
    def __init__(self, cantidad_patas, tipo):
        super().__init__(cantidad_patas, tipo)

    def volar(self):
        return "estoy volando"


#para testear
animal = Animal(8, Tipo.I.value)
print(f"{animal.cantidad_patas} patas y tipo: {animal.tipo}")
print(animal.comer())

perro = Perro(4,Tipo.V.value, "Picho", "mestizo")
print(f"\n{perro.cantidad_patas} patas, tipo: {perro.tipo}, nombre: {perro.nombre} y raza: {perro.raza}")

aguila = Aguila(2, Tipo.V.value)
print(f"\n{aguila.cantidad_patas} patas y tipo: {aguila.tipo}")
print(aguila.volar())
