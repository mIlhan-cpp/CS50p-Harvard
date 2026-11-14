# import os

# print(__file__)
# name=input("whats your name. ").title()

# print(f"hello  {name}")
# print()

# x=float(input("whats x"))
# y=float(input("whats y"))
# z=round(x+y)
# print(f"{z:,}")

# def hello(to="milhan"):
#      print("hello, ", to)
# def main():
#          name=input("whats your name ")
#          hello(name)     
# main()

def main():
    x=int(input("value of x "))
    print ("squared x is", square(x))

def square(x):
    return x * x 
# pow(x,2) or n**2 will equal x square 
# return is used to pass values to other function print not used here

main()