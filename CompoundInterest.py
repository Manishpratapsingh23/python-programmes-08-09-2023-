#COMPOUND INTEREST
p=float(input("enter principal amt: "))
r=float(input("enter rate: "))
t=int(input("enter time: "))
x=p
while t!=0:
    ci=p*(1 + r/100)
    p=p+ci
    t=t-1
print("Compoud Interest is ",ci)
print("Total Amount is ",x+ci)



#output:
#enter principal amt: 2500
#enter rate: 10
#enter time: 2
#Compoud Interest is  5775.000000000001
#Total Amount is  8275.0
