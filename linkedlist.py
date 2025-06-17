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
    def insert_at_specifiecposition(self, pos, data):
        new_node = Node(data)

    # Insert at beginning (or when list is empty)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

    # If list is empty and pos > 1, invalid
        if self.head is None:
            print("⚠️ Position out of range")
            return

        temp = self.head
        count = 1

    # Traverse to (pos - 1)th node
        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("⚠️ Position out of range")
            return

    # Insert at correct position
        new_node.next = temp.next
        temp.next = new_node
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")    
a = linkedlist()
a.insert_at_specifiecposition(2, 20)  # ❌ Out of range (empty list)
a.insert_at_specifiecposition(1, 10)  # ✅ OK
a.insert_at_specifiecposition(2, 15)  # ✅ OK
a.insert_at_specifiecposition(4, 25)  # ❌ Out of range
a.insert_at_specifiecposition(3, 22)  # ✅ OK
a.display()

       
            
