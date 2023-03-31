from random import choice
import string
from typing import Iterable


def generate_digits(digits_num: int) -> Iterable:
    i = 0
    while i < digits_num:
        yield choice(string.digits)
        i += 1


def generate_low_letters(low_letters_num: int) -> Iterable:
    i = 0
    while i < low_letters_num:
        yield choice(string.ascii_lowercase)
        i += 1


def generate_upp_letters(upp_letters_num: int) -> Iterable:
    i = 0
    while i < upp_letters_num:
        yield choice(string.ascii_uppercase)
        i += 1
