


while True:
    Frac = input("Fraction: ")
    
    try:
        x, y = Frac.split("/")
        x=int(x)
        y=int(y)
       
        if x>y or x<0 or y<=0:
            continue
        result= x/y *100
        if result<=1:
            print('E')
        elif result>=99:
            print("F")
        else:
            print(f'{round(result)}%')        
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break    

