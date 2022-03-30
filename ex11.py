l = float(input('Length of the wall: '))
h = float(input('High of the wall: '))
area = l * h
ink = area/2
print('Your wall`s dimension is: {} x {} \nThe wall`s area is: {}m2\n'. format(l, h, area))
print('To paint this wall, you`ll need {}l of ink'.format(ink))
