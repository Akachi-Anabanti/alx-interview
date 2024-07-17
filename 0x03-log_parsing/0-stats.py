#!/usr/bin/python3
# Author: Anabanti Akachi

"""Defines a script that reads stdin line by line
of the format
`<IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>`
and prints the stats in specifiec format

`
File size: 14525
200: 1
300: 2
`
"""

import sys
from collections import defaultdict


# Defines the global variables
total_file_size = 0
status_codes_dict = defaultdict(int)  # sets dict keys to int data type
status_codes_list = [200, 301, 400, 401, 403, 404, 405, 500]

try:
    for line_count, line in enumerate(sys.stdin, start=1):
        parts = line.split(" ")
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        total_file_size += file_size

        # check if the status code is in the parsed status codes
        if status_code in status_codes_list and type(status_code) == int:
            # add the status code and set the count
            status_codes_dict[status_code] += 1

        if line_count % 10 == 0:
            # for every 10 lines
            print("File size: {}".format(total_file_size))
            for status_code in sorted(status_codes_dict.keys()):
                print("{}: {}".format(
                                      status_code,
                                      status_codes_dict[status_code]
                                      ))

except KeyboardInterrupt:  # Handle CTRL + C
    print("File size: {}".format(total_file_size))
    for status_code in sorted(status_codes_dict.keys()):
        print("{}: {}".format(status_code, status_codes_dict[status_code]))
