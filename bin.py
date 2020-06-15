def binario(numero):
    return binario_aux(numero,0,0)
def binario_aux(numero,contador,respuesta):
    if numero==0:
        return respuesta
    else:
        return binario_aux(numero//2,contador+1,respuesta+(numero%2)*10**contador)

def CD(a):
    if a<10:
        return 1
    else:
        return 1 + CD(a//10)

def Decimal(n):
    if n<10:
        return n 
    else:
        return (n//10**(CD(n)-1))* 2 ** (CD(n)-1) + Decimal(n%10**(CD(n)-1))