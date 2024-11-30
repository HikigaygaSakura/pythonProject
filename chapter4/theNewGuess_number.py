# 目标数字
import random
secret_number = random.randint(1, 10)
#最多次数
guess_limit = 4
#已猜测数
guess_number = 0
while guess_number < guess_limit:
    your_number = int(input("Guess a number between 1 and 10: "))
    guess_number += 1
    if your_number == secret_number:
        print("You guessed right!")
        break
else:
    print("Sorry, you have lost.")
print("This number is ",secret_number)
print("game over")

