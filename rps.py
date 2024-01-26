#PROJECT-1 ROCK-PAPER-SCISSORS.
import random
print('Welcome to the game Rock,Paper and scissors..!')
score=0
def rockPaperScissors():
    global score
  
    rock='''
         -------
    ----'       )
         (------)
         (------)
    ---  (------)
      --(-----)'''
    
    scissors='''
        -------
    ----    ---)-----
                -----)
            ---------)
    ----    (---)
        ----(---)'''
    
    papers='''
            ----)---
    ----        ----)
            ----------)
    ----       -----)
        ----------)'''
    ans=[rock,papers,scissors]
   

    
    
    user=int(input('enter a number,type 0 for rock, 1 for paper ,2 for scissors: '))
    comp=random.choice([0,1,2])
    if user!=0 and user!=1 and user!=2:
        print('sorry you have given the wrong input, try again')
        rockPaperScissors()
    if user==comp:
        print('its a draw')
        print('yours choice is ',ans[user],'\n','computers choice is',ans[comp],sep='')
        print('to continue the game click yes')
        new=input()
        if new.lower()=='yes':
            rockPaperScissors()
        else:
            print('your score is ',score)
            print('Thank you')
            exit()
    elif user==2 and comp==0:
        print('You Lost')
        print('yours choice is ',ans[user],'\n','computers choice is ',ans[comp],sep='')
        print('if you want to continue the game click yes')
        new=input()
        if new.lower()=='yes':
            rockPaperScissors()
        else:
            print('Thank you')
            print('your score is ',score)
            exit()
    elif user==0 and comp==2:
        score+=1
        print('You Won the game')
        print('yours choice is ',ans[user],'\n','computers choice is ',ans[comp],sep='')

        print('if you want to continue the game click yes')
        new=input()
        if new.lower()=='yes':
            rockPaperScissors()
        else:
            print('your score is ',score)
            print('Thank you')
            exit()
    elif comp>user:
        print('You Lost')
        print('yours choice is ',ans[user],'\n','computers choice is ',ans[comp],sep='')
        print('if you want to continue the game click yes')
        new=input()
        if new.lower()=='yes':
            rockPaperScissors()
        else:
            print('your score is ',score)
            print('Thank you')
            exit()
    elif comp<user:
        score+=1
        print('You won the game')
        print('yours choice is ',ans[user],'\n','computers choice is ',ans[comp],sep='')
        print('if you want to continue the game click yes')
        new=input()
        if new.lower()=='yes':
            rockPaperScissors()
        else:
            print('your score is ',score)
            print('Thank You')
            exit()
rockPaperScissors()
    
        


