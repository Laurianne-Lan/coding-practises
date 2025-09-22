def reverse(str):
    l = []
    for i in range(len(str)-1, -1, -1):
        l.append(str[i])
    _l = "".join(l)
    if str == _l:
        return True
    return False

def findLongest(s):
    w_l = 0
    l_s = len(s)
    lst = []
    a = ""
    for i in range(l_s-1):
        for j in range(i+1,l_s):
            b = s[i:j+1]
            if reverse(b)==True:
                lst.append(b)
    if len(lst)!=0:
        for i in lst:
            if len(i)>w_l:
                w_l = len(i)
                a = i
        return a
    return "There are no palindrome in this string"


while True:
    i = input("please enter a sting that may or may not contain a palindrome, type 'q' to quit")
    if i=='q':
        break
    else:
        r = findLongest(i)
        print(r)





