import os
import sys
import collections


def find_file_names(file_path):
    file_names = []
    for root, _, files in os.walk(file_path):
        file_names.extend(list(map(lambda name_of_file: (
            name_of_file,
            os.path.getsize(root + '/' + name_of_file)), files))
                          )
    return file_names


def find_dublicates(file_names):
    counter = collections.Counter(file_names)
    dublicates = set(file[0] for file in counter if counter[file] > 1)
    return dublicates


if __name__ == '__main__':
    file_path = sys.argv[1]
    file_names = find_file_names(file_path)
    dublicates = find_dublicates(file_names)
    if len(dublicates) > 0:
        print('Количество дубликатов:', len(dublicates))
        print(*(file_name for file_name in dublicates), sep='\n')
    else:
        print('Дубликатов нет')
