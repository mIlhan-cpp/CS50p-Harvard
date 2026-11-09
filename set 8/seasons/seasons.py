from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    x=input('Born in')
    try:
        x = date.fromisoformat(x)
    except ValueError:
        sys.exit("Invalid date")     
    y=date.today()
    print(cal(x,y))
   
def cal(x,y):
        z=y-x
        days=z.days
        a=days*24*60
        return f'{p.number_to_words(a,andword=' ').capitalize()} minutes'


if __name__ == "__main__":
    main()