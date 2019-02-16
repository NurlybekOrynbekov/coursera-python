import os
import tempfile


class File:
    def __init__(self, path):
        self.path = path
        if not os.path.exists(self.path):
            f = open(self.path, 'w')
            f.close()
        with open(self.path) as f:
            self.lines = f.readlines()
        self.end = len(self.lines)
        self.current = 0

    def write(self, text):
        with open(self.path, 'w') as f:
            f.write(text)
        with open(self.path) as f:
            self.lines = f.readlines()
        self.end = len(self.lines)
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        
        result = self.lines[self.current]
        self.current += 1
        return result

    def __add__(self, obj):
        new_file_path = os.path.join(tempfile.gettempdir(), 'new_file')
        text = ''
        with open(self.path, 'r') as f:
            text = f.read()
        with open(obj.path, 'r') as f:
            text += f.read()
        with open(os.path.join(new_file_path), 'w') as f:
            f.write(text)
        
        return File(new_file_path)

    def __str__(self):
        return self.path