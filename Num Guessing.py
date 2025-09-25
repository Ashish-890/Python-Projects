#generate a random number between 1 and 100
#LOOP
#ask user to guess the number
#if not a valid number
#  print invalid input
#if number < guess
#  print too low
#if number > guess
#  print too high
#else
#  print correct

import random
number_to_guess = random.randint(1, 100)
while True:
    try:
        #understood that typing exit() in terminal would exit the python interpreter
        #we should run our code in system terminal

        guess = int(input('Guess a number between 1 and 100: '))
        if guess < number_to_guess:
            print('Too low!')
        elif guess > number_to_guess:
            print('Too high!')
        else:
            print('Correct! You guessed the number.')
            break
    except ValueError:
        print('Invalid input, please enter a number.')


