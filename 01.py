while True:
    l = (input("please input the list:"))
    s = input("choose the way you want to sort,quit with the letter q: increasing or decreasing:")
    _lst = list(l)
    lst =[int(i) for i in _lst]
    ls = s.lower()
    print(ls)
    print(lst)
    if ls=="q":
        break
    elif ls=="increase":
        for i in range(0, len(lst)):
            for j in range(0, len(lst) - 1 - i):
                if lst[j] > lst[j + 1]:
                    temp = lst[j + 1]
                    lst[j + 1] = lst[j]
                    lst[j] = temp
                    print(lst)
                    print("内循环" + str(j))
            print("-----"+str(i))
    elif ls=="decrease":
        for i in range(0, len(lst)):
            for j in range(0, len(lst) - 1 - i):
                if lst[j] < lst[j + 1]:
                    temp = lst[j + 1]
                    lst[j + 1] = lst[j]
                    lst[j] = temp
                    print(lst)
                    print("内循环" + str(j))
            print("-----" + str(i))