def is_palindrome(s):
    if len(s)<=1:
        return True
    elif s[0]!=s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])
text = input("Enter a string:").replace(" ","").lower()
if is_palindrome(text):
    print("\nstring is palindrome:",text)
else:
    print("\nstring is not palindrome:",text)