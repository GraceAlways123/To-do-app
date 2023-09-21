# # Check if a string contains only lowercase letters

import string as st

while True:
    def only_lowercase_letter(string):
        for letter in string:
            if letter not in st.ascii_lowercase:
                return False
        return True

    user_input = input('Enter a string, all should be characters: ')
    
    if user_input == 'exit' or user_input == 'Exit' or user_input == 'EXIT':
        break

    elif only_lowercase_letter(user_input):
        user_message = f'{user_input}, contains only lowercase letters'
    else:
        user_message = f'{user_input}, contains one or more capital letters'

    print(user_message)

print('Thank you for your time, bye!')

# Generate a random password of lowercase letters
import random

def generate_password():
  password = ""
  for _ in range(8):
    password += random.choice(st.ascii_lowercase)
  return password

print(generate_password())


