# print(type(50)) its a class all things like str lists dict are class 


# import random
# class hat:
#     def __init__(self):
#         self.house=['ravenclaw','gryffindor','hufflepuff','slytherin']
#     def sort(self,name):
#         print(name, 'is in ',random.choice(self.house))

# hat=hat()
# hat.sort('harry')

# import random
# class hat:

#     house=['ravenclaw','gryffindor','hufflepuff','slytherin'] #stored house globally accessible to every class
#     @classmethod
#     def sort(cls,name):
#         print(name, 'is in ',random.choice(cls.house))

# hat.sort('harry')


# class Student:
#     def __init__(self,name,house):
#         self.name=name
#         self.house=house
        
#     def __str__(self): 
#         return f"{self.name} from {self.house}"

#     @classmethod
#     def get(cls):
#         name=input('Name:')
#         house=input('house:')
#         return cls(name,house)
        

# def main():
#     student=Student.get()
#     print(student)
   
   
# if __name__=='__main__':
#     main()
    
    
# inheritance
# class wizard:
#     def __init__(self,name):
#         if not name:
#             raise ValueError
#         self.name=name

# class stud(wizard):
#     def __init__(self,house,name):
#         self.house=house
#         super().__init__(name)
#     def __str__(self):
#         return f"{self.name},{self.house},is"

# class professor(wizard):
#     def __init__(self,subject,name):
#         self.subject=subject
#         super().__init__(name)

# wiz=wizard('akbus')
# student=stud('griffindor','hairy')
# prof=professor('science','serveus')
# print(student)


# class vault:
#     def __init__(self,rupee,paisa,cent):
#         self.rupee=rupee
#         self.paisa=paisa
#         self.cent=cent
#     def __str__(self):
#         return f"{self.paisa} paisa {self.rupee} rupee {self.cent} cent"

# def main():
#     potter=vault(10,20,30)
#     print(potter)
#     weasley=vault(0,3,5)
#     print(weasley)
#     rs=potter.rupee+weasley.rupee
#     ps=potter.paisa+weasley.paisa
#     ct=potter.cent+weasley.cent
#     total=ct,rs,ps
#     print(total)
# if __name__=='__main__':
#     main()


class vault:
    def __init__(self,rupee,paisa,cent):
        self.rupee=rupee
        self.paisa=paisa
        self.cent=cent
    def __str__(self):
        return f"{self.paisa} paisa {self.rupee} rupee {self.cent} cent"
    def __add__(self, other):
        rs=self.rupee+other.rupee
        ps=self.paisa+other.paisa
        ct=self.cent+other.cent
        return vault(rs,ps,ct)

def main():
    potter=vault(10,20,30)
    print(potter)
    weasley=vault(0,3,5)
    print(weasley)
   
    total=potter+weasley
    print(total)
if __name__=='__main__':
    main()