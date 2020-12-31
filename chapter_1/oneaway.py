'''
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
'''

def are_one_different(s1, s2):
    # check insert/remove as they are same
    if len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    # check replace, which == one place different
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    # keep rolling count, has to be <= 1
    if len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)


def one_edit_replace(s1, s2):
    edited = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True

def one_edit_insert(s1, s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True


a = 'pale'
b = 'sale'
c = 'ale'
d = 'pail'

print(are_one_different(a,b))
print(are_one_different(a,c))
print(are_one_different(a,d))
print(are_one_different(b,d))
print(are_one_different(b,c))
