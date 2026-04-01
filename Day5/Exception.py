# def division():
#     try:

#         a=int(input("Enter the Value of a:"))
#         b=int(input("Enter the Value of b:"))    
#         print("Division=",a/b) 
#     except ZeroDivisionError:
#         print("can't devide by zero")       
#     except ValueError:
#         print("Enter only integer value")
# division()        


#handling type Error
# try:
#     num="hello"+5
# except:
#     print("can't add string and number together")


#Handling multiple different kinds of exception with singke except block
# def division():
#     try:
#         a=int(input("Enter the Value of a:"))
#         b=int(input("Enter the Value of b:"))    
#         print("Division=",a/b) 

#     except (ValueError,ZeroDivisionError)as msg:
#         print(msg)

# division()         


#The concept of default ecxept block generally we used for writing normal msg or showing normal error


# def division():
#     try:
#         a=int(input("Enter the Value of a:"))
#         b=int(input("Enter the Value of b:"))    
#         print("Division=",a/b) 

#     except (ValueError,ZeroDivisionError)as msg:
#         print("Enter correct no:",msg)
#     except:
#         print("This is default part of except block")
# division()          
#default except part should be last in case of multiple exception except part


#
# def division():
#     try:
#        a=int(input("Enter the Value of a:"))
#        b=int(input("Enter the Value of b:"))            
#        print("Division=",a/b) 

#     except (ValueError,ZeroDivisionError)as msg:
#         print("Enter correct no:",msg)
#     else:
#        print("This is ok")
# division()          


#Finally block will always execute whether try block generate error or not
# def division():
#     try:
#        a=int(input("Enter the Value of a:"))
#        b=int(input("Enter the Value of b:"))            
#        print("Division=",a/b) 

#     except (ValueError,ZeroDivisionError)as msg:
#         print("Enter correct no:",msg)
#     finally:
#        print("i will always executed")
# division()          

#nested try except block
# def division():
#     try:
#        a=int(input("Enter the Value of a:"))
#        b=int(input("Enter the Value of b:")) 
#        try:           
#             print("Division=",a/b) 

#        except ZeroDivisionError as msg:
#         print(msg)
#     except ValueError as msg:
#        print(msg)
# division()          


#raise = user defined exception by raise keyword
# bank_bal=500
# if bank_bal<2000:
#     raise Exception("your account balance is below a accessing limit")
# else:
#     print("Your account has withdrawal")