# THE PROGRAM HAS TO GIVE A FINE WHO EXCEEDS THE SPEED LIMIT
sp = float(input('What is the current car velocity? '))
if sp > 80:
    fine = (sp-80)*7
    print('You exceeded the speed limit "{}Km/h"! You got a fine!'.format(sp))
    print('You have to pay a fine that cost ${:.2f}'.format(fine))
else:
    print('Your speed does not exceed the speed limit "{}Km/h". Good job!'.format(sp))
    