days = int(input('How many days?'))
kms = float(input('How many Kilometers? '))
vday = days*60
vkm = kms*0.15
result = vday+vkm
print('+'*50)
print(' You have spent {} day(s), it costs ${:.2f} per day'
      '\n And {}km, it costs ${} per Km.'
      '\n The total you should pay is ${:.2f}'.format(days, vday, kms, vkm, result))
print('+'*50)
