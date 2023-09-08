#counting number of currency notes of 2000,500 and 100
s=int(input("enter total currency: "))
t1,t2,t3=0,0,0
while s>100:
 if s>=2000:   
   t1=s//2000
   s=s%2000
 elif s>500: 
  t2=s//500
  s=s%500
 elif s<=500: 
  t3=s//100
  s=s%100
print("currency of 2000 notes: ",t1)
print("currency of 500 notes: ",t2)
print("currency of 100 notes: ",t3)


#outputs:
'''
enter total currency: 4500
currency of 2000 notes:  2
currency of 500 notes:  0
currency of 100 notes:  5


enter total currency: 2800
currency of 2000 notes:  1
currency of 500 notes:  1
currency of 100 notes:  3
'''
