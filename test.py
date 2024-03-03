import string
import random

def shuffle_string(input_string):
    temp_list = list(input_string)
    random.shuffle(temp_list)
    return ''.join(temp_list)

def generate_random_password():
    length_str = input("Enter desired number of characters for password: ")

    try:
        length = int(length_str)
        if length < 4:
            raise ValueError("Password length must be at least 4 characters.")
    except ValueError:
        print("Invalid input. Enter a valid integer for password length")
        return None

    # Combine all character sets (excluding potentially problematic characters)
    safe_punctuation = '!@#$%^&*()_-+=<>?/[]{}|'
    all_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + safe_punctuation

    # Generate random characters from each set
    upper_letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(length // 4))
    lower_letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(length // 4))
    numbers = ''.join(random.choice(string.digits) for _ in range(length // 4))
    special = random.choice(safe_punctuation)

    # Ensure unique characters
    remaining_chars = all_chars.replace(upper_letters + lower_letters + numbers + special, '')
    additional_chars = ''.join(random.choice(remaining_chars) for _ in range(length - len(upper_letters + lower_letters + numbers + special)))

    # Combine and shuffle all generated characters
    password = shuffle_string(upper_letters + lower_letters + numbers + special + additional_chars)

    return password

# Example: Generate a random password of length 16
generated_password = generate_random_password()
print(f'Generated password: {generated_password}')
