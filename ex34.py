# THE PROGRAM CALCULATE A PROMOTION FOR A NEW SALARY IN TWO DIFFERENT CASES
wage = float(input('Inform your current wage: '))
if wage <= 1250:
    new = wage + (wage * 15 / 100)
else:
    new = wage + (wage * 10 / 100)
print('Your last wage was ${:.2f} and now is ${:.2f}'.format(wage, new))
