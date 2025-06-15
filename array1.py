arr = []
for i in range(5):
    element = int(input(f"Enter the element value{i+1}:"))
    print(f"index number at element inserted :{i}")


    arr.append(element)
print(arr)
print("Searching process start :")
if(len(arr)==0):
    print("No element in arr")
else:
    search_val = int(input("Enter searching value here:"))
    if(search_val in arr):
        print(f"Entered value is in array at{arr.index(search_val)}")
    else:
        print("Entered value is not in array")
print("remove element from array")
val = int(input("Entered element that is remove from array:"))
print(f"remove item :{arr.remove(val)}")
print("array after remove item",arr)

print("print only which that is in odd index place")

print(arr[1:6:2])
