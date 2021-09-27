'''
Source:
https://practice.geeksforgeeks.org/problems/pythagorean-triplet3018/1
Problem:
Given an array arr of N integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2, otherwise false.
'''
from itertools import combinations

def Comibations(arr,n):
    for i in combinations(arr,3):
	if(i[0]**2 + i[1]**2 == i[2]**2 or i[1]**2 + i[2]**2 == i[0]**2 or i[2]**2 + i[0]**2 == i[1]**2):
		return True

def SetApproach(arr, n):
    for i in range(n):
        arr[i] = arr[i] * arr[i]
 
    arr.sort()
 
    for i in range(n - 1, 1, -1):
        s = set()
        for j in range(i - 1, -1, -1):
            if (arr[i] - arr[j]) in s:
                return True
            s.add(arr[j])
    return False

'''
Solution:
1. using combinations:
- Get all possible n_C_3, and verify each combination 

2. using set:
- Get i^2 for all n numbers, and verify if there is a set that can make a+b=c
'''
