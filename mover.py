import os
import shutil


class Mover:
    src_path: str = None
    src_filelist: list = None
    target_path: str = None
    file_type: str = None

    def __init__(self, src: str = None, trgt: str = None, file_type: str = None):
        self.src_path = src
        self.target_path = trgt
        self.file_type = file_type
        if self.src_path and self.file_type:
            self.src_filelist = self._build_file_list(self.file_type)

    def _build_file_list(self, file_type: str):
        folder = os.scandir(self.src_path)
        file_list = [f for f in folder if f.is_file() and f.name.lower().endswith(file_type)]
        folder.close()

        return file_list

    def move(self):
        for file in self.src_filelist:
            print(f'Moving {file.name}')
            shutil.move(file.path, os.path.join(self.target_path, file.name))
