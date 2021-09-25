from django.conf import settings
from random import choice
from string import ascii_letters, digits
from django.utils.crypto import get_random_string


AVAIABLE_CHARS = ascii_letters + digits

def create_random_code(chars=AVAIABLE_CHARS):
    return get_random_string (10)


