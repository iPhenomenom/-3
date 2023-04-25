import os
import shutil
import threading
from concurrent.futures import ThreadPoolExecutor


def sort_files_by_extension(src_path):
    for root, dirs, files in os.walk(src_path):
        with ThreadPoolExecutor(max_workers=len(dirs) + 5) as executor:
            for file in files:
                extension = os.path.splitext(file)[-1]
                dst_path = os.path.join(root, extension[1:])
                if not os.path.exists(dst_path):
                    os.makedirs(dst_path)
                executor.submit(shutil.move, os.path.join(root, file), os.path.join(dst_path, file))


if __name__ == '__main__':
    folder_path = input('Enter folder path: ')
    sort_files_by_extension(folder_path)