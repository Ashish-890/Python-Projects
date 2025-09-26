
print("Welcome to computer quiz game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    # != means not equal to
    # here playing!="yes" is the condition
    quit()

print("Okay! Let's play :) ")
score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    #.lower() method converts the string to lowercase  
    # here if statement checks if the answer is correct
    # here == means equal to 
    print("Correct!")
    score += 1
    # here score is an integer variable
    # += operator adds the value in score variable by 1
else:
    # else statement executes if the if condition is false
    # that means the condition {answer.lower() == "central processing unit" is false} is not true
    print("Incorrect!")

answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does NBA stand for ")
if answer.lower() == "national basketball association":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does UFC stand for? ")
if answer.lower() == "ultimate fighting championship":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what is the date of uri attack? ")
if answer.lower() == "18 september 2016":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
# here str() function converts the integer variable score to string
print("You got " + str((score / 5) * 100) + "%.")
# here (score/5)*100 calculates the percentage of correct answers