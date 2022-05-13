""" import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    hold = [None]*int(len(arr)-3)
    for i in range(0,len(arr)-3):
        temp = 0
        for j in range(i, i + 4):
            temp = temp + arr[j]
        hold[i] = temp
    
    print(hold[0],hold[-1])


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

 """
def miniMaxSum(arr):
        arr.sort() #ordena de forma asendene la lista
        s = sum(arr) #suma los valores de la lista
        maxResult = s - arr[0] #resta el primer valor de la lista
        minResult = s - arr[len(arr) - 1] # resta el ultimo valor de la lista
    
        print(minResult, maxResult)
  
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)