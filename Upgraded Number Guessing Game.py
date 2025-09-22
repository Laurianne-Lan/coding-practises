import random
answer = random.randint(100,1000)
_t = answer//100
_s = answer//10
_f = answer%100%10
print(answer)
while True:
    n = input("Please in put a 3 digit number, enter 'q' to quit")
    if n=="q":
        break
    else:
        num = int(n)
        t = num//100
        s = num//10
        f = num%100%10
        a = 0
        b = 0

        if _t==t:
            a+=1
        else:
            b+=1
        if _s==s:
            a+=1
        else:
            b+=1
        if _f==f:
            a+=1
        else:
            b+=1
        print(f"{a}A{b}B")
