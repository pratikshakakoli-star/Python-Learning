#WAP to accept three paper marks and calculate total,percentage and if percentage is greater rhen equal to 60 he/she is eligible for placement else not
math=60
chem=70
phy=60
total=math+chem+phy
percentage=total/3.0
print("Total=",total)
print("percentage=",percentage)
if percentage>=60:
    print("You r eligible for placement")
else:
    print("not eligible")    