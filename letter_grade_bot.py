# Project 1
# Letter Grade Bot

pointspossible = 100
score = 74
studentname = 'Nick'

'''
A - 100-90%
B - 89-80%
C - 79-70%
D - 69-60%
F - 59-0%
'''

# Print the student name and what grade they got

# Get percentage from pointspossible and score
percentage = float(score) / float(pointspossible)

# Get grade from percentage
sentence = studentname + ", your score is " + str(score) + "."
sentence += "\nYour grade is "

if 0 <= percentage <= 0.59:
    sentence += "F"
elif 0.6 <= percentage <= 0.69:
    sentence += "D"
elif 0.7 <= percentage <= 0.79:
    sentence += "C"
elif 0.8 <= percentage <= 0.89:
    sentence += "B"
elif 0.9 <= percentage <= 1:
    sentence += "A"

sentence += "."
print(sentence)
