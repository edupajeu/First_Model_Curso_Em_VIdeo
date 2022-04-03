# ANALYSING A STRING
p = str(input('Enter a phrase: ')).upper().strip()
print('The letter "A" shows up {} times'.format(p.count('A')))
print('First time shows up: {} position'.format(p.find('A')+1))
# + 1 add to show a right numerical position
print('Last time shows up: {} position'.format(p.rfind('A')+1))
