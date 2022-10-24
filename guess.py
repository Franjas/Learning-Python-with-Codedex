# Create a program that guesses the number:
# First, introduce a variable called tries at the top and give it a value of 0.
# Then, add another condition to the while using a logical operator.
# Codédex

guess = 0
tries = 0

print('Hello! Guess the number from 1 to 10')

while guess != 7 and tries < 5:
    guess = int(input("Guess the number:  "))
    tries += 1

if guess != 7:
    print("Game over")
  
else:
    print("Very well!! You got it in", tries,'tries')