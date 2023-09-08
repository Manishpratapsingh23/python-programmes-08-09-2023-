#finding a number in fiboniacci series
n=int(input("enter number: "))
a=0
b=1
s=0
count=0
while n>s:
    s=a+b
    a=b
    b=s
    if s==n:
        count+=1
        break
if count==1:
    print("found")
else:
    print("not found")


#outputs:

#enter number: 13
#found

#enter number: 1000000000
#not found

