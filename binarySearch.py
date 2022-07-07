def binaryRecursive(array, x, left, right):
    if left>right:
        return False
    
    mid = (left+right)//2
    if array[mid] == x:
        return True
    elif x < array[mid]:
        return binaryRecursive(array, x, left, mid-1)
    else:
        return binaryRecursive(array, x, mid+1, right)
    
    
def binarySearch(array, x):
    return binaryRecursive(array, x, 0, len(array)-1)

def binarySearchIterate(array, x):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = left + (right-left)//2
        if array[mid] == x:
            return True
        elif x < array[mid]:
            right = mid-1
        else:
            left = mid+1
    
    return False
    
     
