from datetime import date
from color_msg import Message as msg


def verify_correctness(correct, correct2=None, correct3=None):
    if correct3 is not None:
        return True if correct and correct2 and correct3 else False
    elif correct2 is not None:
        return True if correct and correct2 else False
    else:
        return True if correct else False


def check_list(date_of_birth):
    for item in date_of_birth:
        if not item.isdigit():
            print(msg.error('Digits are only allowed!'))
            return False

    return True


def check_day(date_of_birth):
    correct = True
    correct2 = True

    if len(date_of_birth) > 2:
        print(msg.error('There is no day greater than 2 digits'))
        correct = False

    if int(date_of_birth) > 31:
        print(msg.error('There is no day greater than 31'))
        correct2 = False

    return verify_correctness(correct, correct2)


def check_month(month_of_birth):
    correct = True
    correct2 = True

    if len(month_of_birth) > 2:
        print(msg.error('There is no month greater than 2 digits'))
        correct = False

    if int(month_of_birth) > 12:
        print(msg.error('There is no month greater than 12'))
        correct2 = False

    return verify_correctness(correct, correct2)


def check_year(year_of_birth):
    correct = True

    curr_year = str(date.today().year)
    len_curr_year = len(curr_year)

    if len(year_of_birth) > len_curr_year:
        print(msg.error(f'There is no year greater than {len_curr_year} digits'))
        correct = False

    return verify_correctness(correct)
