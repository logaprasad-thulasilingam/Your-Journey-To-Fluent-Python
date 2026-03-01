def sum_digit(num):
    result = 0
    for i in num:
        if i.isdigit():
            result += int(i)
    return result

num = input("enter a number:")
print(sum_digit(num))