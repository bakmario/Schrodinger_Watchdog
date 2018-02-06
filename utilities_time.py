import datetime

# The epoch used in the datetime API.
EPOCH = datetime.datetime.utcfromtimestamp(0)


def timedelta_to_seconds(delta):
    seconds = (delta.microseconds * 1e6) + delta.seconds + (delta.days * 86400)
    seconds = abs(seconds)

    return seconds


def datetime_to_timestamp(date, epoch=EPOCH):
    # Ensure we deal with `datetime`s.
    date = datetime.datetime.fromordinal(date.toordinal())
    epoch = datetime.datetime.fromordinal(epoch.toordinal())

    timedelta = date - epoch
    timestamp = timedelta_to_seconds(timedelta)

    return timestamp


def timestamp_to_datetime(timestamp, epoch=EPOCH):
    # Ensure we deal with a `datetime`.
    epoch = datetime.datetime.fromordinal(epoch.toordinal())

    epoch_difference = timedelta_to_seconds(epoch - EPOCH)
    adjusted_timestamp = timestamp - epoch_difference

    date = datetime.datetime.utcfromtimestamp(adjusted_timestamp)

    return date

