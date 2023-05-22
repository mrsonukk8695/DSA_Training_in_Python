class MyNode:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class MyLinkedList:
    def __init__(self):
        self.head=None
    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next

class MyStackLinkedList:
    def __init__(self):
        self.LinkedList=MyLinkedList()
    def IsEmpty(self):
        if self.LinkedList.head==None:
            return True
        else:
            return False
    def push(self, value):
        node=MyNode(value)
        node.next=self.LinkedList.head
        self.LinkedList.head=node
    def pop(self):
        if self.IsEmpty():
            return "There is no element in the LinkedList"
        else:
            nodevalue=self.LinkedList.head.value
            self.LinkedList.head=self.LinkedList.head.next
            return nodevalue
    def peek(self):
        if self.IsEmpty():
            return "There is no element in the LinkedList"
        else:
            nodeValue=self.LinkedList.head.value
            return nodeValue
    def delete(self):
        self.LinkedListt.head=None
    def __str__(self):
        values=[(i.value)for i in self.LinkedList]
        return "\n".join(values)
    

Obj_stack=MyStackLinkedList()
Obj_stack.push(50)
Obj_stack.push(35)
Obj_stack.push(20)
Obj_stack.push(90)
print(Obj_stack.pop())
Obj_stack.peek()