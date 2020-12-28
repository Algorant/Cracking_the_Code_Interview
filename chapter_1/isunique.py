'''
Implement an algo to determine if a string has all unique characters.

What if you cannot use data structures?
'''

# hints on page 665,
# questions on page 88

def is_unique_algorithmic(str):
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if str[i] == str[j]:
                return False

    return True

def is_unique_pythonic(str):
    if len(set(str)) == len(str):
        return True
    else:
        return False


s1 = "unique"
s2 = "bear"

print(is_unique_pythonic(s1))
print(is_unique_pythonic(s2))

print(is_unique_algorithmic(s1))
print(is_unique_algorithmic(s2))
