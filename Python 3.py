snack_name  = "Chips"
price = 1.50
quantity  = 10
is_available = True

print("Snack:", snack_name)
print("Price:$", price)
print("In Stock:", quantity)
print("Availabe?", is_available)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_available))



total = price * quantity
print("Total value:$", total - 0.25)
print("Sale price:", quantity * 2)


print("Is price under $2", price < 2)
print("Letters in snack name:",len(snack_name))
print("First letter:",snack_name[0])


price_a = 1.50
price_b = 3.00
print("Before:", price_a, "and", price_b)

shop_name = "Quick" + " " +  "Bites"
print("Shpo name:", shop_name)
print("Letters in snack name:", len(snack_name))
print("First letter", snack_name[0])


price_a = 1.50
price_b = 3.00
print("Before:", price_a, "and", price_b)

temp = price_a
price_a = price_b
price_b = temp

print("After:", price_a, "and", price_b)
