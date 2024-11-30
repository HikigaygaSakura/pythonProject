# 目标数字
import random
secret_number = random.randint(1, 10)
#最多次数
guess_limit = 4
#已猜测数
guess_number = 0
while guess_number < guess_limit:
    your_number = int(input("Guess a number between 1 and 10: "))
    guess_number += 1  #note：输入一次后就加1，不需要在if里搞
    if your_number == secret_number:
        print("You guessed right!")
        break

print("This number is ",secret_number)
print("game over")