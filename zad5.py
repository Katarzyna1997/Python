## Build-in function
# import os

# ROOT_DIR = 'dev'
# for root, _, files in os.walk(ROOT_DIR):
#     for file in files: print(os.path.join(root, file))

## Own function
import os

def get_files(dir):
    items = os.listdir(dir)
    itmes_paths = [os.path.abspath(os.path.join(dir, item)) for item in items]
    for item in itmes_paths:
        if os.path.isdir(item):
            get_files(item)
        else:
            print(item)

get_files('dev')

