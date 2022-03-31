import random
print("This is number  guessing game")
number=random.randint(1,9)
chances=0
print("Guess a number between 1 to 9")
while chances<5:
    guess=int(input("enter your guess"))
    if guess==number:
        print ("congratulations you won")
        break
    elif guess<number:
        print ("your guess was low")
    else:
        print ("your guess was too high")
    chances+=1
if not chances<5:
    print("you loose and the number is ",number)               