#!/usr/bin/python3
"""This module contains a script about
log parsing"""

import sys
import signal

"""Initialize variables"""
slit_line = []
file_size = 0
num_file = {}
ct = 0


def signal_handler(signal, frame):
    """Signal handler function to print file size and HTTP status codes."""
    sys.stdout.write("File size: {}\n".format(file_size))
    for k, v in sorted(num_file.items()):
        sys.stdout.write("{}: {}\n".format(k, v))


"""Register signal handler for SIGINT"""
signal.signal(signal.SIGINT, signal_handler)

"""Iterate over input lines"""
for line in sys.stdin:
    """Split the line"""
    split_line = line.split()
    """Update total file size"""
    file_size += int(split_line[-1])
    """List of HTTP status codes"""
    list_code = ["200", "301", "400", "401", "403", "404", "405", "500"]
    """Check if status code is in the dictionary"""
    if split_line[-2] in num_file and split_line[-2] in list_code:
        """Increment count if status code exists"""
        num_file[split_line[-2]] += 1
        ct += 1
    elif split_line[-2] in list_code:
        """Add status code to dictionary if it doesn't exist"""
        num_file[split_line[-2]] = 1
        ct += 1
    """Check if 10 lines have been processed"""
    if ct == 10:
        """Print file size and status codes"""
        sys.stdout.write("File size: {}\n".format(file_size))
        for k, v in sorted(num_file.items()):
            sys.stdout.write("{}: {}\n".format(k, v))
        """Reset counter"""
        ct = 0

"""Final signal handler to print when the script ends"""
signal_handler(None, None)

