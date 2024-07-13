# Paycheck Values
pay_rate = int(input())
hours_worked = int(input())

# Calculator for weekly pay
if hours_worked <= 40:
    pay_check = (pay_rate * hours_worked)
else:
    over_time = hours_worked - 40
    pay_check = (pay_rate * 40) + (over_time * 30)
print(str("Employee's weekly paycheck is ${paycheck}.").format(paycheck=pay_check))
