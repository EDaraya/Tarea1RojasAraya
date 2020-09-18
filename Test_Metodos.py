# Se importan los métodos
from Metodos import Basic_Ops
from Metodos import Array_Ops

# TESTS PARA METODO 1
a = "ERROR#1: Uno o ambos operandos no son números enteros"
b = "ERROR#2: Uno o ambos operandos no son del rango permitido"
c = "ERROR#3: La operación indicada no es válida"
d = "ERROR#4: los array de entrada no son del mismo tamaño"
# Pruebas de caso de éxito.


def test_suma():
    assert Basic_Ops(2, 2, "suma") == 4


def test_resta():
    assert Basic_Ops(2, 2, "resta") == 0


def test_AND():
    assert Basic_Ops(2, 0, "AND") == 0


def test_OR():
    assert Basic_Ops(2, 0, "OR") == 2


# Prueba: caso de error donde se ingresa un número decimal.

def test_error1():
    assert Basic_Ops(2.5, 3, "suma") == a

# Prueba: caso de error donde se ingresa un número mayor a 127.


def test_error2():
    assert Basic_Ops(130, 3, "suma") == b

# Prueba: caso de error donde se ingresa una operación inválida.


def test_error3():
    assert Basic_Ops(8, 2, "division") == c

# TESTS PARA METODO 2

# Pruebas de caso de éxito.


def test_SumaArray():
    assert Array_Ops([1, 2, 3], [1, 2, 3], "suma") == [2, 4, 6]


def test_RestaArray():
    assert Array_Ops([1, 2, 3], [1, 2, 3], "resta") == [0, 0, 0]


def test_AndArray():
    assert Array_Ops([1, 2, 3], [0, 0, 0], "AND") == [0, 0, 0]


def test_OrArray():
    assert Array_Ops([1, 2, 3], [0, 0, 0], "OR") == [1, 2, 3]


# Prueba: caso de error donde se ingresa un número decimal.

def test_error1Array():
    assert Array_Ops([1.1, 2, 3], [1, 2, 3], "resta") == a

# Prueba: caso de error donde se ingresa un número mayor a 127.


def test_error2Array():
    assert Array_Ops([128, 2, 3], [0, 0, 0], "AND") == b

# Prueba: caso de error donde se ingresa una operación inválida.


def test_error3Array():
    assert Array_Ops([1, 2, 3], [1, 2, 3], "bruno") == c

# Prueba: caso de error donde se ingresan arreglos de diferente tamaño.


def test_error4Array():
    assert Array_Ops([1, 2, 3, 4], [1, 2, 3], "suma") == d
