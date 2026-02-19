a = int(input("Enter first value for triangle:"))
b = int(input("Enter second value for triangle:"))
c = int(input("Enter third value for triangle:"))
if ((a+b)<c or (a+c)<b or (b+c)<a):
    print("NO")
else:
    print ("YES")