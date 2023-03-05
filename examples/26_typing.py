# python3.10 26_typing.py runs OK
# python3.10 -m mypy 26_typing.py raises error

# unused imports
# isort will sort them
# flake8 will tell you these import are not needed
import re
import abc

def print_value(input: str):
    print(input)

print_value("string")
print_value(42)

