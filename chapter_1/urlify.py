'''
Write a method to replace all spaces in a string with '%20: You may assume that
the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string.
'''




def urlify_algo(str, length):
    # remove trailing space, work backwards and replace spaces
    # convert to list first becasue python str are immutable
    str = list(str)
    string = ''
    new_idx = len(str)

    for i in reversed(range(length)):
        if str[i] == " ":
            # replace spaces
            str[new_idx - 3: new_idx] = "%20"
            new_idx -= 3
        else:
            # move characters
            str[new_idx - 1] = str[i]
            new_idx -= 1

    return string.join(str)

def urlify_python(str, length):
    return str[:length].replace(' ', '%20')

# Testing
s1 = 'Mr John Smith    '
len1 = 13

print(urlify_python(s1, len1))
print(urlify_algo(s1, len1))
