"""
    Applies a discount function to a given price.

    Parameters:
    - price: original price
    - discount_function: a function that takes price and returns discounted price

    Returns:
    - discounted price
    """

#function
def apply_discount (price,discount_function):
    return discount_function(price)


flat_discount= lambda price: price-50
percent_discount = lambda price : price - ((price *20)/100)


#inputs and print
price = 200
print("Flat Discount:", apply_discount(price, flat_discount))  

print("20% Discount:", apply_discount(price, percent_discount))  

print("Flat Discount:", apply_discount(40, flat_discount))  
