# Programmer: Christine Doan
# Prompt: Ask price of product and quantity ordered
# Calculate price before subtotals, money saved, and total amount of purchase after subtotals

# variables
price = float(input("What is the price of each item? "))
items = int(input("How many are you ordering? "))

# defining
def subtotals (p, i):
    if items >= 10 and items <= 19:
        t = (p * i) * 0.10
    elif items >= 20 and items <= 49:
        t = (p * i) * 0.20
    elif items >= 50 and items <= 99:
        t = (p * i) * 0.25
    elif items >= 100:
        t = (p * i) * 0.30
    else:
        t = (p * i) * 0
    return t

# calculations
sub = (price * items)
dis = subtotals (price, items)
total = (sub - dis)

# output
print("Subtotal: $", (format(sub, '.2f')))
print("Discount: $", (format(dis, '.2f')))
print("Total: $", (format(total, '.2f')))
