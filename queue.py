class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def display(self):
        print("Queue elements:", self.queue)
a = Queue()
a.enqueue(10)
a.enqueue(20)
a.enqueue(30)
a.display()
print("\npopped element is :",a.dequeue())
print("\npeek element is :",a.peek())
a.display()
print("is queue empty :",a.is_empty())