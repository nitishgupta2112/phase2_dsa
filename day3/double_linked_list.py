class Node:
    def __init__(self,value):
        self.previous = None
        self.data = value
        self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def isempty(self):
        if self.head is None:
            return True
        return False
    
    def length(self):
        temp = self.head
        count = 0
        while temp is not None:
            temp = temp.next
            count+=1
        return count
    
    def insertAtBeginning(self,value):
        new_node = Node(value)
        if self.isempty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head=new_node
    
    def insertAtEnd(self,value):
        new_node = Node(value)
        if self.isempty():
            self.insertAtBeginning(value)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.previous=temp

    def insertAtPosition(self,value,Position):
        temp = self.head
        count = 1
        while temp is not None:
            if count == Position -1:
                break
            count +=1
            temp = temp.next
            if Position ==1:
                self.insertAtBeginning(value)
            elif  temp is None:
                print("there are less than {}-1 elements in the linked list.cannot insert at {} position.".format(Position,Position))
            elif temp.next is None:
                self.insertAtEnd(value)
            else:
                new_node =Node(value)
                new_node.next = temp.next
                new_node.previous = temp
                temp.next.Previous = new_node
                temp.next = new_node
    
    def deleteFromBeginning(self):
        if self.isempty():
            print("Linked List is empty. Cannot delete element")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.previous = None
        
    def deleteFromEndinning(self):
        if self.isempty():
            print("Linked List is empty. Cannot delete element")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.previous.next=None
            temp.previous=None

    
    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data,sep=",")
            temp = temp.next


x = DoublyLinkedList()
print(x.isempty())
x.insertAtBeginning(5)
x.insertAtBeginning(15)
x.insertAtBeginning(25)
x.insertAtEnd(40)
x.insertAtEnd(45)
x.insertAtPosition(6,3)
x.printLinkedList()
print("no of nodes",x.length())
x.deleteFromBeginning()
x.deleteFromEndinning()
x.printLinkedList()