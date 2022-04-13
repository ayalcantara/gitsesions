lista=[] #Creamos una lista
menu = ' s'
multiplo = 0
multiplo2 = 0
bol = False
bol2 = False

while  menu == ' s' :
    print("MENU")
    print ("1.-Agregar datos")
    print("2.- Borrar datos")
    print("3.-Borrar tabla")
    print("4.- Imprimir tabla")
    print("5.- Buscar multiplos")
    opcion=int(input("Escribe el numero de la opcion a elergir: "))

    if opcion ==1:
        regresar =  ' s' 
        while regresar==  ' s' :
            print ("AGREGAR DATOS A LA TABLA")
            cantidad=int(input("Cuantos datos agregaras a la tabla?: "))
            for i in range(cantidad):
                agregar=int(input("Dame el valor: " ))
                lista.append(agregar)
            regresar=input("Deseas agregar mas datos? s/n: " )

    if opcion ==2:
        print("BORRAR DATOS")
        print(lista)
        borrar=int(input("Escribe el lugar de valor que deseas borrar: "))
        del lista[borrar-1]

    elif opcion == 3:
        del lista
        lista=[]
        print("La lista esta vacia.")

    elif opcion == 4:
        print(lista)

    elif opcion == 5:

        #multiplo de 3 
        for i in range (len(lista )):
            
            while multiplo <= lista[i]:
                multiplo=multiplo+3
                if multiplo == lista[i]:
                    print (multiplo)
                    print("Es multiplo de 3")
                    bol = True

            while multiplo2 <= lista[i]:
                multiplo2=multiplo2+5
                if multiplo2== lista[i]:
                    print (multiplo2)
                    print("Es multiplo de 5")
                    bol2 = True

            if bol == True and bol2 == True:
                print (lista[i])
                print ("Es multiplo de 3 y 5")

            else:
                 break
  

        
menu = ' no'  
menu=input("Regresar al menu principal? si/no: ")