class MyQueue_using_list:
    def __init__(self):
        self.items_queue=[]
    def __str__(self):
        values = [str(i) for i in self.items_queue]
        return ' '.join(values)
    def IsEmpty(self):
        if self.items_queue==[]:
            return True
        else:
            return False
    def enqueue(self,data):
        self.items_queue.append(data)
        return "Data Added Successfully"
    def deque(self):
        if len(self.items_queue)<=0:
            return "No element in the list to the delete"
        else:
            return  self.items_queue.pop(0)
    def peek(self):
        if self.IsEmpty():
            return "Queue is Empty"
        else:
            return self.items_queue[0]
    def delete(self):
        self.items_queue=[]

Obj_Queue=MyQueue_using_list()
print(Obj_Queue.enqueue(1))
print(Obj_Queue.enqueue(34))
print(Obj_Queue.enqueue(45))
print(Obj_Queue.enqueue(78))
print(Obj_Queue.peek())
print(Obj_Queue.__str__())
print(Obj_Queue.deque())
print(Obj_Queue.__str__())


# max Limit=10