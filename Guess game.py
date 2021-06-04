import random
logo='''
   ___                                        _     _                                          _                    
  / __|  _  _    ___    ___    ___     o O O | |_  | |_     ___     o O O _ _    _  _   _ __  | |__    ___     _ _  
 | (_ | | +| |  / -_)  (_-<   (_-<    o      |  _| | ' \   / -_)   o     | ' \  | +| | | '  \ | '_ \  / -_)   | '_| 
  \___|  \_,_|  \___|  /__/_  /__/_  TS__[O] _\__| |_||_|  \___|  TS__[O]|_||_|  \_,_| |_|_|_||_.__/  \___|  _|_|_  
_|"""""_|"""""_|"""""_|"""""_|"""""|{======_|"""""_|"""""_|"""""|{======_|"""""_|"""""_|"""""_|"""""_|"""""_|"""""| 
"`-0-0-"`-0-0-"`-0-0-"`-0-0-"`-0-0-./o--000"`-0-0-"`-0-0-"`-0-0-./o--000"`-0-0-"`-0-0-"`-0-0-"`-0-0-"`-0-0-"`-0-0-' 

'''
Win='''
                                
 __ __ _____        _ _ _ _     
|  |  |     |_ _   | | | |_|___ 
|_   _|  |  | | |  | | | | |   |
  |_| |_____|___|  |_____|_|_|_|
                                
'''
Lose= '''
                                      
 __ __ _____        __                
|  |  |     |_ _   |  |   ___ ___ ___ 
|_   _|  |  | | |  |  |__| . |_ -| -_|
  |_| |_____|___|  |_____|___|___|___|
                                      
'''
print(logo)
start=input("Do you wanna start the game? y/n \t")
level=(input("Enter the mode you wanna play hard or easy?:\t")).lower()
Winner_number=random.randint(0,100)

def making_guess(got):
    if got == Winner_number:
        print(Win)
        exit()
    elif got< Winner_number:
        print("Too low")
    elif got> Winner_number:
        print("Too High")



if(start=='y'):

    if (level== "easy"):
        chance=10
        for _ in range(0,10):
            got = int(input("Enter the number\t:"))
            making_guess(got)
            chance-=1
            print(f"You have {chance} attempts left")
            if chance==0:
                print(Lose)
                exit()


    elif(level=='hard'):
        chance=5
        for _ in range(0,5):
            got = int(input("Enter the number\t:"))
            making_guess(got)
            chance -= 1
            print(f"You have {chance} attempts left")
            if chance==0:
                print(Lose)
                exit()

    else:
        print("Wrong input!!")




