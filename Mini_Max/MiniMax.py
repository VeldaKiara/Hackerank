#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    Max = sorted(arr,reverse = True)
    mini= sorted(arr)
    Max_sum = 0
    mini_sum = 0
    for i in range(len(Max)-1):
        Max_sum = Max_sum +Max[i]
    for k in range(len(mini)-1):
        mini_sum = mini_sum+mini[k]
    print(mini_sum, Max_sum)
   
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
