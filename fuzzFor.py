def functionFuz():
    #for (num=1; num <200000; num++) for en C++
    for num in range(1,101):
        output = ""
        if num % 3 == 0:
            output = output + "Fizz"
        if num % 4 == 0:
            output = output + "Buzz"
        if num % 4 != 0 and num % 3 != 0:
            output = output + str(num)
        print(output)
    
    

