a=int(input("enter first side: "))
b=int(input("enter second side: "))
c=int(input("enter third side: "))
x=0
if b>c:
    x=c
    c=b
    b=x
if a>b:
    x=a
    a=b
    b=x
if b>c:
    x=c
    c=b
    b=x
if a+b>c:
    if a==b or b==c or c==a:
        print("isosceles")
    elif a*a + b*b ==c*c:
        print ("right angled")
    elif a!=b or b!=c or c!=a:
        print("scalane")
else:
    print("not a triangle")

    

