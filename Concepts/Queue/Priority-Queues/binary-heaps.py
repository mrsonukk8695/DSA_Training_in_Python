
# This is the example Min Heap
class binHeap:
    def __init__(self):
        self.heapList = [0]
        self.curSize = 0
        
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i = i // 2
    
    def insert(self, n):
        self.heapList.append(n)
        self.curSize += 1
        self.percUp(self.curSize)
        
    def percDown(self, i):
        while i * 2 <= self.curSize:
            minn = self.minChild(i)
            if self.heapList[i] > self.heapList[minn]:
                self.heapList[i], self.heapList[minn] = self.heapList[minn], self.heapList[i]
            i = minn
    
    def minChild(self, i):
        if (i * 2) + 1 > self.curSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            return i * 2 + 1
            
    def delMin(self):
        val = self.heapList[1]
        self.heapList[1] = self.heapList[self.curSize]
        self.curSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return val
        
    def buildHeap(self, alist):
        i = len(alist)//2
        self.curSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1
            
    def getMin(self):
        return self.heapList[1]
            
x = binHeap()
x.buildHeap([9, 6, 5, 2, 3])
print(x.heapList) # Print [0, 2, 3, 5, 6, 9]
print(x.delMin()) # Print 2
print(x.heapList) # Print [0, 3, 6, 5, 9]
x.insert(2)
print(x.heapList) # Print [0, 2, 3, 5, 9, 6]
print(x.getMin()) # Print 2
print(x.heapList) # Print [0, 2, 3, 5, 9, 6]
print(x.delMin()) # Print 2
print(x.heapList) # Print [0, 3, 6, 5, 9]