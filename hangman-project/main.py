import sys
from color_msg import Message as msg

trials = 5
solution = ['s', 'e', 'b', 's', 'o', 'n']
my_choices = []
correct_letters = ['_' for _ in solution]

try:

    while True:
        choice = input(f"Enter letter and resolve puzzle {correct_letters}: ")

        if not choice.isnumeric():
            if len(choice) < 2:
                my_choices.append(choice)
                found_letter = False

                for i, item in enumerate(solution):
                    if choice == item:
                        correct_letters.pop(i)
                        correct_letters.insert(i, item)
                        found_letter = True

                if not found_letter:
                    trials -= 1
                    if trials < 1:
                        print(msg.info('You used every trials'))
                        sys.exit()
                    else:
                        print(msg.error(f"You didn't found correct letter, trials left: {trials}"))
                else:
                    if '_' in correct_letters:
                        print(msg.success(f'You found correct letter, updated correct letters: {correct_letters}'))

                if correct_letters == solution:
                    correct_word = ''
                    for item in solution:
                        correct_word += item
                    print(msg.success(f'\nCongratulation! You resolved searching word! Correct word: {correct_word}'))
                    break

                print(msg.info(f'Used words: {my_choices}'))

            else:
                print(msg.error('Only one letter is allowed!'))

        else:
            print(msg.error('Only letters are allowed not digits or other characters'))

except KeyboardInterrupt:
    print(msg.error('\nKeyboard interrupted and finished the program'))
