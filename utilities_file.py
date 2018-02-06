import os
from utilities_time import timestamp_to_datetime


def touch_file(path):
    os.utime(path, times=None)
    print(path + " was touched")


def get_modification_date(path):
    return timestamp_to_datetime(os.path.getmtime(path))