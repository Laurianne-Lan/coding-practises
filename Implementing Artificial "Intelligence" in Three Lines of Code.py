while True:
    #ins = input("请随便问")
    #ins = ins.replace("吗","")
    #ins = ins.replace("?", "!")
    #ins = ins.replace("?", "!")
    ins = input("请随便问").replace("吗","").replace("?", "!").replace("?", "!")
    print("人工智障回: ", ins, sep="")

    if ins == "再见" or ins == "拜拜":
        print("人工智障撇了你一眼, 头也不回地走了~")
        break
#this could only be understood due to the difference in grammer between Chinese and English
#adding the character "吗" is capable of changing most sentences into questions
