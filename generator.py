# Random Password Generator
# by brad :p

import string
import random

# function that shuffles all characters in a string
def shuffle(string):
    temp = list(string)
    random.shuffle(temp)
    return ''.join(temp)

# generate random uppercase letters from ASCII code and stores the values in a variable
upperLetter1 = chr(random.randint(65, 90))
upperLetter2 = chr(random.randint(65, 90))
upperLetter3 = chr(random.randint(65, 90))
upperLetter4 = chr(random.randint(65, 90))

# generate random lowercase letters from ASCII code and stores the values in a variable
lowerLetter1 = chr(random.randint(97, 122))
lowerLetter2 = chr(random.randint(97, 122))
lowerLetter3 = chr(random.randint(97, 122))
lowerLetter4 = chr(random.randint(97, 122))

# generate random number from ASCII code and stores the value
# creates two numbers, cannot figure out why ?
num1 = int(random.randint(48, 57))

# generates special character from ASCII code and stores the value
special_characters = string.punctuation
special_char1 = random.choice(special_characters)

# grabs all generated values and creates a random password with them
# variable shortened for easier reading
upper_letters = upperLetter1 + upperLetter2 + upperLetter3 + upperLetter4
lower_letters = lowerLetter1 + lowerLetter2 + lowerLetter3 + lowerLetter4
numbers = str(num1)
special = str(special_char1)
passwd = upper_letters + lower_letters + numbers + special
passwd = shuffle(passwd)

# show generated password
print(passwd)