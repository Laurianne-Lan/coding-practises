
def reverse(str):
    l = []
    for i in range(len(str)-1, -1, -1):
        l.append(str[i])
    _l = "".join(l)
    return _l

while True:
    i = input("Please input a string, type 'q' to quit")
    if i=="q":
        break
    else:
        _i = reverse(i)
        if i==_i:
            print("it is a palindrome")
        else:
            print("Please try again!")
