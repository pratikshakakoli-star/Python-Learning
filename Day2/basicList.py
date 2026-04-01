#mylist=["prashant","b","k","an","ashish",77,"san",60.52,"prashant"]

#print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])

# mylist[2]="AK"  #to change the index value
# print(mylist)

# mylist.append("Pratiksha")
# print(mylist)

# if "AK" in mylist:
#     print("yes")
# else:
#     print("no")    #no

#append
# mylist.append("h") 
# mylist.append('L')
# print(mylist)


#if we want to add the value at specified index

# mylist.insert(1,"san")
# print(mylist)

# mylist.remove("san")
# print(mylist)

# newlist=mylist.copy()
# print(newlist)
# print(mylist)

# mylist=[["pra",'jha'],['85.56'],[442200,"yyy"]]

# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])
# print(mylist[1][1])

# mylist=["A","B"]
# # print(mylist*2)

# list2 =[50,25.50]    
# print(list2+mylist)   
# list1=[50, 25.5, 'A', 'B']
# # del list1
# # print(list1)
# list1.clear()
# print(list1)

# n="pra"
# print(n)
# m=list(n)
# print(m)

# mylist=[10,20,30,40]
# mylist.reverse()
# print(mylist)

# mylist = [44, 22, 77, 0, 9, 88]  
# list=['b','c','a']
# list.sort()
# print(list)
# mylist.sort()  
# print(mylist)
# mylist.sort(reverse=True)
# # print(mylist)

# mylist=[44,22,7,0,9,8]
# newlis=mylist
# print(id(mylist))
# print(id(newlis))

# for i in range(1,11):
#     print(i*2," ",i*3," ",i*4," ",i*5," ",i*6," ", i*7," ",i*8," ",i*9," " ,i*10)

#WAP to print even or odd no:
# odd=0
# even=0
# for i in range(1,11):
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1    
# print("Even: ",even)
# print("odd: ",odd)
                    
# user=input("Enter user name: ")
# passo=input("Enter the password: ")
# if user==passo:
#     print("login successful")
# else:
#     print("Invalid login")    

# brand=input("Enter the cool drink name either in upper case in lowercase but not combine")
# if brand=="pepsi" or brand=="PEPSI" :
#     print("swag")
# elif brand=="dew" or brand=="DEW" :
#     print("dar ke age jeet hai")  
# elif brand =="thumsup" or brand=="THUMBSUP":
#     print('taste the thunder')
# else:
#     print("go to ur brand")        


n1=int(input("Enter the 1st no: "))
n2=int(input("Enter the 1st no: "))
n3=int(input("Enter the 1st no: "))

if n1>n2 and n1>n3:
    print("Big:",n1)
elif  n2>n3:
    print("Big:",n2)    
else:
    print("Big:",n3)    