'''
Given two strings, write a method to decide if one is a permutation of
the other.
'''

p1 = "god"
p2 = "dog"

np1 = "not"
np2 = "top"

# by sort

def is_perm_sort(s1, s2):
    # if they are not same length, fail
    if len(s1) != len(s2):
        return False
    # sort both strings
    s1, s2 = sorted(s1), sorted(s2)
    # if theres a character mismatch, fail
    for i in range(len(s1) - 1):
        if s1[i] != s2[i]:
            return False
        return True

print(is_perm_sort(p1,p2))
print(is_perm_sort(np1,np2))

def is_perm_count(s1, s2):
    # if they are not same length, fail
    if len(s1) != len(s2):
        return False
