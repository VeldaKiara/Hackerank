"""
My thought process
num = input("What's your number?")
for i in range(1, int(num) + 1): 
    print(" " * (int(num) - int(i)) + "#" * i)
"""
#Hackerank solution
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(1, n + 1):
       print(' ' * (n - i) + '#' * i)

if __name__ == '__main__':
    n = int(input())

    staircase(n)