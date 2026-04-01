#WAP to accept days and check the working day or weekend\
# days=input("Enter the day")
# if days == "saturday" or days=="SUNDAY" or days=='SATURDAY' or days=='sunday':
#     print("weekend")
# else:
#     print("Working day")

#strip: to remove spaces both sides
#lstrip: to remove spaces at right hand side
#rstrip:to remove the space at left side

pr=input("Enter your programming name:")
p_name=pr.strip()
if p_name=='Python'or 'python' or 'PYTHON':
    print(p_name)
elif p_name=='Java'or 'java'or 'JAVA':
    print(p_name) 
elif p_name=="CPP"or "cpp"or 'Cpp':
    print(p_name)
else:
    print("Wrong programming name")             