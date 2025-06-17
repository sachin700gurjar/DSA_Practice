class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
    def insert_at_specifiecposition1(self,pos,data):
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
            count += 1
        if temp is None:
            print("position is out of range")
            return 
        new_node.next = temp.next
        temp.next = new_node
    def display(self):
        temp = self.head
        while temp :
            print(temp.data,end="->")
            temp = temp.next
        print(None)
a = linkedlist()
a.insert_at_specifiecposition1(2,5)
a.insert_at_specifiecposition1(1,10)
a.insert_at_specifiecposition1(2,30)
a.display()