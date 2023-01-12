'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

print("Welcome to my quiz about world geography, lets see how many you can get right")

total = 7
score = 0

print("What is the capital of Canada?")
Answer = input("Answer: ")
if Answer == "Ottawa" or Answer == "ottawa":
    print("Thats Right!")
    score += 1
else:
    print("Incorrect its Ottawa")


print("What mountain range is Mt. Everest apart of?")
Answer = input("Answer: ")
if Answer == "Himalayas" or Answer == "himalayas":
    print("Correct")
    score += 1
else:
    print("Incorrect it was Himalayas")

print("90% of the Earths population lives in which Hemisphere?")
Answer = input("Answer: ")
if Answer == "Northern Hemisphere" or Answer == "northern hemisphere":
        print("Correct!")
        score += 1
else:
        print("Incorrect it is the northern hemisphere")

print("What river flows through the Grand Canyon")

print("Colorado River")
print("Nile River")
print("Mississippi river")
print("Lena River")
Answer = input("Answer: ")
if Answer.lower() == "colorado river":
    print("Correct")
    score += 1
else:
    print("Wrong its the Colorado river")

print("What country does the Rhine River Flow Through")
print("Mongolia")
print("Eritrea")
print("Germany")
print("Romania")
Answer = input("Answer: ")
if Answer == "Germany":
    print("Nice")
    score += 1
else:
    print("Nice Try it was germany")

print("what is the official currency of Britan")
print("Shekel")
print("Pound Sterling")
print("Dollar")
print("Rupee")
Answer = input("Answer: ")
if Answer == "Pound Sterling":
    print("Nice!")
    score += 1
else:
    print("wrong")

print("How Many time zones are in Australia")
print("1")
print("2")
print("3")
print("4")
Answer = input("Answer: ")
if Answer == "3":
    print("Correct")
    score += 1
else:
    print("Wrong its 3")

per = score/total*100
print("your score is",score)