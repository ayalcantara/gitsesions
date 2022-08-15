""" def isAnagram(a, b):
 
        if sorted(a) == sorted(b):
            return True
        else:
            return False
 
# {
#  Driver Code Starts
 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = map(str, input().strip().split())
        if(Solution().isAnagram(a, b)):
            print("The two strings are anagram of each other")
        else:
            print("The two strings are not anagram of each other") """

import math
from collections import Counter

""" def anagram(s):
    n = len(s)
    if n % 2 == 1:
        return -1

    s = Counter(s [:n//2]) - Counter(s[n//2:])
    return sum(s.values()) """


def anagram(s):
    if len(s)%2: return -1
    l = len(s)//2
    a = Counter(s[:l])
    b = Counter(s[l:])
    return l-sum((a & b).values())

for _ in range(int(input())):
    print(anagram(input())) 

""" 
import os
import random
import re
import sys

def checkForAnagrams(word, arr): #checa si si es un anagrama o no
    for x in arr:
        if (sorted(word) == sorted(x)):
            return True
    return False

def funWithAnagrams(limitText):
    limit = len(limitText)
    final_limitText = list(limitText)
    count = 0
    for i in range(0, limit):
        if limitText[i+1:] and checkForAnagrams(limitText[i], limitText[i+1:]): #mada a llamar la funcion de revisar anagrama
            count += 1
    return sorted(final_limitText)

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    text_count = int(input().strip())

    text = []

    for _ in range(text_count):
        text_item = input()
        text.append(text_item)
    result = funWithAnagrams(text)
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close() """