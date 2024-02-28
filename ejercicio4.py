"""
Cierta empresa requiere una aplicación informática
para administrar los datos de su personal, del
cual se conoce:

- número de DNI
- nombre
- apellido
- año de ingreso.

Existen dos categorías de
empleados:-
- con salario fijo
- a comisión.

Los empleados a comisión tienen
- un salario mínimo,
- un número de clientes captados
- un monto a cobrar por cada cliente captado.
El salario = clientes captados * monto por cliente

Si el salario obtenido por los clientes
captados no llega a cubrir el salario mínimo, cobrará
el salario mínimo.

-----

Los empleados con salario fijo
tienen un sueldo básico y un porcentaje adicional
en función del número de años que llevan la empresa:
• Menos de 2 años: Nada
• De 2 a 5 años: 5% más.
• Más de 5 años: 10% más.

Basado en el enunciado descripto, realizá:

A) El diagrama de clases que lo modelice, con sus relaciones, atributos y métodos.
B) La implementación del método mostrarSalarios que imprima por consola el nombre
completo de cada empleado junto a su salario.
C) La implementación del método empleadoConMasClientes que devuelva al empleado con
mayor cantidad de clientes captados (se supone único).

creen 10 empleados
"""

anio_en_curso = 2024

from enum import Enum

class CatEmpleado(Enum):
    salario_fijo = "Empleado con salario fijo"
    comision = "Empleado por comisión"

class Empleado:
    def __init__(self, DNI, nombre, apellido, anio_ingreso, categoria):
        self.DNI = DNI
        self.nombre = nombre
        self.apellido = apellido
        self.anio_ingreso = anio_ingreso
        self.categoria = categoria

    def mostrarSalario(self):
        pass

class EmpleadoConSueldoFijo(Empleado):
    def __init__(self, DNI, nombre, apellido, anio_ingreso, categoria, sueldo_basico):
        super().__init__(DNI, nombre, apellido, anio_ingreso, categoria)
        self.sueldo_basico = sueldo_basico

    def mostrarSalario(self):
        if anio_en_curso - self.anio_ingreso < 2:
            print(f"El salario del empleado {self.nombre} {self.apellido} es de ${self.sueldo_basico}")
        elif 2 <= anio_en_curso - self.anio_ingreso < 5:
            print(f"El salario del empleado {self.nombre} {self.apellido} es de ${self.sueldo_basico * 1.05}")
        else:
            print(f"El salario del empleado {self.nombre} {self.apellido} es de ${self.sueldo_basico * 1.1}")

class EmpleadoConComision(Empleado):
    def __init__(self, DNI, nombre, apellido, anio_ingreso, categoria, sueldo_min, cant_clientes, monto_por_cliente):
        super().__init__(DNI, nombre, apellido, anio_ingreso, categoria)
        self.sueldo_min = sueldo_min
        self.cant_clientes = cant_clientes
        self.monto_por_cliente = monto_por_cliente

    def mostrarSalario(self):
        salario = self.cant_clientes * self.monto_por_cliente
        if salario > self.sueldo_min:
            print(f"El salario del empleado {self.nombre} {self.apellido} es de ${salario}")
        else:
            print(f"El salario del empleado {self.nombre} {self.apellido} es de ${self.sueldo_min}")


def empleadoConMasClientes(empleados_lst):
    max_clientes = empleados_lst[0].cant_clientes
    emp_con_mas_clientes = empleados_lst[0]
    for e in empleados_lst[1:]:
        if e.cant_clientes > max_clientes:
            max_clientes = e.cant_clientes
            emp_con_mas_clientes = e
    print(f"\nLe empleade con mas clientes es: {emp_con_mas_clientes.nombre} {emp_con_mas_clientes.apellido} y tiene una cuenta con {emp_con_mas_clientes.cant_clientes} clientes")


#test

empleado1 = EmpleadoConSueldoFijo("21.162.121", "Juan", "Pérez", 2013, CatEmpleado.salario_fijo.value, 300000)
empleado2 = EmpleadoConSueldoFijo("24.371.144", "Ricardo", "Diez", 2024, CatEmpleado.salario_fijo.value, 300000)
empleado3 = EmpleadoConSueldoFijo("27.611.311", "Emilio", "Castro", 2000, CatEmpleado.salario_fijo.value, 300000)
empleado4 = EmpleadoConSueldoFijo("26.511.711", "Elsa", "Pallo", 2010, CatEmpleado.salario_fijo.value, 300000)
empleado5 = EmpleadoConSueldoFijo("25.151.181", "Elba", "Lotage", 2020, CatEmpleado.salario_fijo.value, 300000)

empleado6 = EmpleadoConComision("25.150.081", "Rita", "Monti", 2023, CatEmpleado.comision.value, 1000000, 16, 120000)
empleado7 = EmpleadoConComision("35.359.181", "Carlos", "Lupo", 2000, CatEmpleado.comision.value, 1000000, 12, 120000)
empleado8 = EmpleadoConComision("24.153.980", "Javier", "Sanchez", 2003, CatEmpleado.comision.value, 1000000, 10, 120000)
empleado9 = EmpleadoConComision("22.039.188", "Enrico", "Fermi", 2000, CatEmpleado.comision.value, 1000000, 5, 120000)
empleado10 = EmpleadoConComision("20.991.889", "Diego", "Montalbano", 2001, CatEmpleado.comision.value, 1000000, 2, 120000)

lista_empleados_total = [empleado1, empleado2, empleado3 ,empleado4, empleado5, empleado6, empleado7, empleado8, empleado9, empleado10]

for e in lista_empleados_total:
    e.mostrarSalario()

lista_empleados_comision = lista_empleados_total[5:]

empleadoConMasClientes(lista_empleados_comision)

