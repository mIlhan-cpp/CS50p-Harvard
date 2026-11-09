
# name=input('name:')
# house=input('house:')

# print('name is',name,'house is', house)


# def main():
#     name=get_name()
#     house=get_house()

#     print('name is',name,'house is', house)

# def get_name():
#     return input('name:')

# def get_house():
#     return input('house:')


# def main():
#     name,house=get_student()

#     print('name is',name,'house is', house)

# def get_student():
#     name=input('name:')
#     house=input('house:')
#     return name,house

# if __name__=='__main__':
#     main()


# def main():
#     student=get_student()

#     print('name is',student[0],'house is', student[1])

# def get_student():
#     name=input('name:')
#     house=input('house:')
#     return (name,house) #is a tuple and contents cannot be changed [name,house] will be a list indexing is done using [0] only

# if __name__=='__main__':
#     main()


# def main():
#     student=get_student()
#     if student['name']=='padma':
#         student['house']='ravenclaw'
#     if student['house'] not in ['ravenclaw','gryffindor','hufflepuff','slytherin']:
#         student['house']='maglu'
#     print('name is',student["name"],'house is', student['house'])

# def get_student():
#     student={}
#     student['name']=input('name:')
#     student['house']=input('house:')
#     return student
# if __name__=='__main__':
#     main()

# class Student:
#     def __init__(self,name,house):
#         if not name :
#             raise ValueError('missing name')
#         if house not in ['ravenclaw','gryffindor','hufflepuff','slytherin']:
#             raise ValueError('No such House')
      
#         self.name=name
#         self.house=house



# def main():
#     student=get_student()
#     print('name is',student.name,'house is', student.house)

# def get_student():
 
#     name=input('Name:')
#     house=input('house:')
#     return Student(name,house)


# if __name__=='__main__':
#     main()


# class Student:
#     def __init__(self,name,house,patro):
#         if not name :
#             raise ValueError('missing name')
#         # if house not in ['ravenclaw','gryffindor','hufflepuff','slytherin']:
#         #     raise ValueError('No such House')
      
#         self.name=name
#         self.house=house
#         self.patro=patro
#     def __str__(self): #__str__ is pythons inbuilt
#         return f"{self.name} from {self.house}"
#     def ch(self):
#         match self.patro:
#             case "stag":
#                 return "emoji1"
#             case "otter":
#                 return "emoji2"
#             case _:
#                 return "random"


# def main():
#     student=get_student()
#     print(student) #will automatically print __str__ return 
#     print("Expecto patro",student.ch())
# def get_student():
 
#     name=input('Name:')
#     house=input('house:')
#     patro=input('Patro:')
#     return Student(name,house,patro)


# if __name__=='__main__':
#     main()



# class Student:
#     def __init__(self,name,house):
#         if not name :
#             raise ValueError('missing name')
#         # if house not in ['ravenclaw','gryffindor','hufflepuff','slytherin']:
#         #     raise ValueError('No such House')
      
#         self.name=name
#         self.house=house
        
#     def __str__(self): #__str__ is pythons inbuilt
#         return f"{self.name} from {self.house}"

    
# def main():
#     student=get_student()
#     print(student)
   
# def get_student():
 
#     name=input('Name:')
#     house=input('house:')

#     return Student(name,house)


# if __name__=='__main__':
#     main()

class Student:
    def __init__(self,name,house):
        
        self.name=name
        self.house=house
        
    def __str__(self): #__str__ is pythons inbuilt
        return f"{self.name} from {self.house}"

    @property
    def house(self): #getter
        return self._house
    @house.setter
    def house(self,house): #setter 
        if house not in ['ravenclaw','gryffindor','hufflepuff','slytherin']:
                    raise ValueError('No such House')
        self._house= house

    @property
    def name(self): #getter
                return self._name
    @name.setter
    def name(self,name): #setter 
            if not name :
                raise ValueError('missing name')
            self._name= name
    #getter used to set instruction when someone gets value eg printing
    #setter used to set instructions or rules when someone changes value or sets value

def main():
    student=get_student()
    #student.house="kuch bhi" #error because of this as changing value
    print(student)
   
def get_student():
 
    name=input('Name:')
    house=input('house:')

    return Student(name,house)


if __name__=='__main__':
    main()
    
    