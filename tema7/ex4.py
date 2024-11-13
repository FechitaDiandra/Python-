import os
import sys
from collections import defaultdict

def count_extensions(directory_path):
    extension_counts = defaultdict(int)

    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The specified directory '{directory_path}' does not exist.")
        
        if not os.access(directory_path, os.R_OK):
            raise PermissionError(f"Permission denied to read the directory '{directory_path}'.")

        files = os.listdir(directory_path)
        
        if not files:
            print(f"The directory '{directory_path}' is empty.")
            return

        for file_name in files:
            if os.path.isfile(os.path.join(directory_path, file_name)):
                extension = os.path.splitext(file_name)[1].lower()  # Get the extension and convert it to lowercase
                extension_counts[extension] += 1

        if extension_counts:
            for ext, count in extension_counts.items():
                print(f"Extension '{ext}': {count} file(s)")
        else:
            print("No files with extensions found.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        count_extensions(directory_path)
