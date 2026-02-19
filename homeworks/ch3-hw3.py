weight = int(input("Enter the bodyweight:"))
if (weight > 64 and weight <=69):
    print("Middleweight")
elif (weight> 60 and weight <=64):
    print ("First Middleweight")
elif (weight<= 60):
    print ("LightWeight")
else:
    print("Not a valid weight category")