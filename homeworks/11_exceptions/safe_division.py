def safe_divide(num, den):
    try:
        print(f"The result is {num / den}")

    except ZeroDivisionError:
        print("ERROR: Cannot be divided by zero")
    finally:
        print("Division is done")


num = int(input("Enter the numerator:"))
den = int(input("Enter the denominator:"))
safe_divide(num, den)
