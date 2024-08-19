import random
from replit import clear

test_list = [ 222, 3232,444,1,44,55,100]
score =0
play = True
choice_B = random.choice(test_list)\

while play == True:
    choice_A = choice_B
    choice_B = random.choice(test_list)
    
    if choice_A == choice_B:
        choice_B = random.choice(test_list)
    print('pick who is bigger: ')
    print('press(A) for : ' +str(choice_A))
    print('press(B) for : '+str(choice_B))
    answer = input().upper()
    if answer =="A":
        if choice_A > choice_B:
            print('got it')
            score= score+1
            print('ur score is: '+str(score))
        else:
            print('wrong answer')
            score=score
            print('ur score is: '+str(score))
            play= False
    elif answer =="B":
        if choice_B > choice_A:
            print('got it')
            score= score+1
            print('ur score is: '+str(score))
        else:
            print('wrong answer')
            score=score
            print('ur score is: '+str(score))
            play= False