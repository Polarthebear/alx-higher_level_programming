#!/usr/bin/python3
"""Reads from standard input and computes metrics

After every 10 lines or if input of CTRL + C,
the following statistics will be printed:
    - The total file size up to that point
    - Count of the read status codes up to that point
"""


def print_stats(size, status_codes):
    """Print built up metrics

    Args:
        size (int): Total file size calculated from input lines.
        status_codes (dict): Dictionary containing
        counts of diffrent HTTP status codes

    Return:
        Display the total file size and
        counts of each HTTP status code in a sorted order
    """
    print(f"File size: {size}")
    for key in sorted(status_codes):
        print(f"{key}: {status_codes[key]}")


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_stats(size, status_codes)
                line_count = 1
            else:
                line_count += 1

            line_parts = line.split()

            try:
                current_size = int(line_parts[-1])
                size += current_size
            except (IndexError, ValueError):
                pass

            try:
                current_code = line_parts[-2]
                if current_code in valid_codes:
                    status_codes[current_code] =
                    status_codes.get(current_code, 0) + 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
