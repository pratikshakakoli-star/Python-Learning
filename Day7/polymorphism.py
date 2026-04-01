# class Principal:
#     def role(self):
#         print("I am managing the all activities of collage")
# class Dean:
#     def role(self):
#         print("I am decision taking person")
# class Hod:
#     def role(self):
#         print("I have responsibility of teacher and students")
# class Faculty:
#     def role(self):
#         print("I have to complete syllabus successfully")

# def fuc(obj):
#     obj.role()
# campus=[Principal(),Dean(),Hod(),Faculty()] 
# for obj in campus:
#     fuc(obj)           

#overloading concept
# class Arithmetic:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# obj=Arithmetic()
# obj.add(10,20,30)
# # obj.add(10,20)
# # obj.add(1,2,3)

#cunstructor overloading
#constructor over is not possible in python 
#if we define multiple constructors then the last constructor will be considered 

#class Arithmatic:
#     def __init__(self):
#         print("There is no argument")
#     def __init__(self,a):
#         print("paassing 1 argument")
#     def __init__(self,a,b ):
#         print("passing 2 parameters")
# obj = Arithmatic(10,20)
# obj=Arithmatic(10)
# obj=Arithmatic(2)            

#method overriding
# class RBI:
#     def homeloan_ROI(self):
#         print("Hoe loan interest = 7.5%")
#     def carloan_ROI(self):
#         print("Car loan interest is = 8%")
# class Sbi(RBI):
#     def homeloan_ROI(self):
#         print("Home loan interest of child is = 6.5%")

# obj=Sbi()
# obj.homeloan_ROI()
# obj.carloan_ROI()

# class RBI:
#     def homeloan_ROI(self):
#         print("Hoe loan interest = 7.5%")
#     def carloan_ROI(self):
#         print("Car loan interest is = 8%")
# class Sbi(RBI):
#     def homeloan_ROI(self):
#         print("Home loan interest of child is = 6.5%")
# #to access the parent class method use SUPER()
#         super().homeloan_ROI()
# obj=Sbi()
# obj.homeloan_ROI()
# obj.carloan_ROI()

#constructor overriding

# class Father:
#     def __init__(self):
#         print("I am already at breakfast")
# class child(Father):
#     def __init__(self):
#         print("I will be late for the breakfast")
# obj=child()

#accessing parent class in child using super() in consrtucter overriding 
# class Father:
#     def __init__(self):
#         print("I am already at breakfast")
# class child(Father):
#     def __init__(self):
#         print("I will be late for the breakfast")
#         super().__init__()
# obj=child()


from abc import ABC, abstractmethod

class Help4Code(ABC):
    @abstractmethod
    def training(self):
        pass
    @abstractmethod
    def placement(self):
        pass
class Ashish(Help4Code):
    def training(self):
        print('C,C++,Java')
    def placement(self):
        print('Java Placement')

class Ankush(Help4Code):
    def training(self):
        print('Python')
    def placement(self):
        print('Python Placement')

class Prashant(Help4Code):
    def training(self):
        print('ML')
    def placement(self):
        print('ML Placement')
obj1=Ashish()
obj1.training()
obj1.placement()

obj2=Ankush()
obj2.training()
obj2.placement()

obj3=Prashant()
obj3.training()
obj3.placement()