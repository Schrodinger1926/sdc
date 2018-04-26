import os

def validate_file_path(path):
    assert(os.path.isfile(path)),"Enter a valid image file path relative or abosolute"
