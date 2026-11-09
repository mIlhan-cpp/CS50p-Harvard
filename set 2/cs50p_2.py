# i=3
# while i!=0:
#     print('meow')
#     i-=1

# for _ in range(1): #_ is used for default integer value counting purpose/iterating for understanding purpose no compulsion
#     print('meow')

# print('meow \n'*3, end="")

# i=int(input("enter a num"))
# while i>0:
#     print("Positive")
    #   i-=1  
# else:
#     print('negative')    

# def main():
#     num=get_num()
#     meow(num)

# def get_num():
#     while true:
#         num=int(input("enter a num"))
#         if num>0:
#             return num # return breaks the loop so no extra break needed


# def meow(num):
#     for _ in range(num):
#         print('meow')
# main()


# students=['har','herm','ron'] #list

# for _ in range(len(students)):
#     print(_+1,students[_])

# students={'harry':'gryffindor',
#           'ron':'gryffindor',
#           'hermoine':'gryffindor',
#           'draco':'slytherin'
#           }
# for stud in students:
#     print(stud) #gives key values only as for loop iterates over keys
#     print(stud,students[stud],sep=', ')

# list_of_dic=[{'name':'ronaldo','club':'saudi','team':'portugal;'},
#              {'name':'messi','club':'inter miami','team':'argentina'},
#              {'eman':'neymar','bulc':'los santos','maet':'brazil'}]

# for _ in list_of_dic:
#     print(_['name'])

# for i in range(3):
#     print("?"*i)

# def main():
#     get_num(4)

# def get_num(h):
      # print('?'*h) #for horiziontal lines printing

# main()

def main():
    square_block(4)

def square_block(h):
    for i in range(h):
        for j in range(h):
            print('?',end='')
        print()

main()