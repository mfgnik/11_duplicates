import os
import sys


def find_file_names_and_sizes(file_path):
    file_names_and_sizes_dict = dict()
    for root, _, name_of_files in os.walk(file_path):
        file_names_and_sizes = list(map(lambda name_of_file: (
            name_of_file,
            os.path.getsize(os.path.join(root, name_of_file))), name_of_files)
                          )
        for name_and_size_of_file in file_names_and_sizes:
            name_of_file, _ = name_and_size_of_file
            path = os.path.join(root, name_of_file)
            if name_and_size_of_file in file_names_and_sizes_dict:
                file_names_and_sizes_dict[name_and_size_of_file].append(path)
            else:
                file_names_and_sizes_dict[name_and_size_of_file] = [path]
    return file_names_and_sizes_dict


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
