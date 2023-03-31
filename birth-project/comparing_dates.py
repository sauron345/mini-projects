from datetime import date
from check_correctness import verify_correctness
from color_message import Message as msg


def compare_birth_to_curr_date(birth_date: list) -> bool:
    birth_day = int(birth_date[0])
    birth_month = int(birth_date[1])
    birth_year = int(birth_date[2])

    curr_year = date.today().year

    correct = True
    correct2 = True
    correct3 = True

    if birth_year > curr_year:
        current_year = curr_year
        print(msg.error(f'Entered year is greater than current year: {current_year}'))
        correct = False
    else:
        curr_month = date.today().month
        curr_day = date.today().day

        if birth_month > curr_month:
            print(msg.error("Entered month is greater than current month"))
            correct3 = False

        elif birth_day > curr_day and birth_month == curr_month:
            print(msg.error("Entered day is greater than current day"))
            correct2 = False

    return verify_correctness(correct, correct2, correct3)



