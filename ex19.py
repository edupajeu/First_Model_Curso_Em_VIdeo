#import random TO USE THE WHOLE MODEL
from random import choice
n1 = str(input('First student: '))
n2 = str(input('Second student: '))
n3 = str(input('Third student: '))
n4 = str(input('Last student: '))
list = [n1, n2, n3, n4]
# We are using [] because we are dealing with a list
x = choice(list)
print('The student will erase the blackboard is: ', x)
