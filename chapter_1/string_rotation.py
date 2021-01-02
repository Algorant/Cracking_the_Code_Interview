'''
String Rotation: Assume you have a method i5Substring which checks if
one word is a substring of another. Given two strings, 51 and 52, write code
to check if 52 is a rotation of 51 using only one call to isSubstring
(e.g., Uwaterbottleuis a rotation of uerbottlewat U).
'''


def string_rotation(s1, s2):
    if len(s1) == len(s2) !=0:
        return s2 in s1 * 2

    return False



t1 = "waterbottle"
t2 = "erbottlewat"

print(string_rotation(t1, t2))
print(string_rotation(t2, t1))
