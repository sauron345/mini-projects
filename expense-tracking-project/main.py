from json_operations import get_expenses
from expense_operations import show_expenses, add_expense, show_stats, delete_expense
from datetime import datetime
from color_message import Message as msg
import sys


def main_loop(expenses: list, expense_id: int) -> None:

    while True:
        month = input('Choose a month [1-12] (exit - n): ')

        if month.lower() == 'n':
            sys.exit()

        if not month.isdigit():
            print(msg.error('Only digits are allowed'))
            continue
        elif not ((int(month) > 0) and (int(month) < 13)):
            print(msg.error('Only month between [1-12] exists'))
            continue

        month = datetime.strptime(month, '%m').strftime('%B')

        while True:
            print(f"\nSelected month: {month}")
            print('0. Back to month selection')
            print('1. Show month expenses')
            print('2. Add expense')
            print('3. Statistics')
            print('4. Delete expense')
            response = input('Choose option: ')
            print()

            if not response.isdigit():
                print(msg.error('Only digits are allowed'))
                continue

            response = int(response)

            if response == 0:
                break
            elif response == 1:
                show_expenses(month, expenses)
            elif response == 2:
                expense_id += 1
                add_expense(month, expenses, expense_id)
            elif response == 3:
                show_stats(month, expenses)
            elif response == 4:
                delete_expense(month, expenses)
            else:
                print(msg.error('Only [0-4] digits are allowed'))


if __name__ == '__main__':
    try:
        expenses = get_expenses()
        # expense_id = 0 if list expenses is empty
        expense_id = expenses[-1][0] if expenses else 0
        main_loop(expenses, expense_id)
    except KeyboardInterrupt:
        print(msg.error('\n\nKeyboard interrupted and finished the program'))
