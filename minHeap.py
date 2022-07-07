import sys

class MinHeap:
    def __init__(self):
        self.array = [-1]

    def find(self, val):
        if val in self.array[1:]:
            return self.array[1:].index(val)
        else:
            return -1
                    
    def heapifydown(self, i):
        while 2*i <= len(self.array):
            left = self.array[2*i] 
            if 2*i+1 > len(self.array):
                right = sys.maxsize
            else:
                right = self.array[2*i+1]
            if self.array[i] > left or self.array[i] > right:
                if left > right:                    
                    self.array[2*i+1] = self.array[i]
                    self.array[i] = right
                    i = 2*i+1
                else:
                    self.array[2*i] = self.array[i]
                    self.array[i] = left
                    i = 2*i
            else:
                 break
                   
    def heapifyup(self):
        i = len(self.array)-1
        while i//2 > 0:
            if self.array[i//2] > self.array[i]:
                temp = self.array[i]
                self.array[i] = self.array[i//2]
                self.array[i//2] = temp            
            i=i//2
            
    #Insert
    def insert(self, val):
        self.array.append(val)
        self.heapifyup()
        
    def delete(self, val):
        index = self.find(val)
        if index > 0:
            lastVal = self.array.pop()
            self.array[index] = lastVal
            self.heapifydown(index) 
            
    def getMinimum(self):
        if len(self.array) >1:
            return self.array[1]
        else:
            return "The heap is empty." 
    

#main
if __name__ == '__main__':
    heap = MinHeap()
    queryNum = int(input())
    for x in range(queryNum):
        query = list(map(int,input().split()))
        if query[0] ==1:
            heap.insert(query[1])
        elif query[0] == 2:
            heap.delete(query[1])
        elif query[0] == 3:
            print(heap.getMinimum())
    
        

