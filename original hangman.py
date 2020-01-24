import random
from time import sleep

HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    0
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    0
 |   -+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    0
 |  /-+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    0
 |  /-+-/
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    0
 |  /-+-/
 |    |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    0
 |  /-+-/
 |    |
 |    |
 |   |
 |   |
 |
----------
""",
"""
 ------
 |    |
 |    0
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |
----------
""")
WORDS = ('APPLE','PINEAPPLE','PAWPAW','WATERMELON','SUGARCANE','GRAPE','BANANA',
         'ORANGE','TOMATO','PEER','CHERRY','KIWI','PLUM','STRAWBERRY','MELON',
         'BLUEBERRY','BLACKBERRY','CUCUMBER','GRAVER','CARROT','MANGO','TANGERINE',
         'CASHEW','COCONUT')
Word = random.choice(WORDS)

POSITIVE_SAYINGS =('Well done!','Awesome!','You legend!')
MAX_WRONG = len(Word)-1
so_far = ('-')*len(Word)
print('\t \t Welcome to Hangman!')
print()
input('press Enter to start:')
def wrong():
    print()
wrong()
while  so_far !=Word:
    print()
    print('WRONG')
    print('Word so far:',so_far)
    used = letter in guess
    print('letters used:',used)

    guess = input('guess a letter:').upper()
    sleep(1)#Time delay-allows userfriendly reading
    print()

    while guess in used:
        print("Try again...you've already used this letter")
        guess = input('Guess a letter:').upper()
        sleep(1)
        print()
    used.append(guess)

    if guess in word:
        print(random.choice(POSITIVE_SAYING),'...Updating word so far...')

        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess

            else:
                new += so_far[i]
        so_far = new
    else:
        print('INCORRECT! Try again.')
        wrong += 1

print('Calculating result...')
sleep(1)
if wrong == MAX_WRONG:
    print('UNLUCKY! Better luck next time!')

else:
    print('WINNER! congratulation!')

print()
print()
input('press Enter to leave:')
        
























