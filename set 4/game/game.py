import random 
import sys

while True:
    try:
        a=int(input('Level:'))
        if a>0:
            x=random.randint(1,a)
            while True:
                y=int(input('Guess:'))
                if y>0:
                    if x==y :
                        print('Just right!')
                        sys.exit()
                    elif x>y:
                        print('Too small!')
                    elif x<y:
                        print('Too large!')
        
    except ValueError:
        continue
