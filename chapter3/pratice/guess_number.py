import random
from tokenize import Number

number = random.randint(1, 100)
num = int(input("Guess a number between 1 and 100: "))
if num == number:
    print("You guessed right!The number was " , number )
else:
    print("You guessed wrong!The number was " , number)