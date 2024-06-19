#!/usr/bin/env python3
import sys
import signal

total_size = 0
status_codes_count = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0


def print_statistics():
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def handle_interrupt(signal, frame):
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 7:
                continue
            ip = parts[0]
            date = parts[3] + ' ' + parts[4]
            request = parts[5] + ' ' + parts[6] + ' ' + parts[7]
            status_code = parts[-2]
            file_size = int(parts[-1])
            if request != '"GET /projects/260 HTTP/1.1"':
                continue

            total_size += file_size
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_statistics()

        except Exception as e:
            continue
except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)

print_statistics()
