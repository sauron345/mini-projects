from datetime import date
from birth_weekday import get_weekday
from check_correctness import check_list, check_day, check_month, check_year
from comparing_dates import compare_birth_to_curr_date
from color_msg import Message as msg
import sys


def main_loop():

    while True:
        date_of_birth = input("Enter your date of your birth (or 'n' to exit) in sequence day-month-year: ")
        # ['1', '12', '2020']
        if date_of_birth.lower() == 'n':
            sys.exit()
        else:
            date_of_birth = date_of_birth.split('-')

        # check if items of list is numeric
        response = check_list(date_of_birth)
        if response is False:
            continue

        if (len(date_of_birth) < 4) and (len(date_of_birth) > 2):
            day_of_birth = date_of_birth[0]
            ver_day = check_day(day_of_birth)

            month_of_birth = date_of_birth[1]
            ver_month = check_month(month_of_birth)

            year_of_birth = date_of_birth[2]
            ver_year = check_year(year_of_birth)

            if int(year_of_birth) == date.today().year or int(year_of_birth) > date.today().year:
                compare_response = compare_birth_to_curr_date(date_of_birth)
                if compare_response is False:
                    continue

            if ver_day and ver_month and ver_year:
                get_weekday(date_of_birth)
                break

        else:
            print(msg.error('It should be: day-month-year, not more or less than that'))


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print(msg.error('\n\nKeyboard interrupted and finished the program'))
