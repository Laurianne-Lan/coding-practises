def shorten(s):
    l = ""
    w = ""
    count = 0
    for i in s:
        if l!=i:
            if count>0:
                w += l + str(count)
            l = i
            count = 0
        count+=1
    w+=l+str(count)
    if len(w)>=len(s):
        return s
    return w

while True:
    i = input("please input a string containing only letters that repeat for a number of times, type 'q' to quit")
    if i=="q":
        break
    else:
        r = shorten(i)
        print(r)



