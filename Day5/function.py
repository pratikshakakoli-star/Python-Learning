# def msg():#called function
#     print("Hello World!")

# msg()#calling function
# msg()

# def login():
#     user=input("Enter the user name:")
#     passw=input("Enter the password")
#     if user == passw:
#         print("Login succeessfull")
#     else:
#         print("Invalid credential")
# login()    

# def add():
#    return 2+3

# # print(add())

# res=add()
# print("result:",res)

#can a function return multiple value in python
# def add():
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b:"))
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return add,sub,mul,div  
# result=add()
# print("result:",result)


#how many types of arguments we can pass in the function
#1 positional argument
#2 keyword argument
#3 default argument
#4 variable number of argument/variable length of argument
#1
# def name(a,b):
#     print(a+b)

# name(2,3)    


# def personalInfo(fname,lname):
#     print("FirstName:",fname)
#     print("Lastname:",lname)
# personalInfo("pratiksha","Kakoli")
# def name(a,b):
#    n=a+b
#    return n

# add=name(2,3)
# print(add)

#2

# def profile(fname,lname):
#     print("first name:",fname)
#     print("lastname:",lname)
# profile(fname="p",lname="k")    

#3
# def cityName(city="Banglore"):
#     print("City Name:",city)
# cityName("Nagpur")
# cityName("Delhi") 
# cityName()   


#4
# def city(*name):
#     print(name)

# city("mumbai","pune","banglore","hydrabad","delhi")

#WAP to menu driven program using arithmetic operation


# def fact(n):
#     result=1
#     for i in range(1,n+1):
#         result*=i
#     return result
# num=int(input("Enter the no:"))
# print("Factorial:",fact(num))    

def prime(n):
    if n<=1:
        return  False
    for i in range(2, int(n**0.5)):
        if n%i==0:
            return False
    return True    
num=int(input("Ente the no:"))
if prime(num):
    print(num,"is prime")
else:
    print(num,"is not prime")    