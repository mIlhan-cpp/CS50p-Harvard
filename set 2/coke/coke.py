
amount=50
while amount>0:
     print('Amount Due:',amount)
     y=int(input('Insert coin:'))
     if(y==5 or y==25 or y==10):
       amount=amount-y
if (amount<0):
    print('change owed:',amount-(2*amount)) 
else:
    print('Change Owed: 0')           