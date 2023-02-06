import re

def verify(regexp, yes, no):
    for i in yes:
        if not re.match(regexp, i, re.X):
            print(f'Not matched {i}!')
            return False
    for i in no:
        if re.match(regexp, i, re.X):
            print(f'Unexpected match {i}!')
            return False
    return True

if verify(r"""\+?\d\s*              # State code (maybe leaded by '+' or not)
        (\d{3}|                     # 3-digit city code
        (\(\d{3}\)))\s*             # OR (3-digit city code)
        \d{3}                       # First 3 digits
        (([\s]*\d{2}[\s]*\d{2})|    # [spaces]XX[spaces]XX
        ([-]?\d{2}[-]?\d{2}))$""",  # OR -XX-XX
       ['+7 499 456-45-78', '+74994564578', '7 (499) 456 45 78', '7 (499) 456-45-78'],          # Correct numbers
       ['+7 4994 56-45-78', '-74994564578', '7 (499 456 45 78', '7 (499) 456 45-78']):          # Incorrect numbers
    print('Passed!')
else:
    print('Error!')
