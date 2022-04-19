In this project we will know about the programming involed in guessing the numbers .

First we need to consider the range and then include a number .

If the number is considered to be a digit the assign the range with "int" function.

Assuming the number is more or equal to zero then by using "print" give a command of typing a number more than 0 or else print that includes "please type a number next time".
Quit

Now consider , guess 
user_guess = ("make a guess")

now give the same commands to user_guess by including a int and type a number 

if the user_ guess is a random number then the number is right 

elseif the user number > random number , you are above the number 

else if the user_number < random number , you are below the number 

use the same elseif , else statements again 

By using print give the statement " you got the number" , guesses , "gusses" 




import random
   top_of_range = ("Type a number:")

if top_of_range.isdigit
    top_of_range = int(top_of_range)

if top_of_range <= 0:
    print("please type a number more than  0 next time:")
else:
    print("please type a number next time ")
    quit()

random = random.randit("0 , top_of_range")
guesses = 0
while True:
guess+= 1
user_guess = ("make a guess")

if user_guess.isdigit
    user_guess = int(user_guess)
else:
    print("please type a number ")
    quit()
    continue

if user_guess = random number
    print ("you got the number right!")
   break
 else:
     if user_guess > random_number
        print("you were above the number!")
else:
    if user_guess < random_number
        print("you were below the number!")
,,,
elif user_guess > random_number
    print("you were above the number!")
else user_guess < random_number
    print("you were below the number!")
,,,

print("you got it in", guesses , "gusses")
