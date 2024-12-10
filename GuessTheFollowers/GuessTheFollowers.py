from game_data import data
import random

def get_data():
    value = random.choice(data)
    return value

li=[]
for _ in range(2):
    li.append(get_data())
score=0
continue_game = True

while(continue_game):
    print(f'A. {li[0]['name']}, {li[0]['description']}, {li[0]['country']}')
    print(f'B. {li[1]['name']}, {li[1]['description']}, {li[1]['country']}')

    ans = max(li[0]['follower_count'], li[1]['follower_count'])

    choice = input('Who do you think has more followers? "A" or "B" : \n')

    if li[0]['follower_count']==ans and choice.lower() == "a":
        print('correct guess')
        li.pop(0)
        li.append(get_data())
        score+=1
        print('current score : ',score)

    elif li[1]['follower_count']==ans and choice.lower() == "b":
        print('correct guess')
        li.pop(0)
        li.append(get_data())
        score+=1
        print('current score : ',score)
        
    else:
        print('Wrong guess....total score is : ', score)
        continue_game=False
    
    
    
    
