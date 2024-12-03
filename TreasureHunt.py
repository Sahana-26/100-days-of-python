print("Welcome to the Treasure Island \n your mission is to find the treasure")

q1 = input("You are at a cross road. Where do you want to go? Type 'left' or 'right'\n")

if q1.lower() == 'left':
    q11 = input("You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n")
    if q11.lower() == 'wait':
        q111 = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
        if q111.lower() == 'yellow':
            print("You win!!!!!!!!!") 
            exit()
        else:
            print("Game Over")
            exit()
    else:
        print("Game Over")
        exit()
else:
    print("Game Over")
    exit()