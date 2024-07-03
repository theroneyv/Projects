import random

options = ['rock','paper','scissors']

def main():
    computer = random.choice(options)
    while True:
        user = input('Your option: ')
        if user not in options:
	        print('Invalid option!')
        else:
            if user == 'rock ' and computer == 'paper'or\
                 user == 'paper' and computer == 'scissors' or\
                 user == 'scissors' and computer == 'rock':
        	    print('You lose!')
            elif user == computer:
	            print('Tie!')
            else:
	            print('You win!')
            break

main()
