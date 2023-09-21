feet_inches = input('Enter feet value first and then inches value: ')
# Using function decoupling to decouple the function feet_convert_to_inches() so as not to over work it.

def parse(feet_inches_args):
    split_parts = feet_inches_args.split(' ')

    feets = float(split_parts[0])
    inches = float(split_parts[1])

    return {'feet': feets, 'inches': inches}


def feet_convert_to_inches(feets, inches):
    meters = feets * 0.3048 + inches * 0.0254
    return meters


parsed = parse(feet_inches)
converted = feet_convert_to_inches(parsed['feet'], parsed['inches'])
message = f"{parsed['feet']} feets and {parsed['inches']} inches is equal to {converted} meters."

print(message)

if converted > 1:
    print('Kid can use the slide.')
else:
    print('Kid is too small.')