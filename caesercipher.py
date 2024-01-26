print('Secure your code or crack the code using Caesercipher..!')

def caeser_cipher():
    totallist=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    what=input('Type \'encrypt\' for encryption and type \'decrypt\' for decryption: ')
    if what=='encrypt':
        give=input('Type your message: ')
        shift=int(input('Type the shift number: '))
        ans=''
        for l in give.upper():
            get=totallist.index(l)
            
            eleind=(get+shift)%26
            ans+=totallist[eleind]
        print('Here is your encrypted message:', ans)
        replay=input('Type \'yes\' if you want to go again otherwise type \'no\' ')
        if replay.lower()=='yes':
            caeser_cipher()
        else:
            exit()
    elif what.lower()=='decrypt':
        give=input('Type your message: ')
        shift=int(input('Type the shift number: '))
        ans=''
        for l in give.upper():
            get=totallist.index(l)
            
            eleind=(get-shift)%26
            if eleind<0:
                eleind=eleind+26
            ans+=totallist[eleind]
        print('Here is your encrypted message:', ans)
        replay=input('Type \'yes\' if you want to go again otherwise type \'no\' ')
        if replay.lower()=='yes':
            caeser_cipher()
        else:
            exit()
    else:
        exit()

caeser_cipher()


   