import math
co = float(input('Enter the opposite cathetus: '))
ca = float(input('Enter the adjacent cathetus: '))
hypot = math.hypot(ca, co)
print('The sum between the cathetus is equal the length of the hypotenuse {:.2f}'.format(hypot))

