from datetime import date
from check_correctness import verify_correctness
from color_msg import Message as msg


def compare_birth_to_curr_date(date_of_birth):
    day_of_birth = int(date_of_birth[0])
    month_of_birth = int(date_of_birth[1])
    year_of_birth = int(date_of_birth[2])

    curr_year = date.today().year

    correct = True
    correct2 = True
    correct3 = True

    if year_of_birth > curr_year:
        current_year = curr_year
        print(msg.error(f'Entered year is greater than current year: {current_year}'))
        correct = False
    else:
        curr_month = date.today().month
        curr_day = date.today().day

        if month_of_birth > curr_month:
            print(msg.error("Entered month is greater than current month"))
            correct3 = False

        elif day_of_birth > curr_day and month_of_birth == curr_month:
            print(msg.error("Entered day is greater than current day"))
            correct2 = False

    return verify_correctness(correct, correct2, correct3)



