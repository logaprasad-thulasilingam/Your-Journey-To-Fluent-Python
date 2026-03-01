def factors(num):
    result = []
    if num < 1:
        return result
    else:
        for i in range(1, num+1):
            # print (i)
            # print(num%i)
            if (num%i == 0):
                # print(num/i)
                result.append(i)
    return result

num = int(input("enter the num:"))
print (factors(num))