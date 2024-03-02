"""
Una fábrica de instrumentos musicales posee una lista con todas sus sucursales.
Cada sucursal tiene su nombre y una lista con todos los instrumentos a la venta.
De cada uno de ellos se sabe su ID alfanumérico, su precio y su tipo    <----agregué nombre
(Percusión, Viento o Cuerda).

Puntos a desarrollar
1)Desarrollar el diagrama de clases UML que modele lo enunciado y donde consten
las clases con sus atributos, métodos y relaciones (los constructores pueden omitirse).

2) Crear un proyecto en Python que resuelva:
    A) método listarInstrumentos que muestre en la consola todos los
    datos de cada uno de los instrumentos. - DEVOLVEME TODOS LOS INSTRUMENTOS
    B) método instrumentosPorTipo que devuelva una lista de
    instrumentos cuyo tipo coincida con el recibido por parámetro. ... DE CUERDAS (FILTRO)
    C) método borrarInstrumento que reciba un ID y elimine el
    instrumento asociado a tal ID de la sucursal donde se encuentre.
    ***bueno esto puedo interpretar como donde se encuentre el ID hablando de TODAS las sucursales o lo que terminé
    haciendo que es en la sucursal en que se encuentre entendiendo en la cual se ejecuta el método***
    D) método porcInstrumentosPorTipo que reciba el nombre de una
    sucursal y retorne los porcentajes de instrumentos por tipo que hay para tal sucursal.
"""

from enum import Enum

class Instrumento:
    def __init__(self, ID, nombre, precio, tipo):
        self.ID = ID
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo

class TipoInstrumento(Enum):
    P = 'Percusión'
    V = 'Viento'
    C = 'Cuerda'

class Fabrica:
    def __init__(self):
        self.__sucursales_lst = []

    def agregarSucursal(self, sucursal):
        self.__sucursales_lst.append(sucursal)

    def listarInstrumentos(self):
        print("Listado de instrumentos por sucursal:\n")
        for sucursal in self.__sucursales_lst:
            print(f'Sucursal {sucursal.nombre}:')
            for instrumento in sucursal.instrumentos_lst:
                print(f'ID:{instrumento.ID} "{instrumento.nombre}" ({instrumento.tipo}) ${instrumento.precio}')
            print()

    def instrumentosPorTipo(self, tipo):
        instrumentos_de_x_tipo_lst = []
        for sucursal in self.__sucursales_lst:
            for instrumento in sucursal.instrumentos_lst:
                if tipo == instrumento.tipo:
                    instrumentos_de_x_tipo_lst.append(instrumento)
        return instrumentos_de_x_tipo_lst

    '''
    def borrarInstrumento(self):
        pass    # debo definir en sucursal
    '''

    def porcInstrumentosPorTipo(self, nombreSucursal):
        encontrado = False
        for sucursal in self.__sucursales_lst:
            if nombreSucursal == sucursal.nombre:
                encontrado = True
                totalInstrumentos = len(sucursal.instrumentos_lst)
                for tipo in TipoInstrumento:
                    cantidad = 0
                    for instrumento in sucursal.instrumentos_lst:
                        if tipo.value == instrumento.tipo:
                            cantidad += 1
                    print(f'Hay {round(cantidad/totalInstrumentos*100, 2)}% de instrumentos de tipo {tipo.value}')
                print()
        if not encontrado:
            print(f'ERROR: No se encontró la sucursal {nombreSucursal} en la lista!')

class Sucursal(Fabrica):
    def __init__(self, nombre):
        super().__init__()           # llamo al método __init__() de la clase padre (constructor en otros lenguajes)
        self.nombre = nombre
        self.instrumentos_lst = []   # no lo puedo hacer privado ya que lo accedo de la clase padre

    def agregarInstrumento(self, instrumento):
        self.instrumentos_lst.append(instrumento)

    def listarInstrumentos(self):
        print(f"Listado de instrumentos de sucursal {self.nombre}:")
        for instrumento in self.instrumentos_lst:
            print(f'ID:{instrumento.ID} "{instrumento.nombre}" ({instrumento.tipo}) ${instrumento.precio}')
        print()

    def borrarInstrumento(self, ID):
        borrado = False
        print(f'\nIntentando borrar ID:{ID}...')
        for instrumento in self.instrumentos_lst:
            if ID == instrumento.ID:
                self.instrumentos_lst.remove(instrumento)
                print(f'Borrado de {ID} "{instrumento.nombre}" EXITOSO!')
                borrado = True
        if not borrado:
            print(f"No se encontró el ID:{ID}, borrado FALLIDO!")
        print()


# Test
violin = Instrumento('v001', 'Violín', 134000.99, TipoInstrumento.C.value)
flauta = Instrumento('f001', 'Flauta Dulce', 57000.00, TipoInstrumento.V.value)
tambor = Instrumento('t001', 'Tambor Legüero', 86500.00, TipoInstrumento.P.value)

sucursal1 = Sucursal('Florencio Varela')
sucursal1.agregarInstrumento(violin)

sucursal2 = Sucursal('Sarandí')
sucursal2.agregarInstrumento(flauta)

sucursal3 = Sucursal('Roque Pérez')
sucursal3.agregarInstrumento(tambor)
sucursal3.agregarInstrumento(violin)
sucursal3.agregarInstrumento(flauta)

fabrica = Fabrica()
fabrica.agregarSucursal(sucursal1)
fabrica.agregarSucursal(sucursal2)
fabrica.agregarSucursal(sucursal3)

fabrica.listarInstrumentos()

filtro_tipo = TipoInstrumento.C.value  # Suponiendo filtro por tipo "Cuerda"
instrumentos_de_x_tipo_lst = fabrica.instrumentosPorTipo(filtro_tipo)
print(f'Listado de instrumentos de tipo "{filtro_tipo}":')
for instrumento in instrumentos_de_x_tipo_lst:
    print(f'ID:{instrumento.ID} "{instrumento.nombre}" ${instrumento.precio}')

sucursal1.borrarInstrumento('v011')  # <--trato de borrar ID inexistente
sucursal1.listarInstrumentos()

sucursal1.borrarInstrumento('v001')
sucursal1.listarInstrumentos()

fabrica.porcInstrumentosPorTipo("Roque Pérez")
fabrica.porcInstrumentosPorTipo("Villa Lynch")
