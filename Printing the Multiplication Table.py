
def form():
    rows = []
    for i in range(1,10):
        row = []
        for j in range(1,i+1):
            row.append(f"{i}*{j}")
        rows.append(" ".join(row))#用空格连接 n*m
        #print(rows)
    c = "\n".join(rows)# 用换行连接所有行，直接输出
    print(c)

def reverse_form():
    rows= []
    for i in range(9,0,-1):
        row = []
        for j in range(i,0,-1):
            row.append(f"{i}*{j}")
        rows.append(" ".join(row))  # 用空格连接 n*m
        #print(rows)
    c = "\n".join(rows)  # 用换行连接所有行，直接输出
    print(c)

while True:
    i = input("Please enter the command: f for the form, r for the reversed, q to quit")
    if i=="q":
        break
    elif i=="f":
        form()
    elif i=="r":
        reverse_form()
