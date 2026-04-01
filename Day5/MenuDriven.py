#WAP to menu driven program using arithmetic operation
import sys# this is used to make exit 
def addition():
    print("FOR ADDITION")
    a=int(input("Enter the Value of a:"))
    b=int(input("Enter the Value of b:"))
    print("Addition=",a+b)
def substraction():
    a=int(input("Enter the Value of a:"))
    b=int(input("Enter the Value of b:"))
    print("Substraction=",a-b)
def multiplication():  
    a=int(input("Enter the Value of a:"))
    b=int(input("Enter the Value of b:"))
    print("Multiplication=",a*b)  
def division():
    a=int(input("Enter the Value of a:"))
    b=int(input("Enter the Value of b:"))
    try:    
        print("Division=",a/b) 
    except:
        print("can't devide by zero")       
while True:
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        addition()#calling function
    elif choice==2:
        substraction()
    elif choice==3:
        multiplication()
    elif choice==4:
        division()
    elif choice==5:
        sys.exit()


