#Question 3 Task one: Leap year checker

year = 2024
if year%4==0 and (year%100 != 0 or year%400==0):
    print("This is a leap year.")
else:
    print("This is not a leap year.")