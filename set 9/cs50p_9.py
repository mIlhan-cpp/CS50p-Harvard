# student=[{'name':'m','job':'unemp'},
#          {'name':'s','job':'ass'}]

# houses=[]
# for st in student:
#     if st['job'] not in houses:
#         houses.append(st['job'])
# print (houses)


# student=[{'name':'m','job':'unemp'},
#          {'name':'s','job':'ass'},
#          {'name':'d','job':'asss'}]

# houses=set()
# for st in student:
#         houses.add(st['job'])
# print (houses)

# balance=0 


# def main():
#     print('balance:',balance)
#     withdraw(100)
#     deposit(20)
#     print('balance:',balance)


# def withdraw(n):
#     balance-=n
#     return balance

# def deposit(n):
#     balance+=n
#     return balance

# if __name__=='__main__':
#     main()


# balance=0 

# def main():
#     print('balance:',balance)
#     withdraw(100)
#     deposit(20)
#     print('balance:',balance)


# def withdraw(n):
#     global balance
#     balance-=n
#     return balance

# def deposit(n):
#     global balance #using global makes you write values
#     balance+=n
#     return balance

# if __name__=='__main__':
#     main()


class account:
    def __init__(self):
        self._balance=0

    @property
    def balance(self):
        return self._balance
    def withd(self,n):
        self._balance -= n
    def depo(self,n):
        self._balance+=n

def main():
    Acc=account()
    Acc._balance=100
    Acc.withd(45)
    Acc.depo(100)
    print(Acc._balance)

if __name__=='__main__':
    main()