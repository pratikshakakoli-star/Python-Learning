# i=1 #i=1
# while i<=5:
#     print(i)
#     i=i+1

#WAP to print the sum of the natural no from 1-10 using while loop 
# i=1
# sum=0
# while i<=10:
#     sum=sum+i
#     i=i+1
# print("sum:",sum)    

#WAP to print the count of even and odd from 1 to 10 using while loop
# even=0
# odd=0
# i=1
# while i<=10:
#     if i%2==0:
#        even=even+1
#     else:
#         odd=odd+1
#     i=i+1    
# print("even",even) 
# print("odd",odd)          

# n= [1,2,4,5]
# n.reverse()
# print(n)
# n=[1,2,4,5]
# for i in n:

#     print(i)
#zip()--> it is used to keep multiple range functions
# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i," ",j)

#WAP using while loop 5*4*3*2*1=120

# i=1
# S=0
# n=int(input("Enter the no"))
# while i<=n:
#     S=n*(n-1)
# i=i+1
# print("fact:",S)

# WAP to find the fibonacci no:
# i=0
# n=int(input())
# while i<=n:




# username=" "
# passw=0
# while username!="admin" or passw!=12345:
#     username=input("Enter the username:")
#     passw=int(input("Enter the password:"))

# for i in range (1,4):
#     for j in range(1,4):
#         print(i,end=" ")
#     print()    


# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end=" ")
#     print()

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(i,end=" ")
#     print()    


n=int(input())
for i in range(1,n+1):
    for j in range(1,1+i):
        print(chr(64+i),end=" ")
    print()    