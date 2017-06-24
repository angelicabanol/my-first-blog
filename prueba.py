def pruebaordenar(nombre, tamano):
    print("Hola " + nombre + ", vamos a ordenar una lista!")
    listanum = []
    for i in range(0,int(tamano)): 
         print('Ingrese num' + str(i) )
         numero = input()
         listanum.append(numero)
         listanum.sort()
    
    if listanum[0] < listanum[int(tamano)-1]:
        print("Lista ordenada")
        print(listanum)
    else :
        print("Algo fallo =( ")
        print(listanum)

print("Ingresa tu nombre")
nomb = input()
print("Ingresa el tamaño de tu lista")
tam = input()
pruebaordenar(nomb,tam)