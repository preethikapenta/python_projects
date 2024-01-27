
higher='''
_ __ ___ _  _ ____ ____    __    __  _  _ ____ ____     ___  __  _  _ ____       
/ )( (  / __/ )( (  __(  _ \  (  )  /  \/ )( (  __(  _ \   / __)/ _\( \/ (  __)      
) __ ()( (_ ) __ () _) )   /  / (_/(  O \ /\ /) _) )   /  ( (_ /    / \/ \) _)       
\_)(_(__\___\_)(_(____(__\_)  \____/\__/(_/\_(____(__\_)   \___\_/\_\_)(_(____)      
'''
vs='''
 _  _ ____ 
/ )( / ___)
\ \/ \___ \
 \__/(____/
 '''
import random
import os

database=[{'name':'preethika',
           'followers':2,
           'description':'student',
           'country':'India'},
          {'name':'joshika',
           'followers':20,
           'description':'student',
           'country':'India'},
          {'name':'harika',
           'followers':25,
           'description':'Homemaker',
           'country':'India'},
          {'name':'janardhana',
           'followers':200,
           'description':'head of the family',
           'country':'India'},
          {'name':'kavya',
           'followers':56,
           'description':'bevarse',
           'country':'India'},
          {'name':'chimpu',
           'followers':0,
           'description':'player',
           'country':'India'},
          {'name':'lalitha',
           'followers':0,
           'description':'graduate',
           'country':'India'}]
score=0
def higherlower():
    global higher
    global score
    global vs
    get=random.choice(database)
    
    print(higherlower)
    print('Compare 1:',get['name'],get['description'],'from',get['country'])
    print(vs)
    get2=random.choice(database)
    while get2==get:
        get2=random.choice(database)

    print('Compare 2', get2['name'],get2['description'],'from',get2['country'])
    ask=int(input('Who has more followers? Type 1 or 2: '))
    if ask==1:
        if get2['followers']>get['followers']:
            score+=1
            print(f'You are right.Your score is {score}.')
            os.system('cls')
            higherlower()
        else:
            print(f'You are wrong.. Your final score is {score}.')
            exit()
    else:
        if get['followers']>get2['followers']:
            score+=1
            print(f'You are right.Your score is {score}.')
            os.system('cls')
            higherlower()
        else:
            print(f'You are wrong.. Your final score is {score}.')
            exit()

higherlower()

          
