s = input("Enter a string:")
upper=lower=digits=other=0
for i in s:
    if i.isupper():
        upper+=1
        
    elif i.islower():
        lower+=1
    elif i.isdigit():
        digits+=1
    else:
        other+=1
print("count of uppercase word :",upper)
print("count of lowercase word :",lower)
print("count of digits in string :",digits)
print("count of otherword :",other)

print("\n function---")

def removespace(s):
    return s.replace(" ","")
a = removespace(s)
print("String after removing space:",a)