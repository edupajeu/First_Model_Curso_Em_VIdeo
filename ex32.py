# PROGRAM TO LOOK OUT IF THE YEAR INFORMED IS A LEAP YEAR.
from datetime import date
y = int(input('Which year do you want to analyze? Or put 0 to analyze the current year: '))
# leap = year % 4 != 0 and year % 100 == 0 or year % 400
#print(leap)
if y == 0:
    y = date.today().year  # USED TO GET THE CURRENT YEAR
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print('This year ({}) is a LEAP Year!'.format(y))
else:
    print('This year ({}) is a REGULAR year!'.format(y))

