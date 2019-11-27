import os

ROOT_DIR = 'dev'

number_of_files = 0
for root, _, files in os.walk(ROOT_DIR):
    number_of_files += len(files)
    # for file in files: print(os.path.join(root, file))  # show files (for debug)
print("Number of files: ", number_of_files)
