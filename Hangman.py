print("Let\'s play Hangman")
import random
items=['apple','banana','mango','pineapple','custardapple','strawberry']
item=random.choice(items)
user_list=[]
for i in range(len(item)):
    user_list+='-'
comp_list=[]
for j in item:
    comp_list+=j

image='''
     +---+
     |   |
         |
         |
         |
         |
    -------
    -------'''
img0='''
     +---+
     |   |
     0   |
         |
         |
         |
    -------
    -------'''
img1='''
     +---+
     |   |
     0   |
     |   |
         |
         |
    -------
    -------'''
img2='''
     +---+
     |   |
     0   |
    /|   |
         |
         |
         |
    -------
    -------'''
img3='''
     +---+
     |   |
     0   |
    /|\  |
         |
         |
         |
    -------
    -------'''
img4='''
     +---+
     |   |
     0   |
    /|\  |
    /    |
         |
    -------
    -------'''
img5='''
     +---+
     |   |
     0   |
    /|\  |
    / \  |
         |
    -------
    -------'''
count=-1
print('You have only 6 lives so try to gueess the word within 6 attempts Good luck !!')
current_img=image
def Hangman():
    global count
    global current_img
    global image
    global img0
    global img1
    global img2
    global img3
    global img4
    global img5
    ask=input('Guess a letter: ')
    
    img=[img0,img1,img2,img3,img4,img5]
 
    if ask in comp_list:
        get=comp_list.index(ask)
        user_list[get]=ask
      
        comp_list[get]=0
        if user_list==['a','p','p','l','e']:
            print(user_list)
            print('You win')
            print(current_img)
            exit()
        else:
            print(user_list)
            print(current_img)
            Hangman()
    
    else:
        count+=1
        if count==len(item)-1:
            print('You guessed',ask,'that is not present in the word, So you lose a life.')
            print('You lose')
            print(user_list)
            current_img=img[count]
            print(current_img)
            exit()
        else:
            
            print('You guessed',ask,'that is not present in the word, So you lose a life.')
            print(user_list)
            current_img=img[count]
            print(current_img)
            Hangman()
Hangman()

        
        
    


    

