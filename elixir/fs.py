import os
import os.path

class FilesystemObject:
    def __init__(self, path):
        self.path = path
        self.full_name = os.path.basename(path)
        self.name = os.path.splitext(self.full_name)[0]

class File(FilesystemObject):
    def __init__(self, path):
        assert os.path.isfile(path), '"{}" must be a file'.format(path)
        super().__init__(path)

    def read(self):
        with open(self.path) as f:
            return f.read()

class Folder(FilesystemObject):
    def __init__(self, path):
        assert os.path.isdir(path), '"{}" must be a folder'.format(path)
        super().__init__(path)

    def get_files(self):
        files = []
        for f in os.listdir(self.path):
            path = os.path.join(self.path, f)
            if os.path.isfile(path):
                files.append(f)
        return files
