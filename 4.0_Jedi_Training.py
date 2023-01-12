# Sign your name:________________
from timeit import timeit

#1. Make the following program work. (3 mistakes)

# midichlorians = float(input("Enter midichlorian count: "))
#
# if midichlorians > 10000:
#     print("you have serious Jedi potential")
#
# else: midichlorians < 10000
#
# print("Jedi, you will never be")




 # # 2. Make the following program work. (3 mistakes)

# x = int(input("Enter a number: "))
# if x == 3:
#     print("You entered 3")
 #
 #
 #  # 3. Make the following program work. (4 mistakes)
# mistakes
# answer = input("What is the name of Poe Dameron's Droid? ")
# if answer.upper() == "BB8":
#          print("Correct!")
# else:
#          print("Incorrect! It is BB8.")

 #
 #  # 4. Make the following program work. (4 mistakes)
 #
# Jedi = input("Name one of the top 3 greatest Jedi.")
# if Jedi.lower == "yoda" or Jedi.lower == "luke skywalker" or Jedi.lower == "obi-wan kenobi":
#          print("That is correct!")
#
#
#  #
 # # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.

print("Welcome to the Jedi Academy!")
print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?")

if user_input.upper() == "A":
         print("wrong")
elif user_input.upper() == "B":
         sensitivity = 900
elif user_input.upper() == "C":
         sensitivity = 0



print("Sensitivity: ",sensitivity)

# timeit(10)
# for letter in "death star":
#     if letter == " ":
#         break
#     print('current letter :',letter)
#
# var = 10
# while var > 0
#     print("current variable value: ",var)
#     var-=1