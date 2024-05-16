#!/usr/bin/python3
'''0-stats.py'''


import sys
import signal
import re


total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    '''print_stats'''
    print("File size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        if count > 0:
            print(status_code, ":", count)

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    line = line.strip()
    match = re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$', line)
    if match:
        status_code = int(match.group(1))
        file_size = int(match.group(2))
        total_file_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()
