# THE PROGRAM CALCULATE IF IS POSSIBLE FORM A TRIANGLE WITH 3 DIFFERENT VALUES
#  from math import sqrt
print('='*50)
print('            Find your triangle!       ')
print('='*50)
a = float(input('First line: '))
b = float(input('Second line: '))
c = float(input('Third line: '))
#  s = (a+b+c) / 2
#  area = sqrt(s*(s-a)*(s-b)*(s-c)) ANOTHER ALTERNATIVE FINDING AREA
if a < b + c and b < a + c and c < a + b:
    print('You can form a triangle!')
else:
    print('You can not form a triangle!')
