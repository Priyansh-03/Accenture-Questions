import math

x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))
x2=int(input("Enter x2: "))
y2=int(input("Enter y2: "))

distance=math.sqrt((x1-x2)**2+(y2-y1)**2)
print("Distance between two points is: ",int(distance))
