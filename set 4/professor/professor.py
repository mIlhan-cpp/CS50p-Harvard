import random


def main():
    score=0
    level=get_level()
  
    for _ in range(10): 
        attempt=0
        x=generate_integer(level)
        y=generate_integer(level)
        while attempt<3:
            try:
                o=int(input(f'{x} + {y} = '))
                if o==x+y:
                    score+=1
                    break
                else:
                    print('EEE')
                    attempt+=1
            except ValueError:
                pass
        print(f'{x} + {y} = {x+y}')
            
    print('score:',score)

def get_level():
   
    while True:
       
        try: 
            level=int(input('Level:'))
            if 3>=level>=1:
                return level
        except ValueError:
            pass 



def generate_integer(level):

    if level==1:
        x=random.randint(0,9)

    elif level==2:
         x=random.randint(10,99)
   
    elif level==3:
         x=random.randint(100,999)
  
        
    return x


if __name__ == "__main__":
    main()