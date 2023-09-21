def parse(feet_inches_args):
    split_parts = feet_inches_args.split(' ')

    feets = float(split_parts[0])
    inches = float(split_parts[1])

    return {'feet': feets, 'inches': inches}

print('This is parse() function')