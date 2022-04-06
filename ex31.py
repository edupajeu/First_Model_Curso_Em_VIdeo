# TRIP CALCULATER: INFORMS US HOW MUCH IS A TRIP
print('='*80)
print('You going to pay $0,50 for first 200Km, after that you must pay $0,45')
print('='*80)
dist = float(input('Enter the trip distance: '))
if dist <= 200:
    price = dist*0.5
    print('You must pay ${:.2f} for the trip'.format(price))
else:
    price = dist*0.45
    print('You exceeded the first 200km, you must pay ${:.2f} for the trip'.format(price))
