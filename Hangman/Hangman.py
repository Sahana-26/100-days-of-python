import random,time
import Hangman_words as hangman_words
import Hangman_art as hangman_art

word_choice = random.choice(hangman_words.word_list)

logo = hangman_art.logo
print(logo)

stages = hangman_art.stages
# print(word_choice)
gap= ['_']*len(word_choice)


total_chances = len(word_choice)

i=total_chances
k=6
while(i>0):
    guess = input('enter your guess')
    for j in range(len(word_choice)):
        letter = word_choice[j]
        if letter == guess:
            gap[j]=letter
            i+=1
            print('correct guess')        
    if guess not in word_choice:
        print('wrong guess')
        print(stages[k])
        k-=1
        i-=1
    print(' '.join(gap))
    print('total chances left : ',i)

if '_' in gap:
    print('you lost the game! Answer is', word_choice)

else:
    print('you won')

    
