#single ineritence
# class Collage:#parent
#     def collage_name(self):
#         print("Modern clg")
# class Student(Collage):#child
#     def student_info(self): #member function
#         print("Name: prashant j")
#         print("Branch: cse")  
# obj=Student()#obj create child class
# obj.collage_name()
# obj.student_info()

#multi level inheritence
# class Collage:#parent
#     def collage_name(self):
#         print("Modern clg")
# class Student(Collage):#child
#     def student_info(self): #member function
#         print("Name: prashant j")
#         print("Branch: cse") 
# class Exam(Student):
#     def Subject(self):
#         print("Sub1= maths")
#         print("Sub2: AI")
#         print("Sub3-> cc")         
# obj=Exam()#obj create child class
# obj.collage_name()
# obj.student_info()
# obj.Subject()


#multiple inheritence
class SubMarks:
    m=int(input("Enter the marks:"))
    n=int(input("Enter the marks:"))
    o=int(input("Enter the marks:"))
class PractMarks:
    pm=int(input("Enter the marks:"))
class Result(SubMarks,PractMarks):
    def total(self):
        if self.m>=40 and  self.n>=40 and self.o>=40 and self.pm>=20 :
            print("pass")
        else:
            print("fail")
abc=Result()
abc.total()