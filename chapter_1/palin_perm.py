'''
Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
permutation is a rearrangement of letters. The palindrome does not need to be limited to just
dictionary words.
'''

# used in pythonic solution
from collections import Counter

def palin_perm(str):
    # same forwards and backwards for all permutations
    # hash table
    hash_table = [0 for _ in range(ord("z") - ord("a") + 1)]
    count_odd = 0

    for c in str:
        x = char_number(c)
        if x != -1:
            hash_table[x] += 1
            if hash_table[x] % 2:
                count_odd += 1
            else:
                count_odd -= 1

    return count_odd <= 1

def char_number(c):
    a = ord("a")
    z = ord("z")
    upper_a = ord("A")
    upper_z = ord("Z")
    val = ord(c)

    if a <= val <= z:
        return val - a

    if upper_a <= val <= upper_z:
        return val - upper_a

    return -1

def palin_perm_pythonic(str):
    counter = Counter(str.replace(" ", "").lower())

    return sum(val % 2 for val in counter.values()) <= 1

s1 = "aba"
s2 = "abba"
s3 = "Tact Coa"
s4 = "noT a PalinDrome"


# Testing
print(palin_perm(s1))
print(palin_perm(s2))
print(palin_perm(s3))
print(palin_perm(s4))

print(palin_perm_pythonic(s1))
print(palin_perm_pythonic(s2))
print(palin_perm_pythonic(s3))
print(palin_perm_pythonic(s4))
