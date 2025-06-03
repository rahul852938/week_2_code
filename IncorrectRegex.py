import re
import sys

lines = sys.stdin.read().splitlines()
t = int(lines[0])
patterns = lines[1:]

for patternData in patterns:
    try:
        re.compile(patternData)
        print(True)
    except re.error:
        print(False)
