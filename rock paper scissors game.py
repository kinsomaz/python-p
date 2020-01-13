#This is a Rock , Paper or Scissors game
import random
spam = ( 'rock ',' paper' ,' scissors.')
computer = spam[random.randint(0,2)]
#set player to False
player = False
while player == False:
    #set player to true
    player = input()
    if player == computer:
            print('Tie!')
    elif player == 'rock':
        if computer == 'paper':
            print('You lose!,computer covers player')
        else:
            print('You won!,player smashes computer')
    elif player == 'paper':
        if computer == 'scissors':
            print('You lose!,computer cut player')
        else:
            print('You won!,player covers computer')
    elif player == 'scissors':
        if computer == 'rock':
            print('You lose!,computer smashes player')
        else:
            print('You won!,player cut computer')
    else:
        print('That is not a valid play ,check your spelling!!!')
        #player was set to true,but we want it to be False so the loop continues
    player = False
    computer = spam[random.randint(0,2)]
        
        
        
