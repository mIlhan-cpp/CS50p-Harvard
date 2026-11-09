import inflect

p =inflect.engine()
name=[]
while True:

    try:
        names = input('Name: ')
        name.append(names)

    except EOFError:
        print()
        break

print('Adieu, adieu, to '+p.join(name))