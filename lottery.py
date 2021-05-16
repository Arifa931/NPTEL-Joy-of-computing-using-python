import random
account=0
for i in range(10):
    
    bet=random.randint(1,10)
    print("Bet: ",bet)
    lucky_draw=random.randint(1,10)
    print("Lucky draw",lucky_draw)
    
    if(bet==lucky_draw):
        print('Winner')
        account=account+1000-100
        print('Amount in your account: ',account)
    else:
        print('Loser')
        account=account-100
        print('Amount in your account: ',account)
    
