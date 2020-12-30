string = 'azcabcab'
sub = 'acb'

def almostSubstring(t, s):
    count = t.count(s)
    return count

print(almostSubstring(string, sub))
