class stack:
    def __init__(self):
        self.stack = []
    def push(self,s):
        self.stack.append(s)
        print(f"pushed element {s} in stack")
    def pop(self):
        if self.is_empty():
            return "\nStack is underflow - so no one element popped"
        else:
            return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return "\nStack is underflow - so no peek element"
        else:
            return self.stack[-1]
    def is_empty(self):
        return len(self.stack)==0

    def display(self):
        print ("\ncurrent Stack :",self.stack)
a = stack()
a.push(10)
a.push(20)
a.push(30)
a.display()
print("\npopped element :",a.pop())
print("\npeek element :",a.peek())
a.display()

print("\nis stack empty :",a.is_empty())