from pathlib import Path
import os

class FilesStorage:
    def __init__ (self):
        self.root_directory = os.getcwd()

    def check_if_csv_exists(self, csv_file: str):
        if Path(csv_file).is_file():
            return True
        return False

    def check_if_folder_exists(self, folder: str):
        if Path(folder).is_dir():
            return True
        return False

    def new_file(self, file_to_create: str):
        with open(file_to_create, 'x') as new_file:
            new_file.close()
        return new_file

    def new_directory(self, path: str = os.getcwd(), directory_name: str = 'wallets'):
        path_to_create = os.path.join(path, directory_name)
        try:
            os.mkdir(path_to_create, 0o777)
            return True
        except OSError:
            print(f'Creation of directory {path_to_create} failed')
        return False

    def enter_directory(self, directory_to_enter: str):
        os.chdir(os.path.join(os.getcwd(), directory_to_enter))

    def return_to_root_directory(self):
        os.chdir(self.root_directory)

class WalletsStorage:
    def __init__(self):
        pass
