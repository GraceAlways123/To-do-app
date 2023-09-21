from parse7 import parse
from feet_convert_to_inches import feet_convert_to_inches

feet_inches = input('Enter feet value first and then inches value: ')
# Using function decoupling to decouple the function feet_convert_to_inches() so as not to over work it.

parsed = parse(feet_inches)
converted = feet_convert_to_inches(parsed['feet'], parsed['inches'])
message = f"{parsed['feet']} feets and {parsed['inches']} inches is equal to {converted} meters."

print(message)

if converted > 1:
    print('Kid can use the slide.')
else:
    print('Kid is too small.')
