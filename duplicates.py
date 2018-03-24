import os
import sys
from collections import defaultdict


def find_file_names_and_sizes(file_path):
    files_locations = defaultdict(list)
    for root, _, name_of_files in os.walk(file_path):
        for name_of_file in name_of_files:
            path_of_file = os.path.join(root, name_of_file)
            size_of_file = os.path.getsize(path_of_file)
            name_and_size_of_file = (name_of_file, size_of_file)
            files_locations[name_and_size_of_file].append(path_of_file)
    return files_locations


def find_duplicates(file_names_and_sizes_dict):
    duplicates = set(
        name_of_file for name_of_file in file_names_and_sizes_dict
        if len(file_names_and_sizes_dict[name_of_file]) > 1
    )
    return duplicates


if __name__ == '__main__':
    file_path = sys.argv[1]
    file_names_and_sizes_dict = find_file_names_and_sizes(file_path)
    duplicates = find_duplicates(file_names_and_sizes_dict)
    if duplicates:
        print('Количество дубликатов:', len(duplicates))
        for file_name_and_size in duplicates:
            print(*file_names_and_sizes_dict[file_name_and_size])
    else:
        print('Дубликатов нет')
