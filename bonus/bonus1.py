date = input("Enter today's date: ")

mood = input('How do you rate your mood today from 1 to 10?: ')

thoughts = input('Let your thoughts flow: \n')

with open(f'../Journal/{date}.txt', 'w') as file:
    file.writelines('mood rating: ' + mood + '\n\n')
    file.writelines('my thoughts for today is:' + '\n\t' + thoughts)
