real = float(input('How much do you have in your pocket? R$'))
dollar = real / 4.90
euro = real / 5.20
print('With R${} you can exchange US$ {:.2f}'.format(real, dollar))
print('With R${} you can exchange E$ {:.2f}'.format(real, euro))

# ".2f" it defines how many decimals after the poit could be shown
