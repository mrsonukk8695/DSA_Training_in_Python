class MyNode:
    def __init__(self,data=None):
        self.data=data
        self.next=None
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next

class MyQueue_using_LinkedList:
    def __init__(self):
        self.Linkedlistobj=LinkedList()
    def __str__(self):
        values=[str(i)  for i in self.Linkedlistobj]
        return " ".join(values)
    def Enqueue(self,value):
        newNode=MyNode(value)
        if self.Linkedlistobj.head==None:
            self.Linkedlistobj.head=newNode
            self.Linkedlistobj.tail=newNode
            return "Node created successfully"
        else:
            self.Linkedlistobj.tail.next=newNode
            self.Linkedlistobj.tail=newNode
            return "Node created successfully"
    def IsEmpty(self):
        if self.Linkedlistobj.head==None:
            return True
        else:
            return False
    def Deque(self):
        if self.IsEmpty():
            return "there is no data"
        else:
            temNode=self.Linkedlistobj.head
            if self.Linkedlistobj.head==self.Linkedlistobj.tail:
                self.Linkedlistobj.head=None
                self.Linkedlistobj.tail=None
            else:
                self.Linkedlistobj.head=self.Linkedlistobj.head.next
                return temNode
    def peek(self):
        if self.IsEmpty():
            return "No data "
        else:
            return self.Linkedlistobj.head
    def delete(self):
        self.Linkedlistobj.head=None
        self.Linkedlistobj.tail=None


ObjQueue=MyQueue_using_LinkedList()
print(ObjQueue.Enqueue(12))
print(ObjQueue.Enqueue(1))
print(ObjQueue.Enqueue(2))
print(ObjQueue.Enqueue(82))
print(ObjQueue)
print(ObjQueue.peek())
print(ObjQueue.Deque())
print(ObjQueue)

     