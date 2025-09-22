
def exchange(nt,bottle, cap):
    n1 = bottle//2
    n2 = cap//3
    b = bottle%2
    c = cap%3
    nt=nt+n1+n2
    n = n1+n2
    b+=n
    c+=n
    return nt, b, c

def getDrink(amt):
    n = amt
    n_bottle = n
    n_cap = n
    while n_bottle>=2 or n_cap>=3:
        n,n_bottle,n_cap= exchange(n, n_bottle, n_cap)
        #更新n,n_bottle,n_cap数值下次调用函数时传入
    print(f"have a total of {n} bottles")

getDrink(3)
