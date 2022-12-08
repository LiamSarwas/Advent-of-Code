import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent


sum_of_small_directories = 0


class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.files = []
        self.directories = {}
        self.parent = parent
        self.size = None

def print_file_system(node, depth=0):
    if node.size:
        print(" " * depth + node.name + f" {node.size}")
    else:
        print(" " * depth + node.name)

    depth += 1
    for file in node.files:
        print(" " * depth + file.name + f" {file.size}")
    for directory in node.directories.values():
        print_file_system(directory, depth)


def build_file_system(input_data):
    root = Directory("/", None)
    cwd = root
    for line in input_data:
        if line[0] == "$":
            command = line.split(" ")
            if command[1] == "cd" and command[2] == "..":
                cwd = cwd.parent
            elif command[1] == "cd" and command[2] == "/":
                cwd = root
            elif command[1] == "cd":
                cwd = cwd.directories[command[2]]
            elif command[1] == "ls":
                continue
        else:
            ls_res = line.split(" ")
            if ls_res[0] == "dir":
                cwd.directories[ls_res[1]] = Directory(ls_res[1], cwd)
            else:
                cwd.files.append(File(int(ls_res[0]), ls_res[1]))
    return root

def get_directory_size(node):
    dir_size = 0
    small_dir_sum = 0

    for file in node.files:
        dir_size += file.size

    for directory in node.directories.values():
        small_dir_size, sub_dir_size = get_directory_size(directory)
        dir_size += sub_dir_size
        small_dir_sum += small_dir_size

    node.size = dir_size
    if dir_size <= 100000:
        small_dir_sum += dir_size

    return small_dir_sum, dir_size


def part_one(input_data):
    root = build_file_system(input_data)
    return get_directory_size(root)


def find_dir_to_delete(node, space_needed):
    best_node_size = 0
    if node.size > space_needed:
        best_node_size = node.size
    for directory in node.directories.values():
        best_sub_dir_node_size = find_dir_to_delete(directory, space_needed)
        if best_sub_dir_node_size == 0:
            continue
        else:
            if best_sub_dir_node_size < best_node_size:
                best_node_size = best_sub_dir_node_size
    return best_node_size


def part_two(input_data):
    root = build_file_system(input_data)
    get_directory_size(root)
    space_needed = 30_000_000 - (70_000_000 - root.size)
    return find_dir_to_delete(root, space_needed)


if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day7.txt").read_text().strip().split('\n')
    # DATA = (FILE_DIR / "input" / "day7test.txt").read_text().strip().split('\n')
    print(part_one(DATA)[0])
    print(part_two(DATA))
