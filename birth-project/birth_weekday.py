from datetime import datetime
from color_msg import Message as msg


def get_weekday(date_of_birth):
    date_str = date_of_birth[0] + "-" + date_of_birth[1] + "-" + date_of_birth[2]
    weekday = datetime.strptime(date_str, '%d-%m-%Y').strftime('%A')
    print(msg.success(f"Day of week you born is: {weekday}"))
