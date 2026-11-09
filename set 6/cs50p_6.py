# names=[]
# for _ in range(3):
#     names.append(input('whats your name:'))
# print('hello',names)
# print(names)

# for name in sorted(names):
#     print('hello',name)

# name= input('whats your name:')
# file=open('names.txt','w')
# w used to write so every command will change instead of adding to previous command
# file.write(name)
# file.close()


# name= input('whats your name:')
# file=open('names.txt','a') 
# output is mixed example hairyron not hairy ron
# file.write(name)
# file.close()

# name= input('whats your name:')
# file=open('names.txt','a') 
# a is for appending
# file.write(f'{name}\n')
# file.close()

# name= input('whats your name:')
# with open('names.txt','a') as file:
#     file.write(f'{name}\n')



# with open('names.txt','r') as file:
#     read=file.readlines()
#with auto closees file
# for line in read:
#     print('hello',line.rstrip())


# with open('names.txt','r') as file:
#     for line in file:
#         print('hello',line, end='')

# name=[]
# with open('names.txt') as file: #no need to specify read explicitly
#     for line in file:
#         name.append(line.rstrip())
# for names in sorted(name):
#     print(names,' hello')

# name=[]
# with open('names.txt') as file: #no need to specify read explicitly
#     for line in sorted(file):
#         print(line.rstrip(),'hello')



# with open('names.csv') as file:
#     for line in sorted(file,reverse=True):
#         x=line.rstrip().split(',')
#         print(x[0],'is in',x[1])

# students=[]
# with open('names.csv') as file:
#     for line in file:
#         names,house=line.rstrip().split(',')
#         student={'names':names,'house':house}
#         students.append(student)

# def get_name(student):
#     return student['names']

# for student in sorted(students,key=get_name,reverse=True):
#     print(student['names'],'is in',student["house"])


# students=[]
# with open('names.csv') as file:
#     for line in file:
#         names,house=line.rstrip().split(',')
#         student={'names':names,'house':house}
#         students.append(student)


# for student in sorted(students,key=lambda student:student['names']):
# #if a function is needed to bee used once lambda is used instead of creating a function fot dirct usage
#     print(student['names'],'is in',student["house"])


# import csv

# students=[]
# with open('names.csv') as file:
#    reader=csv.reader(file)
#    for row in reader:
#        students.append({'names':row[0],'home':row[1]})

# for student in sorted(students,key=lambda student:student['home']): 
#     print(student['names'],'is in',student["home"])


# import csv

# students=[]
# with open('names.csv') as file:
#    reader=csv.DictReader(file) #dict reader uses first row as headers
#    for row in reader:
#        students.append({'names':row['name'],'home':row['home']})

# for student in sorted(students,key=lambda student:student['home']):
#   print(student['names'],'is in',student["home"])

# import csv

# name=input('whats your name:') 
# home=input('whats your home:')

# with open('names.csv','a') as file:
#     writer=csv.writer(file)
#     writer.writerow([name,home])


# import csv

# name=input('whats your name:') 
# home=input('whats your home:')

# with open('names.csv','a') as file:
#     writer=csv.DictWriter(file,fieldnames=["name",'home'])
#     writer.writerow({'name':name,'home':home})


import sys
from PIL import Image
images=[]

for arg in sys.argv[1:]:
    image=Image.open(arg)
    images.append(image)

images[0].save("costumes.gif",save_all=True, append_images=[images[1]],duration=200,loop=0)