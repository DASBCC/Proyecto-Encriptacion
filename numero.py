def num_bin(x):
    return num_bin_aux(x,0,0)
def num_bin_aux(x,respuesta,cont):
    if len(x)==1:
        return respuesta+(x[0]*(10**cont))
    else:
        return num_bin_aux(x[0:len(x)-1],respuesta+x[-1]*(10**cont),cont+1)
print(num_bin([1,0,0,1,0]))