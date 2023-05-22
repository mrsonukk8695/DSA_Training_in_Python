import SinglyLinkedList
def checkLength(LinkedList):
    count=0
    temp=LinkedList.head
    while(temp !=None):
        count+=1
        temp=temp.next
    return count

def reverseLinkedList(myLinkedList):
    prev=None
    current=myLinkedList.head
    while(current !=None):
        temp=current.next
        current.next=prev
        prev=current
        current=temp
    myLinkedList.head=prev

if __name__=='__main__':
    mylinkedlistobj=SinglyLinkedList.LinkedList()
    for i in range (1,20,3):
        mylinkedlistobj.insertAtStart(i)
    mylinkedlistobj.printLinkedList()
        #print(".......")
    print(reverseLinkedList(mylinkedlistobj))