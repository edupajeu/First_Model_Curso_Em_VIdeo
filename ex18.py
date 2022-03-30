import math
ang = float(input('Enter the value of angle: '))
rad = math.radians(ang)
cos = math.cos(rad)
sin = math.sin(rad)
tan = math.tan(rad)
print(' The value of cos is {:.2f}\n'
      ' The value of sin is {:.2f}\n '
      ' The value of tan is {:.2f}'.format(cos, sin, tan))
