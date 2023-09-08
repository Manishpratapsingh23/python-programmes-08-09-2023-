#goat and chicken problem
h=int(input("enter number of heads: "))
l=int(input("enter number of legs: "))
for i in range(1 , h+1):
    if i*4 + (h-i)*2 == l:
        print("number of chickens: ", h-i)
        print("number of goats: ", i)
        break



#output:
#enter number of heads: 340
#enter number of legs: 1060
#number of chickens:  150
#number of goats:  190
