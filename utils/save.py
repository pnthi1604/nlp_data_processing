import torch

def write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

__all__ = [
    "write_file",
]