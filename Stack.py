stack = []
n = int(input("Enter a number which indicate number of elements in stack:"))
for i in range(n):
    val = int(input("Enter a value :"))
    stack.append(val)
print("\nFull stack :",stack)
print("\npop operation begin---")
pop = stack.pop()
if(len(stack)==0):
    print("stack is empty")
else:
    print("popped element is :",pop)
print("\nsearching peek element of stack---")
peek_element = stack[-1]
if(len(stack)==0):
    print("stack is empty")
else:
    print("peek element is :",peek_element)
print("\nprint final stack---")
print("stack is :",stack)


