item = input("What item would you like to buy today?: ")
price = float(input("What is the price of that item?:"))
quantity = int(input("How much would you like to buy?:"))
subtotal = price*quantity
total = subtotal*7.25
total = int(total)
print(f"You have bought {quantity} {item}")
print(f"Subtotal: {subtotal}")
print(f"Total: {total}.00")