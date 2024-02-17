import os
import shutil

# clear cache
cache_dir = "C:\Windows\Prefetch"

# clear temp files
temp_dir = "C:\Windows\Temp"

# clear more temp files
more_temp_dir = r"C:\Users\your_name\AppData\Local\Temp"

def clear_folder(directory_path):
    contents = os.listdir(directory_path)
    for item in contents:
        item_path = os.path.join(directory_path, item)
        try:
            if os.path.isfile(item_path):
                os.remove(item_path)
                
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                
            else:
                print(f"Skipped: {item_path} (Not a file or directory)")
        except Exception as e:
            print(f"Error deleting {item_path}: {e}")


if __name__ ==  "__main__":
    print(f'Cleaning {cache_dir}')
    clear_folder(cache_dir)

    print(f'Cleaning {more_temp_dir}')
    clear_folder(more_temp_dir)

    print(f'Cleaning {temp_dir}')
    clear_folder(temp_dir)
