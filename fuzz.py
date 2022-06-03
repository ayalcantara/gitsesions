import fuzzFor as fuz
import fuzzV3 as fw

def fizzBuzz(x):
    output = ""
    if x % 3 == 0:
        output += "Fizz"
    if x % 5 == 0:
        output += "Buzz"
    if not output:
        output = str(x)
    return(output)
    

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
    #fuz.functionFuz()
    #fw.fuzzWhile()


    """ for i in range(1, 31):
        print(FizzBuzz(i)) """

