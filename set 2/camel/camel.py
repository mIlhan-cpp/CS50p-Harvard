i=input('camelCase:')
print('snake_case:',end='')
for _ in i:
    if _.isupper():
        print('_'+_.lower(),end='')
    else:
        print(_,end='')   