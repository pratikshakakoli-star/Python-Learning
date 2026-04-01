# class Student:  #1st char of classname must be capital
#     roll_num=101
#     num1=50
#     num2=100   #data member

#     def add(self):     #member function
#         print(self.num1+self.num2)
#         self.name=input("Enter name: ") #name is your new type of variable
#         print(self.name)
# obj=Student()#obj creation outside a class
# obj.add()#calling function
# print(obj.roll_num)#accessing the data member of class by using obj

# class NewClass:
#     def __init__(self):
#         print("constructor always execute 1st")
#     def show(self):
#         print("Welcome to class level progmming")
# obj=NewClass()
# print(obj)
# obj.show()
# obj1=NewClass()            


# class HOD:
#     def __init__(self):#default construction
#         self.name='pra'#2bytes
#         self.age=20 #3bytes
#         self.empid=101  #1bytes

#     def info(self):
#         print("My name is:",self.name)
#         print("My age is :",self.age)
#         print("My empid is: ",self.empid)    
# obj=HOD()
# obj.info()        


#parameterised constructor 
# class HOD:
#     def __init__(self,name,age,rollno):
#         self.age= age
#         self.rollno= rollno
#         self.name=name
#     def show(self):
#          print("My name is:",self.name)
#          print("My age is :",self.age)
#          print("My empid is: ",self.rollno)   
# obj=HOD('ar',45,110)
# obj.show()         


#instance variable
# class New:
#     def __init__(self):
#         self.a=10
# obj1=New()    
# obj2=New()    
# obj3=New()        
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# obj1.a=20
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)


#static variable
# class New:
#     a=10
#     def __init__(self):
#         self.name="pra"  #instance variable

# obj1=New()
# obj2=New()
# obj3=New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# New.a=50
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

#instance method
# class Student:
#     def __init__(self,name,rollno,mob):
#         self.name=name
#         self.rollno=rollno
#         self.mob=mob
#     def display(self):
#         print(self.name," ",self.rollno," ",self.mob) 
# stud=Student("pra",1001,1234567899)
# stud.display()

#static method
class Student:
    @staticmethod  
    def get_personal_detail(fname,lname):
        print("your personal detail=",fname,lname)

    @staticmethod
    def contact_detail(mno,rollno):
        print("your contact detail=",mno,rollno) 

Student.get_personal_detail("pra","j")
Student.contact_detail(1234567890,101)           
    