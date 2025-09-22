
def decide(h,f):
    a = h*4
    if a>f:
        b = a-f
        n_c = b//2
        n_r = h-n_c
    elif a==f:
        n_c = 0
        n_r = h
    else:
        return "ERROR!"
    if n_c>0 and n_r>0:
        return n_c, n_r
    else:
        return "ERROR!"

while True:
    I = input("PLEASE INPUT THE NUM OF HEADS, ENTER 'q' TO QUIT")
    J = input("PLEASE INPUT THE NUM OF FEET")
    if I=="q":
        break
    else:
        h = int(I)
        f = int(J)
        if type(decide(h,f))==tuple:
            num_c, num_r = decide(h,f)
            print(f"there are(is) {num_c} chicken and {num_r} rabbits")
        else:
            print(decide(h,f))

