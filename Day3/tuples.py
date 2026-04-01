# mytuple=("pra","Ash","Ra","sa","ko","an","ra",23,3.15,77,"sa")
# print(mytuple)
# print(type(mytuple))
# print(mytuple[0])
# #mytuple[0]='a'  tuple is immutable 
# print(mytuple)


#set data type

# muset={1,2,"san",5.66,"ra","au",'r'}
# print(muset)
# print(type(muset))
# # muset.add(60)
# # print(muset)
# #muset.discard(3)
# muset.remove("san")
# print(muset)

# myset={100,20,30,40}
# urset={"pra","jha",100}
# list={100}
# # newset=myset.union(urset,list)
# # print(newset)

# newset=myset.intersection(urset,list)
# print(newset)
#difference() method will returns the element present inthe first set but not in the second set.

# m={1,2,3,4}                                           
# n={1,6,5,3}
# print(m)
# print(m.difference(n)) #{2,4}
# print(n.difference(m))
# print(m.pop())
# print(n.pop())
# print(m.clear())  

#output:
# {1, 2, 3, 4}
# {2, 4}
# {5, 6}
# 1
# 1
# None

mydict={
    "name":"pra",
    "usn":  "2hn23",
    "branch":"Cse"
}
print(mydict)
# print(type(mydict))
# mydict.pop("name")
# print(mydict)
n=mydict.copy()
print(n) 

# m={
#     1:"p",
#     2:"a",
#     "3":"m",#"3"=string data
#     4:"t",
#     1:"a",
#     4:"a"   #the value is updated via value through key
# }
# print(m)

# #with the help of key we have to print values
# print(m[1])
# m[1]="pe"
# print(m)
# for x in m:   #prints only keys
#     print(x)
# for x in m.values():
#     print(x)

# for x,y in m.items():#to display both value
#     print(x,y)
# m['m.no']=1234566
# print(m)