#!/usr/bin/python3
"""script that passes a http logs with metrics"""


if __name__ == "__main__":
    import sys

    def print_log(status_codes, file_size):
        """prints the formated stats"""
        print("File size: {:d}".format(file_size))
        for status_code, count in sorted(status_codes.items()):
            if count:
                print("{:s}: {:d}".format(status_code, count))
    status_codes = {"200": 0,
                    "301": 0,
                    "400": 0,
                    "401": 0,
                    "403": 0,
                    "404": 0,
                    "405": 0,
                    "500": 0
                    }
    file_size = 0
    lines = 0

    try:
        """Read stdin line by line"""
        for line in sys.stdin:
            if lines != 0 and lines % 10 == 0:
                # print every 10 lines
                print_log(status_codes, file_size)
            lines += 1
            log = line.split()
            try:
                # extract info
                status_code = log[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
                file_size = int(log[-1])
            except Exception:
                pass
        print_log(status_codes, file_size)
    except KeyboardInterrupt:
        # handle CTRL + C
        print_log(status_codes, file_sixe)
        raise
