import random
def guessthenumber():
    task=input('Do you need \'easy\' or \'hard\'')
    if task=='easy':
        attempts=10
    else:
        attempts=5
    number=random.randint(1,100)
    while attempts>0:
        ask=int(input('Guess the number: '))
        if ask==number:
            if task=='easy':
                print(f'You guessed the number in {10-attempts} attempts.')
                exit()
            else:
                print(f'You guessed the number in {5-attempts} attempts.')
                exit()
            
        elif ask>number:
            print(f'the number you guessed is too high.')
            attempts-=1
            if attempts==0:
                print('The game ended')
        else:
            print(f'the number you guessed is too low.')
            attempts-=1
            if attempts==0:
                print('The game ended')
guessthenumber()
