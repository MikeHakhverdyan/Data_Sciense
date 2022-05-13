#Capitalize
def capitalize(s): #String
    if 97 <= ord(s[0]) <= 122:
        return chr(ord(s[0]) - 32) + s[1::]
    else:
        return s

#Count
def count(s, sb): #String, Substring
    count = 0
    i = 0
    while i <= len(s) - len(sb):
        if s[i:i + len(sb)] == sb:
            count += 1
        i += 1
    return count

#Endswith
def endswith(s, sb): #String, Substring
    if s[-1] == sb:
        return True
    else:
        return False

#Find
def find(s, sb): #String, Substring
    i = 0
    while i <= len(s) - len(sb):
        if s[i: i + len(sb)] == sb:
            return i
        i += 1

#Join
def join(itr, s): #Iterable Object, Separator String
    st = ''
    i = 0
    while i < len(itr):
        st += str(itr[i])
        if i == len(itr) - 1:
            return st
        st += s
        i += 1

#Replace
def replace(s, sb1, sb2): #String, Substring, Replaceable Substring
    i = 0
    ss = ''
    while i <= len(s) - len(sb1) + 1:
        if s[i: i + len(sb1)] == sb1:
            ss += sb2
            i += len(sb2)
        else:
            ss += s[i]
        i += 1
    return ss

#RFind
def rfind(s,sb): #String, Substring
    i = len(s) - 1
    while i >= 0:
        if s[i - len(sb) + 1: i + 1] == sb:
            return i - len(sb) + 1
        i -= 1
    return None

#Strats With
def startswith(s, sb):#String, Substring
    if s[0] == sb:
        return True
    else:
        return False

#Strip
def strip(s, chars = [' ', '\t', '\n']):
    if s[0] in chars:
        return strip(s[1:], chars)
    if s[-1] in chars:
        return strip(s[:-1], chars)
    return s
print(strip('  asdf  asdf', 'afds'))

#Lower
def lower(s): #String
    ss = ''
    for letter in s:
        if 65 <= ord(letter) <= 90:
            ss += chr(ord(letter) + 32)
        else:
            ss += letter
    return ss