wage = float(input('Enter your current wage: $'))
perc = float(input('Enter the percent of promotion: '))
prom = wage*perc/100
result = wage+prom
print('+'*50)
print(' Your wage ${} have increased in {}%\n Your new wage is ${}\n '
      'Congratulation for your promotion'.format(wage, perc, result))
print('+'*50)

