##NO. GUESSINGN GAME
import random
while True:
    a=int(input('Guess the number(1 to 10) or press 0 to end the game'))
    b=random.randint(1,10)
    if a==0:
        print('PRESS 0 TO END THE GAME')
        break
    if a==b:
        print('You won')
    elif(a>10):
        print('guess no. from 1 to 10')

    else:
        print('You Lost')
        print('Ramdom number is',b)
