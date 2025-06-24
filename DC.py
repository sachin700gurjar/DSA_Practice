class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class dc:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_at_beginning(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
    def insert_at_pos(self,pos,data):
        new_node = Node(data)
        if pos<1:
            print("position is invalid")
            return

        if self.head is None and pos ==1:
            self.insert_at_beginning(data)
        else:
            temp=self.head
            count=1
            while temp.next!=self.head and count<pos-1:
                temp=temp.next
                count+=1
            if temp.next==self.head and count == pos-1:
                self.insert_at_end(data)
                
            elif count == pos-1:
                temp.next = new_node
                new_node.prev = temp
                new_node.next = temp.next
                temp.next.prev = new_node
            else:
                print("position out of range")
    def displayforward(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        while True:
            print(temp.data,end="->")
            temp=temp.next
            if temp == self.head:
                break
        print("(head)")
    def displaybackward(self):
        if self.head is None:
            print("list is empty")
            return
        temp=self.tail
        while True:
            print(temp.data,end="<-")
            temp=temp.prev
            if temp== self.tail:
                break
        print("(tail)")
a = dc()
a.insert_at_beginning(20)
a.insert_at_pos(2,30)
a.insert_at_end(40)
a.displayforward()
a.displaybackward()
        


            
        
