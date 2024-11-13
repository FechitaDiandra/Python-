import os

def rename_files(directory_path, prefix):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")
        
        files = os.listdir(directory_path)
        
        files = [f for f in files if os.path.isfile(os.path.join(directory_path, f))]
        
        files.sort(key=lambda x: int(os.path.splitext(x)[0][4:]) if x[0:4] == 'file' else x)
        
        for i, file_name in enumerate(files, start=1):
            new_name = f"{prefix}{i}.{os.path.splitext(file_name)[1][1:]}"
            
            old_path = os.path.join(directory_path, file_name)
            new_path = os.path.join(directory_path, new_name)
            
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {file_name} -> {new_name}")
            except PermissionError:
                print(f"Permission denied to rename file: {file_name}")
            except Exception as e:
                print(f"An error occurred when renaming {file_name}: {e}")
                
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

directory_path = "./test2"
rename_files(directory_path, "file")
