def functionFuz():
    #for (n=1; n <200000; n++) for en C++
    for n in range(1,101):
        output = ""
        if n % 3 == 0:
            output = output + "Fizz"
        if n % 4 == 0:
            output = output + "Buzz"
        if n % 4 != 0 and n % 3 != 0:
            output = output + str(n)
        print(output)
    
    

