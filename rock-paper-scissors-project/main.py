from random import randint
from color_message import Message as msg


def main_loop(tools: list) -> None:

    while True:
        won, lost, won_per, lost_per, level = 0, 0, 0, 0, 1

        for _ in range(10):
            choice = input(f'Level {level}, choose: rock, paper or scissors: ')

            if choice not in tools:
                print(msg.error(f'Only {tools} are allowed!'))
                continue

            choice = tools.index(choice)
            rand_num = randint(0, 2)

            if choice == rand_num:
                print(msg.success('You won'))
                won += 1
            else:
                print(msg.error('You lost'))
                lost += 1

            level += 1

        won_per = int(100 * (won / 10))
        lost_per = int(100 * (lost / 10))
        print(msg.info(f'\nYour stats:\nwon - {won_per} %\nlost - {lost_per} %'))

        if won > lost or won == 5:
            print(msg.success('\nYou won the game!'))
            break

        choice = input('\nYou wanna try again? (n - exit): ')
        if choice.lower() == 'n':
            break


if __name__ == '__main__':
    tools = ['rock', 'paper', 'scissors']
    try:
        main_loop(tools)
    except KeyboardInterrupt:
        print(msg.error('\nKeyboard interrupted and finished the program'))