from numero import num_bin
from bin import binario
def llave(numero):
    return llave_aux(binario(numero))
def llave_aux(numero):
    Lista=[int(x) for x in str(numero)]
    return XOR(Lista)

def XOR(n):
    if len(n)<8:
        return XOR([0]+n)
    if len(n)==8:
        return num_bin([(((n[7]^n[5])^n[3])^n[2])] + n[:-1])