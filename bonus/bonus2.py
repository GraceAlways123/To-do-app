# Coding exercise 84. Real life coding challenge
# A coin-flip probability program

user_input = input('Throw the coin and enter head or tail here: ? ')

while user_input == 'tail' or user_input == 'head':
    with open('../user_entry.txt', 'r') as file:
        each_user_entry = file.readlines()
        
    each_user_entry.append(user_input + '\n')
    
    with open('../user_entry.txt', 'w') as file:
        file.writelines(each_user_entry)
    
    current_percentage_of_heads = float(each_user_entry.count('head\n') / len(each_user_entry)) * 100

    print(f"Heads: {current_percentage_of_heads}%")

    user_input = input('Throw the coin and enter head or tail here: ? ')

# Clear out the data in the 'user_entry.txt' file since the game is over using with content manager
with open('../user_entry.txt', 'w') as file:
    file.write('')

message = "You didn't enter a head or a tail. This is the end of the game. \nThanks and bye!."
print(message)
