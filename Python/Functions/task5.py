'''
Sorts a list of product dictionaries by their 'price' field.

Parameters:
- products: list of dictionaries, each containing 'name' and 'price'

Returns:
- ascend: list of products sorted by price in ascending order
- descend: list of products sorted by price in descending order
'''

#import
from task4 import products

#functions
ascend= sorted(products,key=lambda x: x["price"])
descend= sorted(products,key=lambda x: x["price"],reverse=True)

#print
print("Ascending order is\n",ascend)
print("Descending order is\n",descend)