from datetime import datetime
from color_message import Message as msg


def get_weekday(birth_date: list) -> None:
    date_str = birth_date[0] + "-" + birth_date[1] + "-" + birth_date[2]
    weekday = datetime.strptime(date_str, '%d-%m-%Y').strftime('%A')
    print(msg.info(f"Day of week you born is: {weekday}"))
