#loop
#if user enter y 
#  generate two random numbers
#  print the two numbers
#if user enter n
#  print thank you, message
#  exit the loop
#else
#  print invalid input
import random

while True:
 choice = input('Roll the dice? (y/n): ').lower()
 if choice == 'y':
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    print(f'You rolled {num1} and {num2}')
 elif choice == 'n':
    print('Thank you for playing!')
    break
 else:
   print('invalid input')