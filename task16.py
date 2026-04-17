data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

# 1. str larni ajrating
# 2. har bir str ni upper case qiling
mapped_data = map(str.upper, filter(lambda item: type(item) == str, data))

print(list(mapped_data))
