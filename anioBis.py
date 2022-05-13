""" def isleap(year):
    leap = False
    a = year / 4
    b = year / 100 
    c = year / 400
 
    if year >= 1899 and year <= 100000:
        if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
            print("ES AÑO BISIESTO")
            leap = True
        else:
            print ("No es año bisiesto")
            leap = False    
    return leap

year = int(input())
isleap(year) """

""" def is_leap(year):
    leap= False
    a=(year / 4) % 2
    b=(year / 100) % 2
    c=(year / 400) % 2
    
    if a == 0 and b == 0 and c == 0:
        print ("Es año bisiesto")
        lead = True
    else:
        print ("No es bisiesto")
        leap = False
    return leap


year = int(input())
print(is_leap(year)) """

def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
             leap = True
    else:
        leap = False

    return leap

year = int(input())
print(is_leap(year))