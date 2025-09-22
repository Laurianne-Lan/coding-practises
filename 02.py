
def game(lst:list):
    _lst = lst[:]

    if len(_lst)>1:
        count = 0
        index = 0
        while len(_lst)>1:
            count+=1
            if count%3==0:
                eliminated = _lst.pop(index)  # 删除当前索引的元素
                print(f"eliminated: {eliminated}")
                # 删除后不需要index+1，因为后面的元素会自动前移
            else:
                index += 1  # 不删除则移动到下一个元素

                # 防止索引越界，循环回到列表开头
            if index >= len(_lst):
                index = 0
    print(f"{_lst[0]} is the winner!")
    print(f"{_lst[0]} was in the {lst.index(_lst[0])+1}th position")
    print(" END of this game cycle!")





while True:
    l = input("please enter a list of names,enter 'q' to quit")
    if l=="q":
        print("bye~")
        break
    else:
        print(l)
        _l = l.strip().split(",")
        print(_l)
        game(_l)