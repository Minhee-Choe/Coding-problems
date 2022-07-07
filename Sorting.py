import random

def BubbleSort(arr):
    for N in range(len(arr)-1,0,-1):        
        for i in range(N):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    print(*arr)

def SelectionSort(arr):
    for i in range(len(arr)-1):
        minIndex = arr.index(min(arr[i:]))
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    print(*arr)

def InsertionSort(arr):
    for i in range(1, len(arr)):
        X=arr[i]
        j=i-1
        while j>=0 and arr[j]>X:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1] = X
    print(*arr)

def MergeSort(arr):
    if len(arr)<=1:
        return
    
    mid=len(arr)//2

    L=arr[:mid]
    R=arr[mid:]

    MergeSort(L)
    MergeSort(R)

    #Merge
    i=j=k=0
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1

    while i<len(L):
        arr[k]=L[i]
        i+=1
        k+=1
        
    while j<len(R):
        arr[k]=R[j]
        j+=1
        k+=1

def partition(arr, left, right):
    pivot = X = left
    #X is the boundary of the group of the smaller values than the pivot
    for i in range(left+1, right+1):
        if arr[i]<arr[pivot] or (arr[i]==arr[pivot] and random.randint(0,1)):
            X+=1
            arr[X], arr[i] = arr[i], arr[X]
            
    arr[pivot], arr[X] = arr[X], arr[pivot]

    return X

def QuickSort(arr, left, right):
    if left>=right:
        return
    pivot = partition(arr, left, right)
    QuickSort(arr, left, pivot-1)
    QuickSort(arr, pivot+1, right)


if __name__== '__main__':
    arr = [12, 11, 19, 23, 4, 5, 2]
    print(*arr)
    print("BubbleSort:", end=" ")
    BubbleSort(arr)
    arr = [12, 11, 19, 23, 4, 5, 2]
    print("Reset:", end=" ")
    print(*arr)
    print("SelectionSort:", end=" ")
    SelectionSort(arr)
    arr = [12, 11, 19, 23, 4, 5, 2]
    print("Reset:", end=" ")
    print(*arr)
    print("InsertionSort:", end=" ")
    InsertionSort(arr)
    arr = [12, 11, 19, 23, 4, 5, 2]
    print("Reset:", end=" ")
    print(*arr)
    print("MergeSort:", end=" ")
    MergeSort(arr)
    print(*arr)
    arr = [12, 11, 19, 23, 4, 5, 2]
    print("Reset:", end=" ")
    print(*arr)
    print("QuickSort:", end=" ")
    QuickSort(arr, 0, len(arr)-1)
    print(*arr)
    
    
    
