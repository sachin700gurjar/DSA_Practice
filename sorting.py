# Selection Sort-----
# def selectionsort(arr):
#     n=len(arr)
#     if len(arr)==0:
#         return arr
#     for i in range(n-1):
#         min = i 
#         for j in range(i+1,n):
#             if arr[j]<arr[min]:
#                 min = j
#         arr[i],arr[min] = arr[min],arr[i]
#     return arr
arr = [3,44,5,6,43,1,4]
# a = selectionsort(arr)
# print(a)

#Bubblesort-----
# def Bubblesort(arr):
#     for i in range(n):
#       n=len(arr)
#       swap = 0
#       if len(arr)==0:
#            return arr
#       for j in range(n-i-1):
#            if arr[j]>arr[j+1]:
#                arr[j],arr[j+1]=arr[j+1],arr[j]
#                swap=1
#       if  not swap:
#         break
# return arr
# arr = [3,44,5,6,43,1,4]
#  a = Bubblesort(arr)
#  print(a)

#Insertionsort-----
def Insertionsort(arr):
    n = len(arr)
    if n==0:
        return arr
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
arr=[3,5,6,43,1,4,44]
a=Insertionsort(arr)
print(a) 
       






