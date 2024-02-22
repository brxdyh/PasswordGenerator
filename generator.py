# random password generator
# by brad :p

import string
import random

# function that shuffles all characters in a string
def shuffle(input_string):
    temp = list(input_string)
    random.shuffle(temp)
    return ''.join(temp)

# stores all uppercase char ASCII codes and generates random uppercase letters 
# then stores the values in a variable
upperChars = list(string.ascii_uppercase)
upperLetter1 = random.choice(upperChars)
upperLetter2 = random.choice(upperChars)
upperLetter3 = random.choice(upperChars)
upperLetter4 = random.choice(upperChars)

# stores all lowercase char ASCII codes and generates random lowercase letters
# then stores the values in a variable
lowerChars = list(string.ascii_lowercase)
lowerLetter1 = random.choice(lowerChars)
lowerLetter2 = random.choice(lowerChars)
lowerLetter3 = random.choice(lowerChars)
lowerLetter4 = random.choice(lowerChars)

# stores all digit/integer ASCII codes, generates random chars, and stores the value
numbers = string.digits
num1 = random.choice(numbers)
num2 = random.choice(numbers)

# stores all special char ASCII codes, generates random char, and stores the value
special_characters = string.punctuation
special_char1 = random.choice(special_characters)

# grabs all generated values and creates a random password with them
# variable shortened for easier reading
upper_letters = upperLetter1 + upperLetter2 + upperLetter3 + upperLetter4
lower_letters = lowerLetter1 + lowerLetter2 + lowerLetter3 + lowerLetter4
numbers = num1 + num2
special = special_char1

passwd = upper_letters + lower_letters + numbers + special
passwd = shuffle(passwd)

# show generated password
print(passwd)