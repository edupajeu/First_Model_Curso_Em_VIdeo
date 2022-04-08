# THE PROGRAM HAVE TO DECIDE WHICH NUMBER IS THE BIGGEST OR SMALLEST
n1 = float(input('Enter the first number: '))
n2 = float(input('Enter the second number: '))
n3 = float(input('Enter the third number: '))
big = n1  # ANALYZING THE SMALLEST NUMBER
if n2 > n1 and n2 > n3:
    big = n2
if n3 > n1 and n3 > n2:
    big = n3
small = n1  # ANALYZING THE BIGGEST NUMBER
if n2 < n1 and n2 < n3:
    small = n2
if n3 < n1 and n3 < n2:
    small = n3
print('This number "{}" is the biggest number!'.format(big))
print('This number "{}" is the smallest number!'.format(small))
