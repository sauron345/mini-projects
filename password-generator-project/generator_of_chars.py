from random import choice
import string


def generate_digits(num_digits):
    i = 0
    while i < num_digits:
        yield choice(string.digits)
        i += 1


def generate_low_letters(num_low_letters):
    i = 0
    while i < num_low_letters:
        yield choice(string.ascii_lowercase)
        i += 1


def generate_upp_letters(num_upp_letters):
    i = 0
    while i < num_upp_letters:
        yield choice(string.ascii_uppercase)
        i += 1
