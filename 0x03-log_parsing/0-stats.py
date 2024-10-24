#!/usr/bin/python3

import sys

# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

for line in sys.stdin:
    line_count += 1

    # Parse the line
    try:
        _, _, _, _, _, status, size = line.split()
        status = int(status)
        size = int(size)

        # Update totals
        total_size += size
        if status in status_codes:
            status_codes[status] += 1

    except ValueError:
        continue

    # Print stats every 10 lines or on KeyboardInterrupt
    if line_count % 10 == 0 or (line_count > 0 and sys.stdin.closed):
        print(f"File size: {total_size}")
        for code in sorted(status_codes):
            if status_codes[code] > 0:
                print(f"{code}: {status_codes[code]}")

# Handle KeyboardInterrupt
try:
    pass
except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
    sys.exit(0)
