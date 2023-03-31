from datetime import date
from birth_weekday import get_weekday
from check_correctness import check_list, check_day, check_month, check_year
from comparing_dates import compare_birth_to_curr_date
from color_message import Message as msg
import sys


def main_loop() -> None:

    while True:
        birth_date = input("Enter your date of your birth (or 'n' to exit) in sequence day-month-year: ")
        # ['1', '12', '2020']
        if birth_date.lower() == 'n':
            sys.exit()
        else:
            birth_date = birth_date.split('-')

        # check if items of list is numeric
        response = check_list(birth_date)
        if response is False:
            continue

        if (len(birth_date) < 4) and (len(birth_date) > 2):
            birth_day = birth_date[0]
            ver_day = check_day(birth_day)

            birth_month = birth_date[1]
            ver_month = check_month(birth_month)

            birth_year = birth_date[2]
            ver_year = check_year(birth_year)

            if int(birth_year) == date.today().year or int(birth_year) > date.today().year:
                compare_response = compare_birth_to_curr_date(birth_date)
                if compare_response is False:
                    continue

            if ver_day and ver_month and ver_year:
                get_weekday(birth_date)
                break

        else:
            print(msg.error('It should be: day-month-year, not more or less than that'))


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print(msg.error('\n\nKeyboard interrupted and finished the program'))
