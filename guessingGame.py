import random

print("Number guessing game")


number = random.randint(1, 9)


chances = 0

print("Guess a number between 1 to 9:")


while chances < 5:

   
    guess = int(input("Enter your guessed number:- "))

   

    if guess == number:
        print("Congratulation you guessed the right number!")
        break

    elif guess < number:
        print("Your guess was low...Choose a higher number than", guess)

    
    else:
        print("Your guess was too high: Guess a number lower than", guess)

    
    chances += 1

if not chances < 5:
    print("Sorry, you lost. The number is", number)