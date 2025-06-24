class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Slinked:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next!=self.head :
                temp= temp.next
            temp.next = new_node      
            new_node.next = self.head
            self.head = new_node
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next!=self.head :
                temp= temp.next
          
            temp.next = new_node
            new_node.next = self.head
    def insert_at_pos(self,pos,data):
        new_node = Node(data)
        if pos<1:
            print("position is invalid")
            return
        if pos == 1:
            self.insert_at_beginning(data)
            return
        temp = self.head 
        count = 1
        while temp.next != self.head and count<pos-1:
            temp = temp.next
            count+=1
        if count<pos-1:
            print("position is out of range")
            return
        new_node.next = temp.next
        temp.next = new_node
    def display(self):
        if self.head is None:
            print("list is empty")
        temp = self.head
        while temp:
            print(temp.data,end="->")
            if temp.next == self.head:
                break
            temp = temp.next
        print("(head)")
            

                 

a = Slinked()
a.insert_at_beginning(20)
a.insert_at_pos(2,30)
a.insert_at_end(40)
a.display()