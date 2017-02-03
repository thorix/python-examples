#!/usr/bin/env python
"""Example tool for creating a good password"""
from __future__ import print_function
from builtins import input # pip install future --upgrade
from datetime import timedelta

import os
import string

# https://www.owasp.org/index.php/Password_special_characters
# https://docs.python.org/2/library/os.html#os.urandom
# http://www.howtogeek.com/howto/30184/10-ways-to-generate-a-random-password-from-the-command-line/
#   randpw(){ < /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-16};echo;}

def generate_temp_password(length):
    if not isinstance(length, int) or length < 8:
        raise ValueError("temp password must have positive length")

    chars = string.ascii_lowercase + string.ascii_uppercase + string.octdigits + string.punctuation + " "
    from os import urandom
    return "".join(chars[ord(c) % len(chars)] for c in urandom(length))


with open('/proc/uptime', 'r') as f:
    uptime_seconds = float(f.readline().split()[0])
    uptime_string = str(timedelta(seconds = uptime_seconds))

print("System uptime: " + uptime_string)
print("")

print(generate_temp_password(32))