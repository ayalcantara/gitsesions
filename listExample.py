list = [1,1,2,2,3,3,4,4,5,5,6,6]
newList = []

print("List with duplicates numbers")
print(list)

for i in list:
    if i not in newList: #comparacion
        newList.append(i) #ubica los primeros numeros, no los duplicados
newList #se puede imprimir la nueva lista
list = newList #o actualizar la lista con duplicados

print("Drop duplicates numbers:")
print(list)