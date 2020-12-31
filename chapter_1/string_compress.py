'''
String Compression: Implement a method to perform basic string compression
using the counts of repeated characters. For example, the string aabcccccaaa
would become a2blc5a3 . If the "compressed" string would not become smaller
than the original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a - z).
'''

def str_compress(string):
    # keep count of characters
    compressed = []
    counts = 0
    # iterate through sorted(string)
    for i in range(len(string)):
        if i !=0 and string[i] != string[i-1]:
            compressed.append(string[i-1] + str(counts))
            counts = 0
        counts += 1

    # add last repeat character
    if counts:
        compressed.append(string[-1] + str(counts))

    # return format of [letter][count]
    return min(string, "".join(compressed), key=len)

a = 'aaaabbbbccccddddd'
b = 'aaa'
c = 'zzzzqqqqmmmmdd'

print(str_compress(a))
print(str_compress(b))
print(str_compress(c))
