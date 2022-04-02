# THE PROGRAM HAVE TO READ A NUMBER (0 - 9999) AND SHOWS EACH NUMBER SEPARATELY
num = int(input('Enter a number between 0 - 9999 : '))
u = num // 1 % 10
t = num // 10 % 10
h = num // 100 % 10
th = num // 1000 % 10
print('Analyzing the number " {} "...'.format(num))
print('Unit: {}'.format(u))
print('Ten: {}'.format(t))
print('Hundred: {}'.format(h))
print('Thousand: {}'.format(th))
