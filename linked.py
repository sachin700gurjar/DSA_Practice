class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
    def insert_at_specposition(self,pos,data):
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head 
            self.head = new_node
            return
        if self.head is None:
            print("position is out of range")
            return
        temp = self.head
        count = 1 
        while temp is not None and count<pos-1:
            temp = temp.next
            count+=1
        if temp is None:
            print("position is out of range")
            return
        new_node.next = temp.next
        temp.next = new_node
    def deletion_at_beginning(self):
        if self.head is None:
            print("linkedlist is empty")
            return
        self.head = self.head.next
    def deletion_at_end(self):

        if self.head is None:
            print("linkedlist is empty")
            return
        if self.head.next is None:
             self.head = None
             return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

        
    def deletion_at_specpos(self,pos):
        if self.head is None:
            print("linkedlist is empty")
            return
        if pos == 1:
            self.head=self.head.next
            return
        temp = self.head
        count = 1
        while temp is not None and count<pos-1:
            temp = temp.next
        if temp is None or temp.next is None:
            print("position out of range")
            return
        temp.next =  temp.next.next
    
    def display(self):
        temp = self.head 
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print(None)
a = linkedlist()
a.insert_at_specposition(1,15)
a.insert_at_end(10)
a.insert_at_specposition(3,20)
a.display()
a.deletion_at_beginning()

a.deletion_at_specpos(1)

a.display()

