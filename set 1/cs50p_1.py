# x=input('enter value of x')
# y=input('enter value of y')

# if x>y:
#     print('x bada hai')
# elif x<y:
#     print('x  chota hai')
# else :
#     print('x y  chota hai')

# if x!=y:
#     print('magic')
    
# score=int(input('Enter a grade'))

# if 40<score<50:
#     print('E grade')
# elif score>50 :
#     print('D grade')
# elif score>60 and score<70:
#     print('C grade')
# elif score>70 and score<80:
#     print('B grade')
# elif score>80 and score<90:
#     print('A grade')

# def main():
#     x=int(input('Enter a num '))
#     if is_even(x):
#         print(x," is even")
#     else:
#         print("odddd")

# def is_even(x):
#     # if x%2==0:
#     #     return True
#     # else:
#     #     return False
#     # return True if x%2==0 else False 
#     return x%2==0 #this also returns boolean
# main()

name=input()

match name:
    case "Harry":       #case "harry"|"herru"|"ron"
        print("Aashiq")
    case "herru":
        print("bewafa")
    case "ron":
        print("Bewafa ka mashooq")
    case default: #case _ does same
        print("chal")    
