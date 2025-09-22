def concatenate(current_combos):
    """
    给当前所有组合的末尾各拼接一个新碱基（A/G/C/T）
    每次调用后，每个组合的长度增加1
    """
    bases = ["A", "G", "C", "T"]  # 原始碱基库（固定不变）
    new_combos = []
    for combo in current_combos:
        for base in bases:
            new_combos.append(combo + base)  # 每个现有组合 + 1个新碱基
    return new_combos



def combination(num):
    lst = ["A", "G","C","T"]
    if num==1:
        return lst
    else:
        for i in range(num-1):#range(num)执行num次
            lst = concatenate(lst)

    return lst

print(concatenate(["A", "G","C","T"]))
print(combination(2))
print(combination(3))