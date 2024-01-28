print('This is your friend which helps you in 4 major arithmetic calculations.')
ask1=int(input('Enter the first number: '))
def calculator():
    global ask1
   
  
    
        
    print('+','-','*','/',sep='\n')
    
    ask2=input('pick an operation: ')
    ask3=int(input('Enter the second number: '))
    if ask2=='+':
        ans=ask1+ask3
    elif ask2=='-':
        ans=ask1-ask3
    elif ask2=='*':
        ans=ask1*ask3
    elif ask2=='/':
        ans=ask1/ask3
    print(f'{str(ask1)} {ask2} {str(ask3)} = {ans}')
   
        


   
   
    ask4=input(f'Enter \'y\'to continue calculation with {ans} or \'n\' to start new calculation or \'x\' to exit: ')
    if ask4=='y':
        ask1=ans
        calculator()
       
    elif ask4=='n':
        ask1=int(input('Enter the first number: '))
        calculator()
    else:
        exit()
calculator()      