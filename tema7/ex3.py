import os
import sys

def get_total_size(directory_path):
    total_size = 0
    try:
        for entry in os.scandir(directory_path):
            if entry.is_file():
                total_size += entry.stat().st_size
            elif entry.is_dir():
                total_size += get_total_size(entry.path)
        print(f"Total size of all files in '{directory_path}': {total_size} bytes")
    except FileNotFoundError:
        print(f"Error: The specified directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied while accessing files in '{directory_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        get_total_size(directory_path)
