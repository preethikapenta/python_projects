print('Welcome to the Silent Auction Programme.')
import os
store={}
def silent_auction():
    
    name=input('What is your name: ')
    bid=int(input('What is your Bid: '))
    store[name]=bid
    ask=input('Are there any other bidders?Type \'yes\' or \'no\'')
    if ask=='yes':
        os.system('cls')
        silent_auction()
    elif ask=='no':
        maxi=max(store.values())
        for i in store.keys():
            if store[i]==maxi:
                ans=i

      
        print('The winner is',ans,'with a bid of',maxi,'.')
    else:
        exit()
silent_auction()
