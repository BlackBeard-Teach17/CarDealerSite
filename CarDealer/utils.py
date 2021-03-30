import datetime
import os
import random
import string

from django.utils import timezone
from django.utils.text import slugify


def get_filename(path):
    return os.path.basename(path)


def random_string_generator(size=20, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
