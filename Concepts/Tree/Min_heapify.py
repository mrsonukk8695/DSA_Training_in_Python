

def MinHeapify(MyArray,k):
    l=leftChild(k)
    r=RightChild(k)
    if ((l<len(MyArray)) and (MyArray[l]<MyArray[k])):
        smallest=l
    else:
        smallest=k
    if ((r<len(MyArray)) and (MyArray[r]<MyArray[smallest])):
        smallest=r
        
    if smallest!=k:
        MyArray[k],MyArray[smallest]=MyArray[smallest],MyArray[k]
        return MinHeapify(MyArray,smallest)
    #print((MyArray),end="")
    
def leftChild(k):
    return (2 * k+1)

def RightChild(k):
    return (2 * k+2)

        
def Min_Heap_creation(MyArray):
    n=int((len(MyArray)//2)-1)
    for k in range (n,-1,-1):
        MinHeapify(MyArray,k)
        
MyArray=[45,35,1,10,9,1,87,56]
Min_Heap_creation(MyArray)
print(Min_Heap_creation(MyArray))