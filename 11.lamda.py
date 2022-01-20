add = lambda x, y: x + y
print(add(5, 3))

#i want palindrome
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("radar"))