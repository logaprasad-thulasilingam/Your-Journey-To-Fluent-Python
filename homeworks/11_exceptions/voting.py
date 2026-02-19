def check_voter_age(age):
    if age < 18:
        raise ValueError("Not eligible to vote")
    print("Eligible to vote")
try:
    age = int(input("Enter the age:"))
    check_voter_age(age)
except ValueError as e:
    print ("Error:", e)