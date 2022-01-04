import os

def create_directory(dir_path):
    try:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    except OSError:
        print("Error: Failed to create the directory.")
