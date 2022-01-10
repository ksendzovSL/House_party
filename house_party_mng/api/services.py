import string
import random

from api.models import Room


def generate_unique_code() -> str:
    """
    Function generates a random code while creating music room
    """
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code
