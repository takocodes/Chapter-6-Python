# Programmer: Christine Doan
# Prompt: Input number of hours worked and hourly rate to calculate total wages for the week

# calculations
hours = int(input("Insert the number of hours worked: "))
rate = float(input("Insert the hourly rate: "))

# defining function
def wages (h, r):
    t = h * r
    return t

# calculation and output
total = wages (hours, rate)

print("Your total wage is $", (format(total, '.2f')))
