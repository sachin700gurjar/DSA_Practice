class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def insert_data(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print(None)
a = linkedlist()

a.insert_data(10)
a.insert_data(20)
a.insert_data(30)
a.display()