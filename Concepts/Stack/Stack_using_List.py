# Stack Using List
class MyStackList(object):
    def __init__(self,limit=10):
        self.stack_list=[]
        self.limit=limit
    def push(self,data):
        if len(self.stack_list)>=self.limit:
            print("Stack is already full")
        else:
            self.stack_list.append(data)
    def pop(self):
        if len(self.stack_list)<=0:
            return -1
        else:
            return self.stack_list.pop()

    def peek(self):
        if len(self.stack_list)<=0:
            return -1
        else:
            return self.stack_list[(len(self.stack_list)-1)]
    
    def IsEmpty(self):
        return self.stack_list==[]
    
    def Size(self):
        return len(self.stack_list)
    
    def __str__(self):
        return " ".join([str(i) for i in self.stack_list])
    def Search(self,value):
            if value in self.stack_list:
                return "Varible Found"
            else:
                return "Not Found"
    


Stack_Obj1=MyStackList()
for i  in range (10,50,5):
    Stack_Obj1.push(i)

Stack_Obj1.push(51)

#print("Size of the Stack is:",Stack_Obj1.Size())
#print("Element of the Stack:",Stack_Obj1)
#print("POPED Element is:",Stack_Obj1.pop())
#print("Top element of the Stack is:",Stack_Obj1.peek())
#print(dir(MyStackList))
#print(Stack_Obj1.__str__)
print(Stack_Obj1.Search(45))