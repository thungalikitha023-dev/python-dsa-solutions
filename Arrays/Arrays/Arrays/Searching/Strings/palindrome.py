def is_palindrome(s):
    s = s.lower()

    return s == s[::-1]


s = "madam"

print(is_palindrome(s))
