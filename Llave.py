from bin import binario
def llave(numero):
    return llave_aux(binario(numero))
def llave_aux(numero):
    Lista=[int(x) for x in str(numero)]
    return Lista
print(llave(2))