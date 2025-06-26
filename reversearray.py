# def reversearr(arr,start,end):
#     if start>=end:
#         return
    
#     arr[start],arr[end]=arr[end],arr[start]
#     reversearr(arr,start+1,end-1)
# arr=[1,2,3,5,4,2]
# a =reversearr(arr,0,len(arr)-1)
# print(arr)
# print("reverse array",a)
# def reversearr(arr):
#     if len(arr)==0:
#         return []
#     restarr = reversearr(arr[1:])
#     return restarr + [arr[0]]
# arr = [1,2,3,4]
# print(arr)
# a =reversearr(arr)
# print(a)

# def palindrome(s):
#     if len(s)<=1:
#         return "it is palindrome"
#     if s[0]!=s[-1]:
#         return "it is not palindrome"
#     return palindrome(s[1:-1])
# s = input()
# a = palindrome(s)
# print(a)