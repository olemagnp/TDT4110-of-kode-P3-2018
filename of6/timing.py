
seconds_per_hour = 3600
seconds_per_min = 60


def formatTime(seconds):
    hours = seconds // seconds_per_hour
    seconds = seconds - seconds_per_hour * hours

    minutes = seconds // seconds_per_min
    seconds = seconds - seconds_per_min * minutes

    formatted = f"{hours:02d}:{minutes:02d}:{str(seconds).rjust(2, '0')}"
    formatted = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    return formatted


print(formatTime(12305))
