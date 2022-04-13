
def fuzzWhile():
    i = 1
    while i >= 1 and i < 199999:
        if (i % 15) == 0:
            print ("fizzbuzz\n", end=' ')
            i = i + 1
        elif (i % 5) == 0:
            print ("buzz", end=' ')
            i = i + 1
        elif (i % 3) == 0:
            print ("fizz", end=' ')
            i = i + 1
        else:
            i = i + 1
            print (i, end=' ')