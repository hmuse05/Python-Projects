import random
print("Number guessing game")

number=random.randint(1,20)
#Computer will choose a random number 1 and 20

chances=0
print("Guess a number between 1 and 20")
while(chances<5):
    guess=int(input())
    if guess==number:
        print("congratulations you won!")
        break

    elif guess<number:
        print("Your guess is too low choose a higher number",guess)

    else:
        print("Your guess is too high choose a lower number",guess)

    chances+=1

    if not chances<5:
        print("You lose the number is",number)


