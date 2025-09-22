import random

def play(num, answer):
    if num==answer:
        print(f"Correct!Congratulations, the correct answer is {answer}")
    else:
        if num>answer:
            print("Too high, guess smaller")
        else:
            print("Too low, guess higher")

answer = random.randrange(0, 31, 1)
count = 0
while True:
    n = int(input("Please input a number 0～30(inclusive), enter 'q' to quit"))
    if count==4:
        print(f"the correct answer is {answer}")
        break
    elif n=="q":
        print("bye~")
        break
    else:
        play(n, answer)
        count+=1
