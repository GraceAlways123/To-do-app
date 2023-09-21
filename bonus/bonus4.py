# A python script to check if password is strong or weak
password = input('Enter the password: ')
result = {}

# Check if the inputed password length is greater than or equal to 8
if len(password) >= 8:
    result['length'] = True

else:
    result['length'] = False

# Check if there is any digit included in the given password
digit = False

for item in password:
    if item.isdigit():
        digit = True

result['digit'] = digit
uppercase = False

for item in password:
    if item.isupper():
        uppercase = True

result['uppercase'] = uppercase

if all(result.values()):
    print('Strong Password!')
else:
    print('Weak Password!')