import random

def default_input(userinput):
    if userinput == '':
         return 'rock,paper,scissors'
    return userinput


user_name = input('Enter your name:')
print(f'Hello, {user_name}')

file = open('rating.txt')
user_score = 0
for line in file:
    name, score = line.split()
    if name == user_name:
        user_score = int(score)

user_combinations = input()
user_combinations = default_input(user_combinations)
list_input = list(user_combinations.split(sep=','))

file.close()
print("Okay, let's start")

# correct_input = ['scissors', 'rock', 'paper', '!rating']
correct_input = list_input[:]
correct_input.append('!rating')
user_input = input()

while user_input != '!exit':
    if user_input not in correct_input:
        print('Invalid input')
    elif user_input == '!rating':
        print(f'Your rating: {user_score}')
    else:
        computer_choice = random.choice(list_input)
        user_index = list_input.index(user_input)
        new_list = list_input[user_index + 1:] + list_input[: user_index]
        win_list = new_list[len(new_list) // 2:]

        if user_input == computer_choice:
            print(f'There is a draw ({user_input})')
            user_score += 50
        # elif win_combinations[user_input] == computer_choice:
        elif computer_choice  in win_list:
            print(f'Well done. Computer chose {computer_choice} and failed')
            user_score += 100
        else:
            print(f'Sorry, but computer chose {computer_choice}')
    user_input = input()

print('Bye!')