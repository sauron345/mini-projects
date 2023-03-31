from generator_of_chars import generate_low_letters, generate_upp_letters, generate_digits
from check_correctness import check_correctness_of_chars
from color_message import Message as msg
from random import sample


def main_loop() -> None:

    while True:
        low_letters_num = check_correctness_of_chars("lowercase letters", 10)

        upp_letters_num = check_correctness_of_chars("uppercase letters", 1)

        digits_num = check_correctness_of_chars("digits", 1)

        # generate random characters
        rand_low_letters_list = list(generate_low_letters(low_letters_num))
        rand_upp_letters_list = list(generate_upp_letters(upp_letters_num))
        rand_digits_list = list(generate_digits(digits_num))

        # convert list to string
        low_letters = ''.join(rand_low_letters_list)
        upp_letters = ''.join(rand_upp_letters_list)
        digits = ''.join(rand_digits_list)

        password_str = low_letters + upp_letters + digits
        password = ''.join(sample(password_str, len(password_str)))

        print(f"{msg.success('Your password is successfully created')}\n{'*'*len(password)}")
        choice = input("Do you want to see the password? (y/n): ")
        if choice.lower() == 'y':
            print(msg.info(f"{password=}"))

        break


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print(msg.error('\nKeyboard interrupted and finished the program'))
