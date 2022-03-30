prod = float(input('Enter the price of the product: US$'))
disc = prod*5/100
result = prod - disc
# In that case you multiple the price between 5% (percent) and divides by 100
# Formula: x*z/y
print('The new price with discount is: US${:.2f}'.format(result))
