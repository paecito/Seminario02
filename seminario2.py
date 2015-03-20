fich = open("pokemon.txt",'r').read()
lista= fich.split(" ")
    
listaAux1 = []
listaAux2 = []

for i in range(len(lista)) :
    elemento = lista[i] 
    listaAux1.append(elemento)
    j=0
    for j in range(len(lista)):
        if lista[j][0] == listaAux1[-1][-1] and not lista[j] in listaAux1 :
            listaAux1.append(lista[j])
            j=0
                    
    if len(listaAux1) > len(listaAux2):
        del listaAux2[:]
        listaAux2=listaAux1[:]
        
    del listaAux1[:]

print "La lista mas larga es:"
print listaAux2
