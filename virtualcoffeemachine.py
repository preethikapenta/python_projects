cappuccino={'Water':50,'milk':150,'coffee':100}
expresso={'Water':100,'milk':53,'coffee':23}
resourcesleft={'Water':1000,'milk':2000,'coffee':750}
latte={'Water':112,'milk':200,'coffee':35}
profit=0
def coffee_machine():
    global profit
    cost={ 'cappuccino':35,'latte':45,'expresso':25}

 

    serve=input('What would you like to have? (latte/expresso/cappuccino): ')
    if serve=='off':
        exit()
    
    elif serve=='cappuccino':
        for item in cappuccino:
            if cappuccino[item]<=resourcesleft[item]:
                can=True
            else:
                deficient=item
                can=False
                break
        if can==True:
            print('please insert coins')
            five=int(input('How many 5Rs. coins: '))
            ten=int(input('How many 10Rs. coins:  '))
            twenty=int(input('How many 20Rs. coins: '))
            final=five*5+ten*10+twenty*20
            if final<cost[serve]:
                print('Sorry That\'s not enough money.Money refunded')
                coffee_machine()
         
            elif final>cost[serve]:
                retur=final-cost[serve]
                print('Here is your',retur,' change.')
                profit+=cost[serve]
                print('Here is your',serve)
                for resource in resourcesleft:
                    resourcesleft[resource]=resourcesleft[resource]-cappuccino[resource]
                coffee_machine()
            else:
                print('Here is your',serve)
                profit+=cost[serve]
                for resource in resourcesleft:
                    resourcesleft[resource]=resourcesleft[resource]-cappuccino[resource]
                coffee_machine()
        else:
            print('Sorry there is not enough',deficient)
            coffee_machine()
    elif serve=='expresso':
        for item in expresso:
            if expresso[item]<=resourcesleft[item]:
                can=True
            else:
                deficient=item
                can=False
                break
        if can==True:
            print('please insert coins')
            five=int(input('How many 5Rs. coins: '))
            ten=int(input('How many 10Rs. coins:  '))
            twenty=int(input('How many 20Rs. coins: '))
            final=five*5+ten*10+twenty*20
            if final<cost[serve]:
                print('Sorry That\'s not enough money.Money refunded')
                coffee_machine()
         
            elif final>cost[serve]:
                retur=final-cost[serve]
                print('Here is your',retur,' change.')
                profit+=cost[serve]
                print('Here is your',serve)
                for resource in resourcesleft:
                    resourcesleft[resource]=resourcesleft[resource]-expresso[resource]
                coffee_machine()
            else:
                print('Here is your',serve)
                profit+=cost[serve]
                for resource in resourcesleft:
                    resourcesleft[resource]=resourcesleft[resource]-espresso[resource]
                coffee_machine()
        else:
            print('Sorry there is not enough',deficient)
            coffee_machine()
    elif serve=='latte':
        for item in latte:
            if latte[item]<=resourcesleft[item]:
                can=True
            else:
                deficient=item
                can=False
                break
        if can==True:
            print('please insert coins')
            five=int(input('How many 5Rs. coins: '))
            ten=int(input('How many 10Rs. coins:  '))
            twenty=int(input('How many 20Rs. coins: '))
            final=five*5+ten*10+twenty*20
            if final<cost[serve]:
                print('Sorry That\'s not enough money.Money refunded')
                coffee_machine()
         
            elif final>cost[serve]:
                retur=final-cost[serve]
                profit+=cost[serve]
                print('Here is your',retur,' change.')
                print('Here is your',serve)
                for resource in resourcesleft:
                    resourcesleft[resource]=resourcesleft[resource]-latte[resource]
                coffee_machine()
            else:
                print('Here is your',serve)
                profit+=cost[serve]
                for resource in resourcesleft:
                    resourcesleft[resource]=resourcesleft[resource]-latte[resource]
                coffee_machine()
        else:
            print('Sorry there is not enough',deficient)
            coffee_machine()
    elif serve=='report':
        print('\n','Water: ',resourcesleft['Water'],'\n','milk: ',resourcesleft['milk'],'\n','coffee: ',resourcesleft['coffee'],'\n','Money: ',profit)
        coffee_machine()


coffee_machine()




       



   
   


   
        
                
    


   
    
        
