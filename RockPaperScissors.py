import random
print("Welcome to Rock Paper Scissors")
print("Guide")
print(" 1 : Rock \n 2 : Paper \n 3 : Scissors")
turns = 3
user_points = 0
comp_points = 0
while(turns>0):
    user = int(input("Enter your choice : "))
    comp = random.randint(1,4)
    print('your_choice :', user)
    print('comp_choice :', comp)
    if (user == 1 and comp == 2) or (user == 3 and comp == 1) or (user == 2 and comp == 3):
        comp_points+=1
        print("computer got a point ")
    else:
        user_points+=1
        print("you got a point")
    turns-=1

if comp_points > user_points:
    print('Sorry you lost the game')
elif comp_points == user_points:
    print('Its a draw')
else:
    print('You Won!!!!')

