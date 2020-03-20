#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for number in range(len(arr)):
        if (arr[number]>0):
            positive += 1
        elif (arr[number]==0):
            zero += 1
        else:
            negative += 1
    print(positive/len(arr))
    print(negative/len(arr))
    print(zero/len(arr))



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
