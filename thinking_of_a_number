import random

guessesTaken = 0

print("I'm thinking of a number!")
print("Try to guess the number I'm thinking of")
print("by picking a number between 1 and 10")
myNumber = (random.randint(1, 10))

while guessesTaken < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < myNumber:
        print('Your guess is too low.')
    if guess > myNumber:
        print('Your guess is too high.')
    if guess == myNumber:
        break

if guess == myNumber:
    guessesTaken = str(guessesTaken)
    print('Good job, You guessed my number in ' + guessesTaken + ' guesses!')

if guess != myNumber:
    number = str(myNumber)
    print('Nope. The number I was thinking of was ' + number)
