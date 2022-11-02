def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a=str(input("Enter string to check whether it is Palindrome or not : "))
if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String is not a palindrome!")