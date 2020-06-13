from bin import binario
def llave(numero):
    return llave_aux(binario(numero))
def llave_aux(numero):
    Lista=[int(x) for x in str(numero)]
    return Lista
#print(llave(55))


def XOR(n):
    if len(n)<8:
        return XOR([0]+n)
    if len(n)==8:
        return [(((n[7]^n[5])^n[3])^n[2])] + n[:-1]
    
#print(XOR(binario))

