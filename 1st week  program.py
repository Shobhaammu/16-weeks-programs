if __name__ == '__main__':
    a = int(input())
    b = int(input())
    #Integer/floor division ->integer part
    #Float division-> integer part with decimal
print(a//b)
print(a/b)

if __name__ == '_main_':
    a = int(input())
    b = int(input())
    # first line is for sum 
    #second line is for difference
    #third line is for multiplication
    print(a+b)
    print(a-b)
    print(a*b)
    
import math
import os
import random
import re
import sys


if __name__ == '_main_':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")