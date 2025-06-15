s = input("Enter a string:")
vowel = 'aeiouAEIOU'
result = " "
for i in s:
    if i not in vowel :
        result+=i
print("Resulting string without vowel:",result)

print("\ncheck string is palindrome--")
s=s.replace(" ","").lower()
if s == s[::-1]:
    print("string is palindrome")
else:
    print("string is not palindrome")
print("\nstring is converted into uppercase and lowercase--")
print(s.upper())
print(s.lower())
print("\ncount of word without space--")
print(len(s))
print("\nprint all even index words--")
print(s[1::2])
