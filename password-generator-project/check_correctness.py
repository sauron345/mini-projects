from color_msg import Message as msg


def check_correctness_of_chars(type_of_chars: str, min_required: int) -> int:
    num_of_chars = input(f'How much {type_of_chars} you want? (at least {min_required} is required): ')
    if not num_of_chars.isdigit():
        print(msg.error('Only digits are allowed'))
        return check_correctness_of_chars(type_of_chars, min_required)
    if int(num_of_chars) < min_required:
        print(msg.error(f'At least {min_required} digit is required'))
        return check_correctness_of_chars(type_of_chars, min_required)
    else:
        return int(num_of_chars)
