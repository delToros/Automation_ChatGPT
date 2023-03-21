

import os
import shutil
import time

# Path of the download folder
path = r"C:\Users\Nikita\Downloads"

# Path of the old junk folder
old_junk_path = r"C:\Users\Nikita\Downloads\old junk"

# Get the current time
current_time = time.time()

# Check if the old junk folder exists, if not, create it
if not os.path.exists(old_junk_path):
    os.makedirs(old_junk_path)

# Iterate through the download folder
for file in os.listdir(path):
    file_path = os.path.join(path, file)
    # Check if the file is older than 30 days
    if os.stat(file_path).st_mtime < current_time - 30*24*60*60:
        # Move the file to the old junk folder
        shutil.move(file_path, old_junk_path)