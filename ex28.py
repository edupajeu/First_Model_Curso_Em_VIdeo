# THE USER HAS TO GUESS WHICH NUMBER THE COMPUTER THOUGHT
from random import randint
from time import sleep
print('+'*80)
print('Thinking a number between 0 -5. Try to guess which number...')
print('+'*80)
print(' ')
num = int(input('Which number I thought: '))
print('Processing...')
sleep(3)  # We use this function to simulate a time processing
n = randint(0, 5)  # Made the computer "THINK"
if num == n:
    print('Congratulation! You got the right number " {} "'.format(num))
else:
    print('Nope! Wrong guess, I thought " {} ", let`s try again...'.format(n))
