import random
students = ('Zé', 'Clara', 'Lara', 'Pedro')
st = random.choice(students)
nd = random.choice(students)
rd = random.choice(students)
lst = random.choice(students)
print(' The first student to presents is: {}\n The second is: {}\n'
      ' The third is: {}\n The last is: {}'.format(st, nd, rd, lst))
