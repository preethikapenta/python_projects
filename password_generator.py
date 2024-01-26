print('Welcome to the password generator....!')
def password_generator():
    import random
    number_list=['0','1','2','3','4','5','6','7','8','9']
    letter_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    symbol_list=['!','@','#','$','%','^','&','*','(',')','~','|',';',':','.',',']
    askn=int(input('How many numbers do you want in your password: '))
    askl=int(input('How many letters do you want in your password: '))
    asks=int(input('How many symbols do you want in your password: '))
    ans=[]
    more=''
    for i in range(askn):
        ans.append(random.choice(number_list))
    for j in range(askl):
        ans.append(random.choice(letter_list))
    for k in range(asks):
        ans.append(random.choice(symbol_list))
    recquire=input('Do you want shuffled pw or normal one click yes if you want shuffled or else no: ')
    if recquire.lower()=='yes':
         
        random.shuffle(ans)
        new=''
        for g in ans:
            new=new+g
        print('Here is your recquired password:',new)
    elif recquire.lower()=='no':
        new=''
        for g in ans:
            new=new+g
        print('Here is your recquired password:',new)
    else:
        print('its ended.')


   

    
       

   
   
  
password_generator()
    


             
