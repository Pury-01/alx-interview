#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys


def print_stats(total_size, status_counts):
    """
    Prints the aggregated statistics: total file size and
    status code counts.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


if __name__ == "__main__":
    total_size = 0
    status_counts = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0
            }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.strip().split(" ")

            # Validate line format
            if len(parts) < 7:
                continue

            # Extract file size
            try:
                file_size = int(parts[-1])
                total_size += file_size
            except ValueError:
                continue

            # Extract status code
            try:
                status_code = int(parts[-2])
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except ValueError:
                continue

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        # Print stats upon keyboard interruption
        print_stats(total_size, status_counts)
        raise

    # Print stats at the end of input
    print_stats(total_size, status_counts)
