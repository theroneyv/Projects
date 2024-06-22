import random

options = ['rock','paper','scissors']

user = input('Your option: ')
computer = random.choice(options)

if user not in options:
	print('Invalid option!') 
else:
	print('Computer option:', computer)


if user == 'rock ' and computer == 'paper' or user == 'paper' and computer == 'scissors' or user == 'scissors' and computer == 'rock':
	print('You lose!')
elif user == computer:
	print('Tie!')
else:
	print('You win!')
