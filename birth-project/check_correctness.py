from datetime import date
from color_message import Message as msg


def verify_correctness(correct, correct2=None, correct3=None) -> bool:
    if correct3 is not None:
        return True if correct and correct2 and correct3 else False
    elif correct2 is not None:
        return True if correct and correct2 else False
    else:
        return True if correct else False


def check_list(birth_date: list) -> bool:
    for item in birth_date:
        if not item.isdigit():
            print(msg.error('Digits are only allowed!'))
            return False

    return True


def check_day(birth_day: str) -> bool:
    correct = True
    correct2 = True

    if len(birth_day) > 2:
        print(msg.error('There is no day greater than 2 digits'))
        correct = False

    if int(birth_day) > 31:
        print(msg.error('There is no day greater than 31'))
        correct2 = False

    return verify_correctness(correct, correct2)


def check_month(birth_month: str) -> bool:
    correct = True
    correct2 = True

    if len(birth_month) > 2:
        print(msg.error('There is no month greater than 2 digits'))
        correct = False

    if int(birth_month) > 12:
        print(msg.error('There is no month greater than 12'))
        correct2 = False

    return verify_correctness(correct, correct2)


def check_year(birth_year: str) -> bool:
    correct = True

    curr_year = str(date.today().year)
    len_curr_year = len(curr_year)

    if len(birth_year) > len_curr_year:
        print(msg.error(f'There is no year greater than {len_curr_year} digits'))
        correct = False

    return verify_correctness(correct)
