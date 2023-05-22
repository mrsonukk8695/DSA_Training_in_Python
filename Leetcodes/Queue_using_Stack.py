class MyStack:
    def __init__(self):
        self.stack_list=[]
    def __len__(self):
        return len(self.stack_list)
    def push (self):
        self.stack_list.append()
    def pop(self):
        if len(self.stack_list)==0:
            return None
        else:
            self.stack_list.pop()

class Queue_using_stack:
    def __init__(self):
        self.in_Stack=MyStack()
        self.out_Stack=MyStack()
    def Enqueue(self,data):
        self.in_Stack.push(data)
    def Deque(self):
        while len(self.in_Stack):
            self.out_Stack.push(self.in_Stack.pop())
        result=self.out_Stack.pop()
        while len(self.out_Stack):
            self.in_Stack.push(self.out_Stack.pop())


Objque=Queue_using_stack()
Objque.Enqueue(1)
Objque.Enqueue(2)
Objque.Enqueue(3)
Objque.Enqueue(4)
Objque.Enqueue(5)
print(Objque)