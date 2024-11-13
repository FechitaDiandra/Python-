from rich import print
import os
import sys

def print_file_contents(path):
    try:
        print("Contents of:", path)
        with open(path, "r") as file:
            print(file.read())
    except PermissionError:
        print(f"[red]Permission denied to read file: {path}[/red]")
    except Exception as e:
        print(f"[red]Error reading file {path}: {e}[/red]")

def print_dir_files_content(path, extension):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"The directory '{path}' does not exist.")
        
        if not extension:
            raise ValueError("File extension cannot be empty.")
        
        files = os.listdir(path)

        for file_name in files:
            if os.path.splitext(file_name)[1][1:].lower() == extension.lower():
                print_file_contents(os.path.join(path, file_name))
        
    except FileNotFoundError as e:
        print(f"[red]Error: {e}[/red]")
    except ValueError as e:
        print(f"[red]Error: {e}[/red]")
    except Exception as e:
        print(f"[red]An error occurred: {e}[/red]")

print_dir_files_content("./test1", "txt")
