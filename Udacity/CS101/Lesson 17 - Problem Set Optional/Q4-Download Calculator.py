# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

# print 2 ** 10      # one kilobit, kb
# print 2 ** 10 * 8  # one kilobyte, kB

# print 2 ** 20      # one megabit, Mb
# print 2 ** 20 * 8  # one megabyte, MB

# print 2 ** 30      # one gigabit, Gb
# print 2 ** 30 * 8  # one gigabyte, GB

# print 2 ** 40      # one terabit, Tb
# print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).


# Converts given unit to bits
def unit_converter(size, unit):
    if 'k' in unit:
        size *= 2.0 ** 10
    elif 'M' in unit:
        size *= 2.0 ** 20
    elif 'G' in unit:
        size *= 2.0 ** 30
    elif 'T' in unit:
        size *= 2.0 ** 40
    return size


def download_time(file_size, file_unit, bandwidth, bandwidth_unit):
    # Convert Bytes to bits:
    if 'B' in bandwidth_unit:
        bandwidth *= 8.0
    if 'B' in file_unit:
        file_size *= 8.0

    # Expand units to bits:
    file_size = unit_converter(file_size, file_unit)
    bandwidth = unit_converter(bandwidth, bandwidth_unit)

    # Calculate seconds
    seconds = file_size / bandwidth

    # Convert seconds to hours, minutes, and seconds string
    output = []

    hours = seconds // 3600
    if hours:
        seconds = seconds % 3600

    minutes = seconds // 60
    if minutes:
        seconds = seconds % 60

    if hours == 1:
        output.append("1 hour, ")
    else:
        output.append(str(int(hours)) + " hours, ")

    if minutes == 1:
        output.append("1 minute, ")
    else:
        output.append(str(int(minutes)) + " minutes, ")

    if seconds == 1:
        output.append("1 second")
    else:
        output.append(str(seconds) + " seconds")

    return ''.join(output)


print(download_time(1024, 'kB', 1, 'MB'))
# >>> 0 hours, 0 minutes, 1 second

print(download_time(1024, 'kB', 1, 'Mb'))
# >>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print(download_time(13, 'GB', 5.6, 'MB'))
# >>> 0 hours, 39 minutes, 37.1428571429 seconds

print(download_time(13, 'GB', 5.6, 'Mb'))
# >>> 5 hours, 16 minutes, 57.1428571429 seconds

print(download_time(10, 'MB', 2, 'kB'))
# >>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print(download_time(10, 'MB', 2, 'kb'))
# >>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable
