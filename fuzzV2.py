print(*map(lambda i: 'Fizz'*(not i % 3)+'Buzz'*(not i % 5) or i, range(1,101)),sep='\n')

""" print(list(map(lambda z: “Fizz” if type(z)==int and z%3==0 else z, 
map(lambda y: “Buzz” if type(y)==int and y%5==0 else y, 
map(lambda x: “FizzBuzz” if x%15==0 else x, range(1, 101)))))) """