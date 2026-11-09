i=input('Input: ')
print('Output: ',end='')
for _ in i:
    if _.lower() in ['a','e','o','i','u']:
        print(end='')
    else:
        print(_,end='')
