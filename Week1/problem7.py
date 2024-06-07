def palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    
    return True
        
string1 = "Akshat"
string2 = "abba"
print(palindrome(string1))
print(palindrome(string2))