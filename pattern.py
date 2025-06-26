from math import *
n times star in nXn------
for i in range (n):
    for j in range(n):
        print("*",end="")
    print()

# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4 
    for i in range (n):
        for j in range(i+1):
            print(j,end="")
        print()

# 0 1 2 3 4 
# 0 1 2 3
# 0 1 2 
# 0 1 
# 0 
for i in range(n):
    for j in range(n-i):
        print(j,end="")
    print()

space , stars ,space pattern-----
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range((2*i)+1):
        print("*",end="")
    for j in range(n-i-1):
        print(" ",end="")
    print()

i times space ,stars,i times space pattern-----
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range((2*n)-(2*i+1)):
        print("*",end="")
    for j in range(i):
        print(" ",end="")
    print()

asceding triangle n times then descending triangle n-1 to 1-----
for i in range(2*n-1):
    k = i
    if k>n :
        k = 2*n-i
    for j in range(k):
        print("*",end="")
    print()

if i is even printing starting to 1 and then 1 swap to 0-----
# 1
# 0 1
# 1 0 1
# 0 1 0 1 
# 1 0 1 0 1
for i in range(n):
    if (i%2==0):
        stars = 1
    else:
        stars = 0
    for j in range(i+1):
        print(stars,end="")
        stars = 1-stars
    print()

# 1        1
# 12      21
# 123    123 
# 1234  1234
# 1234512345
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    for j in range(2*n-(2*i+2)):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    print()

# 1
# 2 3
# 4 5 6 
# 7 8 9 10
for i in range(1,n+1):
    num = 1
    for j in range(1,i+1):
        print(num,end="")
        num+=1
    print()
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end="")
    print()

# ABCDE
# ABCD
# ABC
# AB
# A
for i in range(n):
    for j in range(n-i):
        print(chr(65+j),end="")
    print()
     OR
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65+j),end="")
    print()

#         A
#       A B 
#     A B C
#   A B C D 
# A B C D E 
for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(i+1):
        print(chr(65+j),end="")
    print()

for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(chr(65+j),end="")
    for j in range(i-1,-1,-1):
        print(chr(65+j),end="")
    
    print()     

for i in range(n):
    for j in range(n-i):
        print("*",end="")
    for j in range(i*2):
        print(" ",end="")
    for j in range(n-i):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    for j in range(2*n-(2*i+2)):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()

for i in range(1,n+1):
   
    k = i 
    if k>n:
        k = 2*n-i 
    for j in range(k):
        print("*",end="")
  
    for j in range(2*n-2*i):
        print(" ",end="")

    for j in range(k):
        print("*",end="")
    print()
for i in range(n-1,0,-1):
    stars = '*'*i 
    space = ' '*(2*(n-i))
    print(stars+space+stars)
space = 2*n-2
for i in range(1,2*n):
    stars = i 
    if i>n:
        stars = 2*n-i
    
    for j in range(stars):
        print("*",end="")
    for j in range(space):
        print(" ",end="")
    for j in range(stars):
        print("*",end="")
    if i<n:
        space -= 2
    else:
        space+=2
    print()
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or  i==n-1 or j==n-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()   

for i in range(2*n-1):
    for j in range(2*n-1):
        top = i 
        left = j 
        right = (2*n-2)-j
        bottom = (2*n-2)-i 
        print((n)-min(min(top,bottom),min(right,left)),end="")
    print()
    
n1 = 1331
a = n1
count=0
rev=0
 while n1>0:
    rem = n1%10
    rev = (rev*10)+rem
    count+=1
    n1 = n1//10
    
if a == rev :
    print("it is palindrome")
else:
    print("it is not palidrome")

print("digits:",rev)
print("\nno. of digits",count)
n=36
l=[]
for i in range(1,int(sqrt(n))+1):
    if n%i==0:
       
        l.append(i)
        if n/i != i:
            
            l.append(int(n/i))
l.sort()
print(l)
n=int(input())
count = 0
for i in range (1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("no. is prime")
else:
    print("no. is not prime")
n1=12
n2=36
gcd=1

for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
        gcd = i

print(gcd)
a=52
b=10
while(a>0 and b>0):
    if a>b:
        a=a%b 
    else:
        b=b%a 
if a==0:
    print(b)
else:
    print(a)



        
        
        
        
        
        
        
        
        
        
        
        
        
        
           

