# ANALYSING A NAME
name = str(input('Enter your full name: ')).strip()
sep = name.split()
print('The name analysed was: {}'.format(name))
print('The first name is: {}'.format(sep[0]))
# TO CATH THE LAST ITEM OF THE LIST WE USED THE METHOD LEN
print('The last name is: {}'.format(sep[len(sep)-1]))
