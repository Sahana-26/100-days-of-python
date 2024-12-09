import random

def draw_cards(cards):
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def sum_cards(cards):
    if sum(cards) >=21 and sum(cards) == 0:
        return 0
    if 11 in cards and sum(cards)>=21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, comp_score):
    if user_score>21 and comp_score>21:
        return 'User win the game'
    elif comp_score>=21:
        return 'opponent went over, you win'
    elif user_score>=21:
        return 'you went over'
    elif user_score == comp_score:
        return 'its a draw match'
    elif user_score == 0:
        return 'you win with a blackjack'
    elif comp_score == 0:
        return 'opponent wins with a blackjack'
    else:
        return 'you lose'
   
def play_game():
    user_cards = []
    comp_cards = []
    to_play = True

    for i in range(2):
        user_cards.append(draw_cards(user_cards))
        comp_cards.append(draw_cards(comp_cards))

    while to_play:
        user_score = sum_cards(user_cards)
        comp_score = sum_cards(comp_cards)
        print(f'User cards : {user_cards}, user score : {user_score}')
        print(f'comp first card : {comp_cards[0]}')

        if user_score==0 or comp_score==0 or user_score>21:
            to_play=False
        else:
            choice = input('Do u want to draw card (y) or stand (n) : ')
            if choice == 'y':
                user_cards.append(draw_cards(user_cards))
            else:
                to_play=False
    
    while comp_score!=0 and comp_score<17:
        comp_cards.append(draw_cards(comp_cards))
        comp_score = sum_cards(comp_cards)
    
    print(f'User cards : {user_cards}, final score : {user_score}')
    print(f'comp card : {comp_cards}, final score : {comp_score}')

    print(compare(user_score, comp_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()