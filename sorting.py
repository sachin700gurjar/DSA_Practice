def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [5,4,2,8,1]
bubblesort(arr)
print("sorted array:",arr)

def insertionsort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1

        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key
arr = [5,3,2,4,1]
insertionsort(arr)
print("sorted array after insertion sort :",arr)