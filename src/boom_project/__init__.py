from fractions import Fraction

y2= int(input("Enter one of your Y corrdinates\n"))
y1= int(input("Enter your other Y corrdinates\n"))
print (y2-y1)
if (y2-y1) ==0:
    print("Your slope is 0 bud you have a horizontal line")
x2= int(input("Enter one of your x corrdinates\n"))
x1= int(input("Enter your ofther x corrdinates\n"))
print (x2-x1)  
if (x2-x1) ==0:
    print("Your slope is undefined bud you have a vertical line") 
z1= (y2-y1)
z2= (x2-x1)
if z2 == 0:
    print("Your slope is undefined")
else:
    print("Your slope is " + str(Fraction(z1, z2)))