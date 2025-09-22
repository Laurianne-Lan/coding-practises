lst = []
for i in range(1,10):
    for j in range(0,10):
        for k in range(0, 10):
            a = i*100+j*10+k
            b = i**3+j**3+k**3
            if a==b:
                lst.append(a)

print(lst)
