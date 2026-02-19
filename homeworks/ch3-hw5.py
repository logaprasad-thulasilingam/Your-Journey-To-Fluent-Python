city1 = input("Enter first city name:")
city2 = input("Enter second city name:")
city3 = input("Enter third city name:")

if (len(city1) > len(city2) and len(city1)>len(city3)):
    print (city1)
elif (len(city2)>len(city1) and len(city2)>len(city3)):
    print(city2)
elif (len(city3)>len(city1) and len(city3)>len(city2)):
    print(city3)