def binario(numero):
    return binario_aux(numero,0,0)
def binario_aux(numero,contador,respuesta):
    if numero==0:
        return respuesta
    else:
        return binario_aux(numero//2,contador+1,respuesta+(numero%2)*10**contador)
print (binario(233))