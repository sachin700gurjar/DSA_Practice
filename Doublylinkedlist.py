class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None
class Dlinkedlist:
    def __init__(self):
        self.head = None 
        self.tail = None 
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    def insert_at_specpos(self,pos,data):
        new_node = Node(data)
        if pos<=0:
            print("position is not valid ")
            return
        if pos == 1:
            return insert_at_beginning()
        else:
            temp = self.head
            count = 1 
            while temp is not None and count <pos-1:
                temp = temp.next
                count+=1
            if temp is None:
                print("position is out of range ")
                return
            new_node.next = temp.next
            new_node.prev = temp

            if temp.next:
                temp.next.prev = new_node
            else:
                self.tail =new_node
            temp.next = new_node
    def forward_traversal(self):
        print("forward traversal:")
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("None")
    def backword_traversal(self):
        print("backword traversal:")
        temp = self.tail
        while temp:
            print(temp.data,end="<-")
            temp=temp.prev
        print("None")

a = Dlinkedlist()
a.insert_at_beginning(20)
a.insert_at_specpos(2,30)
a.insert_at_specpos(3,40)
a.insert_at_end(45)
a.forward_traversal()
a.backword_traversal()
            
        