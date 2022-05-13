import math
import os
import random
import re
import sys

""" time = input().strip()
h, m, s = map(int, time[:-2].split(':'))
p = time[-2:]
h = h % 12 + (p.upper() == 'PM') * 12
print(('%02d:%02d:%02d') % (h, m, s)) """

#    print(time.strftime('%H:%M:%S', time.strptime(input(), '%I:%M:%S%p')))
#return time[:-2] if time[-2:] == "AM" else str(int(time[:2]) + 12) + time[2:8]

def convert_to_24(time):
    if time[-2:] == "AM" and time[:2] == "12":
        return "00"+time[2:-2]
    elif time[-2:] == "AM":
        return time[:-2]
    elif time[-2:] == "PM" and time[:2] == "12":
        return time[:-2]
    else:
        return str(int(time[:2]) + 12) + time[2:8]

def timeConversion(s):
    # Write your code here
    return s[:-2] if s[-2:] == "AM" else str(int(s[:2]) + 12) + s[2:8]


if __name__ == '__main__':
     #fptr = open(os.environ['OUTPUT_PATH'], 'w')
     s = input()
     result = timeConversion(s)
     r= convert_to_24(s)
     print(r)
     #fptr.write(result + '\n')
     #fptr.close()
