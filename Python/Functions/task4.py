''' Applies a 10% discount to each product 
    and returns products
    with discounted price greater than 500.
'''
#data
products = [
{"name": "Laptop", "price": 1200},
{"name": "Phone", "price": 800},
{"name": "Tablet", "price": 600},
{"name": "Monitor", "price": 300}
]

#functions
discounted_prices = list(map(lambda p: p["price"] * 0.9, products))
filtered_products = list(filter(lambda p: p["price"] * 0.9 > 500, products))

#print
print(filtered_products)