# ERRORES
# 1) En caso de que los operandos no sean enteros
# 2) En caso de que los operandos no sean del rango permitido
# 2) En caso de que la op no exista
# 3) En caso de que los Array de entrada no sean del mismo tamaño

# METODO 1
def Basic_Ops(a, b, op):
    # Lista de operaciones que tendrá la función.
    Ops = ["suma", "resta", "AND", "OR"]
    # Si estas variables mantienen la condición False, significa que hay un
    # error en los parámetros indicados en la función.
    enteros = False
    rangoA = rangoB = False
    if (type(a) == int) and (type(b) == int):
        enteros = True
        if (a >= -127) and (a <= 127):
            rangoA = True
        if (b >= -127) and (b <= 127):
            rangoB = True
    # Si todas estas variables son verderas, entonces se prosigue a realizar
    # la operación seleccionada.
    x = enteros and rangoA and rangoB
    if x is True:
        # Se verifica que la operación seleccionada esté dentro de la lista
        # de operaciones definida anteriormente.
        if op in Ops:
            if op == "suma":
                y = a + b
            if op == "resta":
                y = a - b
            if op == "AND":
                y = a & b
            if op == "OR":
                y = a | b
            return y
        else:
            return "ERROR#3: La operación indicada no es válida"

    else:
        if enteros is False:
            return "ERROR#1: Uno o ambos operandos no son números enteros"
        else:
            return "ERROR#2: Uno o ambos operandos no son del rango permitido"
# METODO 2


def Array_Ops(A1, A2, op):
    a = len(A1)
    b = len(A2)
    result = []
    # Se verifica que ambos arreglos sean del mismo tamaño.
    if a == b:
        # Se recorre cada elemento de los arreglos, con el fin de realizar
        # la operacion con cada uno.
        for i in range(0, a):
            y = Basic_Ops(A1[i], A2[i], op)
            if (type(y) == int):
                result.append(Basic_Ops(A1[i], A2[i], op))
            else:
                return y
            i = i + 1
        return result
    else:
        return "ERROR#4: los array de entrada no son del mismo tamaño"
