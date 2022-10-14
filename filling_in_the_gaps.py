import os
import re
import shutil
from pathlib import Path

p = Path(os.getcwd())
file_regex = re.compile(r'(\w+)(\d){3}(.\w+)')

files_found = sorted([file for file in os.listdir(p) if file_regex.search(file)])

count_start = int(file_regex.search(files_found[0]).group(2))
number_prefix = count_start

file_length = len(files_found[0])

for file in os.listdir(p):
    mo = file_regex.search(file)
    if mo:
        # Check gap then rename file
        if int(mo.group(2)) != number_prefix:
            leading_zero = '0' * (file_length - len(mo.group(1)) - len(mo.group(2)) - len(mo.group(3)))
            
            # New file name
            new_file_name = mo.group(1) + leading_zero + str(number_prefix) + mo.group(3)
            print(new_file_name)
            shutil.move(p / file, p / new_file_name)
            
        number_prefix += 1
