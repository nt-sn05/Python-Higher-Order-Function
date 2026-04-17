prices = ["$120", "$340", "$50", "$90"]


result = []
for price in prices:
    new_price = float(price[1:])
    result.append(new_price)

result = map(lambda price: float(price[1:]), prices)

print(list(result))


# descending -> kamayish
# ascending -> o'sish
