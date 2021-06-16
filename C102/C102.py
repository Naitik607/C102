#How to overwrite a folder if it already exists when creating it with makedirs this boring task i want automate

import os
import shutil

# Enter your path folder name here and the check the path
# Enter the correct path else it gives  an error
path = 'path_to_my_folder'
if not os.path.exists(path):
    os.makedirs(path)
else:
    shutil.rmtree(path)           # Removes all the subdirectories!
    os.makedirs(path)