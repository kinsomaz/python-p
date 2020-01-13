#This is a guess the number game
import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 to 20.')

#Ask the player to guess 6 times.
for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())
    if guess  < secretNumber:
        print('your guess is too low.')
    elif guess  > secretNumber:
        print('your guess is too high.')
    else:
        break  # This condition is the correct guess!
if guess == secretNumber:
    print('Well done.You have guess my number in ' + str(guessesTaken) + ' guess!' )
else:
    print('Nope. The number i am thinking of is ' +  str(secretNumber))
    
   

