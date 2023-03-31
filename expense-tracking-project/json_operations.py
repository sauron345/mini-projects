import json


def load_json_data():
    with open('expenses.json') as f:
        json_expenses = json.load(f)

    return json_expenses


def save_data_to_json(data):
    with open('expenses.json', 'w') as f:
        json.dump(data, f, indent=4)


def get_expenses(expenses=None):
    if expenses is None:
        expenses = []
    try:
        json_expenses = load_json_data()
    except json.decoder.JSONDecodeError:
        pass
    else:
        for expense in json_expenses:
            expense_id, expense_amount, expense_type, expense_month = \
                expense['id'], expense['amount'], expense['type'], expense['month']

            expense_tuple = (expense_id, expense_amount, expense_type, expense_month)
            expenses.append(expense_tuple)

    return expenses
