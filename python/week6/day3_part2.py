import os

# Check if a file exists
file_name = "day3_os.py"

if os.path.exists(file_name):
    print(f"{file_name} exists!")
else:
    print(f"{file_name} does not exist.")

path_name = "python3"

if os.path.isfile(path_name):
    print(f"{path_name} is a file.")
elif os.path.isdir(path_name):
    print(f"{path_name} is a directory.")
else:
    print(f"{path_name} does not exist.")

import os

old_name = "functions.py"
new_name = "my_functions.py"

os.rename(old_name, new_name)

print("File renamed successfully!")

old_name = "my_functions.py"
new_name = "functions.py"

os.rename(old_name, new_name)

print("Renamed back!")