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
    mylinkedlist=SinglyLinkedList.LinkedList()
    for i in range (1,40,5):
        mylinkedlist.insertAtStart(i)
    mylinkedlist.printLinkedList()
    print(".......")
    print("Length of Lnkedlist is:",checkLength(mylinkedlist))