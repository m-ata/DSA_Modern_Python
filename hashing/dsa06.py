# Hashing 

from utils.formater import format_time
import time
import math

n = [2,3,5,7,8,2,14,4,7,3,2,6,8,4,3,5,0,6,4,2]
m = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96]



# brute force method 
def method01(m: list[int], n: list[int]):
    listOfFrequency = {}
    start = time.perf_counter()
    for item in m:
        if item in n:
            if item in listOfFrequency:
                listOfFrequency[item] += 1
            else:
                listOfFrequency[item] = 1
    end = time.perf_counter()
    print(listOfFrequency)
    total_time = end-start
    print(format_time(total_time))


method01(m,n)