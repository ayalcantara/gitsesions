
if __name__ == '__main__':
    final = []
    diccionario = {}
    cal = []
    suma = 0
    
    N = 0
    for _ in range(int(input())):
        name = input()
        score =float (input())
        
        diccionario.update({name : score})
        N = N + 1
        cal.append (score)
        
    if N >= 2 and N <=5:
        for j in range (len(cal)-1):
            for i in range (len(cal)-1):
                if cal[i]  > cal [i + 1]:
                    cal [i], cal [i+1] = cal [i + 1], cal [i]
                
    cal = list (set(cal))
    valor = cal [1] 
     
    valores = diccionario.values()
    llaves = diccionario.keys()
    
    for m in range (len (valores)-1):
        if valor == valores[m]:
            final.append(llaves[m])
        
    final.sort()        
   
    for m in range(len(final)):
        print (final[m])