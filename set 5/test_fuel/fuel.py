

   

def main():
    while True:
        try:
            Frac = input("Fraction: ")
            x=convert(Frac)
            print(gauge(x))
        except (ValueError, ZeroDivisionError):
                    pass

def convert(Frac):

            x, y = Frac.split("/")
            x=int(x)
            y=int(y)
        
            if x > y or x < 0 or y <= 0:
                raise ValueError
            result = x / y * 100
            return result
        
       


def gauge(result):
     if result<=1:
        return  'E'
     elif result>=99:
        return "F"
     else:
        return f'{round(result)}%'  


if __name__ == "__main__":
    main()
