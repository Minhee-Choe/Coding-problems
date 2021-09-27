'''
Souce:
https://practice.geeksforgeeks.org/problems/rotate-by-90-degree-1587115621/1
Problem:
Given a square matrix of size N x N. The task is to rotate it by 90 degrees in anti-clockwise direction without using any extra space. 
'''
from math import ceil
def rotateAntiClock90(mat):
    for i in range(int(len(mat)/2)):
        for j in range(i, len(mat)-1-i):
            temp = mat[i][j]
            #mat[i][j]->mat[j][len(mat)-1-i] 
            mat[i][j] = mat[j][len(mat)-1-i] 
            mat[j][len(mat)-1-i]=mat[len(mat)-1-i][len(mat)-1-j]            
            mat[len(mat)-1-i][len(mat)-1-j]=mat[len(mat)-1-j][i]                  
            mat[len(mat)-1-j][i]=temp
    return mat


mat = [[0 for x in range(4)] for y in range(4)]
mat = [ [1, 2, 3, 4 ],
        [5, 6, 7, 8 ],
        [9, 10, 11, 12 ],
        [13, 14, 15, 16 ] ]
print(rotateAntiClock90(mat))
print(rotateClock90(mat))
mat = [[0 for x in range(3)] for y in range(3)]
mat = [ [1, 2, 3 ],
        [4, 5, 6 ],
        [7, 8, 9 ] ]
print(rotateAntiClock90(mat))
print(rotateClock90(mat))
mat = [[0 for x in range(2)] for y in range(2)]
mat = [ [1, 2 ],
        [4, 5 ] ]
print(rotateAntiClock90(mat))
print(rotateClock90(mat))

'''
Solution:
Found a pattern that mat[i][j] should go to mat[len(mat)-1-j][j].
'''
