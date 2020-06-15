from Llave import llave
def decode(letra,num):
    return decode_aux(letra,llave(num),0)
def decode_aux(letra,num,pos):
    A1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    A2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    rotar(A2,num)
    if letra==A1[pos]:
        return A2[pos]
    else:
        return decode_aux(letra,num,pos+1)

def rotar(lista,repeticiones):
    rep=0
    while (rep!=repeticiones):
        temp=lista[1]
        lista[1]=lista[0]
        lista=rotar_aux(lista,1,temp)
        rep+1
    return lista
def rotar_aux(lista,pos,anterior):
    if pos==len(lista)-1:
        lista[0]=(anterior)
        return lista
    else:
        temp=lista[pos+1]
        lista[pos+1]=(anterior)
        return rotar_aux(lista,pos+1,temp)

print(decode("k",230))