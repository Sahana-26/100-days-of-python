import random

def guess_the_number(attempts):
    while(attempts>0):
        guess = int(input(f'enter your guess ({attempts} attempts remaining)'))
        if number == guess:
            print('exactly right!!!!')
            exit()
        elif number>guess:
            print("you're guessing too low")
        else:
            print("you're guessing too high")
        attempts-=1
    if attempts==0:
        print(f"you lost! number is {number}")
    

print("Guess the number")
number = random.randint(1,100)

choice = input('enter the level .... type "easy" or "hard"')
if choice == 'easy':
    guess_the_number(10)
else:
    guess_the_number(5)
    
       





