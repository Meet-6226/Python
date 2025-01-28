#Write a simple “guess the number” game. The program randomly generates number between 1 and 10 and user has to guess it

import random
num=random.randint(1,10)
print("Guess the number between 1 to 10")
while True:
    guess=int(input("Guess number: "))
    if guess==num:
        print("Congratulations! You guessed the correct number!")
        break
    elif guess>num:
        print(f"{guess} is above the number")
    elif guess<num:
        print(f"{guess} is below the number")