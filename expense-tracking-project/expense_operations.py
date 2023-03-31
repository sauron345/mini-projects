from json_operations import load_json_data, save_data_to_json
from color_msg import Message as msg


def show_expenses(month: str, expenses: list) -> None:
    if expenses:
        json_expenses = load_json_data()

        have_expense = False
        for expense in json_expenses:
            if expense['month'] == month:
                expense_info = f"id: {expense['id']} - {expense['type']} - {expense['amount']} zł"
                print(msg.info(expense_info))
                have_expense = True

        if not have_expense:
            print(msg.error(f"You don't have expenses in {month}"))

    else:
        print(msg.error(f"You don't have any expenses"))


def save_expense(expenses: list) -> None:
    data = []

    for expense_id, expense_amount, expense_type, month in expenses:
        data.append({
            'id': expense_id,
            'amount': expense_amount,
            'type': expense_type,
            'month': month,
        })

    save_data_to_json(data)


def add_expense(month: str, expenses: list, expense_id: int) -> None:
    expense_amount = input('Enter amount [zł]: ')

    if not expense_amount.isdigit():
        print(msg.error('Only digits are allowed'))
        add_expense(month, expenses, expense_id)
    else:
        expense_type = input('Enter type of expense (eating, entertainment, home, e.t.c): ')
        expense = (expense_id, int(expense_amount), expense_type, month)
        expenses.append(expense)
        save_expense(expenses)


def show_stats(selected_month: str, expenses: list) -> None:
    """Stats of selected month and all month"""
    total_amount_of_selected_month = sum(expense_amount for _, expense_amount, _, month in expenses
                                         if month == selected_month)

    number_of_expenses_of_selected_month = sum(1 for _, expense_amount, _, month in expenses if month == selected_month)

    if number_of_expenses_of_selected_month != 0:
        average_of_expenses_of_selected_month = total_amount_of_selected_month / number_of_expenses_of_selected_month
    else:
        average_of_expenses_of_selected_month = 0

    total_amount = sum(expense_amount for _, expense_amount, _, month in expenses)

    if len(expenses) > 0:
        average_expense = total_amount / len(expenses)
        average_expense = round(average_expense, 2)
    else:
        average_expense = 0

    print(msg.info('Statistics:'))
    print(msg.info(f"All expenses in {selected_month} [zł]: {total_amount_of_selected_month}"))
    print(msg.info(f"Average of expenses in {selected_month} [zł]: {average_of_expenses_of_selected_month}"))
    print(msg.info(f"All expenses [zł]: {total_amount}"))
    print(msg.info(f"Average of expenses [zł]: {average_expense}"))


def delete_expense(month: str, expenses: list) -> None:
    if expenses:
        json_data = load_json_data()
        have_expense = False
        for expense in json_data:
            if expense['month'] == month:
                have_expense = True

        if have_expense:
            choice = input('Choose which expense you want to delete entering his id: ')

            if choice.isdigit():
                choice = int(choice)
                del_expense = False
                for expense in json_data:
                    if expense['month'] == month:
                        if choice == expense['id']:
                            expense_id, expense_amount, expense_type, expense_month \
                                = expense['id'], expense['amount'], expense['type'], expense['month']

                            del_expense = expenses.index((expense_id, expense_amount, expense_type, expense_month))
                            expenses.pop(del_expense)
                            save_expense(expenses)
                            print(msg.success(f"You delete expense: (id: {expense_id} - {expense_type} - {expense_amount} zł)"))
                            del_expense = True

                if not del_expense:
                    print(msg.error(f"Expense with id: {choice}, does not exists in {month}"))
            else:
                print(msg.error(f"Only digits are allowed"))
                delete_expense(month, expenses)
        else:
            print(msg.error(f"You don't have expenses in {month}"))
    else:
        print(msg.error("You don't have any expenses"))
