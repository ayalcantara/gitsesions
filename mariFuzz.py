def fizbuzz (n):
    if   n > 0 and n < 200000:
        multiplo = 0
        multiplo2 = 0
        bol = False
        bol2 = False
            
        while multiplo   <= lista[i]:
            multiplo=multiplo+3
            if multiplo == lista[i]:
                bol = True
               
        while multiplo2 <= lista[i]:
             multiplo2=multiplo2+5
             
             if multiplo2== lista[i]:
                bol2 = True
                
                if bol == True and bol2 == True:
                    print (lista[i])
                    print ("Es multiplo de 3 y 5______fizzbuzz")
                    return None
                
                elif bol == True and bol2== False:
                    print(lista[i])
                    print("Es multiplo de 3 ______fizzz")
                    print("No es multiplo de 5______")
                    return None

                elif bol== False and bol2== True:
                    print(lista[i])
                    print("Es multiplo de 5 ______buzz")
                    print("No es multiplo de 3______")
                    return None
           
                elif bol == False and bol2 == False:
                    print(lista [i])
                    print("No es multiplo de 3 y 5")
                    return None        
    else:
        print ("El numero no se encuentra dentro del rango")
        return None
    

lista=[]
menu = 'y'
multiplo = 0
multiplo2 = 0
bol = False
bol2 = False
    
while  menu == 'y' :
    print ("---------------------------------------------------- ")
    print(" MENU")
    print ("1.-Agregar datos")
    print("2.- Borrar datos")
    print("3.- Borrar tabla")
    print("4.- Imprimir tabla")
    print("5.- Buscar multiplos")
    print("0.- Salir del programa")
    opcion=int(input("Escribe el numero de la opcion a elergir: "))

    if opcion == 1:
        regresar = 'y' 
        while regresar == 'y' :
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
        print ("MULTIPLOS")
        for i in range (len(lista )):
            fizbuzz(lista[i])

    else:
        print ("BYE")
        break

        
menu = 'n'  
menu=input("Regresar al menu principal? y/n: ")