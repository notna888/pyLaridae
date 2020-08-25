import os
from os import path


class FileObj:

    name = ''
    location = ''
    # total_size = 0.0  # TODO

    def __init__(self, name, location='.'):
        self.name = name
        self.location = location

    def __repr__(self):
        return f'File: {self.location}/{self.name}'


class FolderObj(FileObj):

    internal_files = []

    def append_files(self, internal_files):
        current_files = self.internal_files
        current_files.extend(internal_files)

    def from_folder_location(folder_location):
        # TODO
        pass

    def generate_children(self):
        f_list = self.files
        dict_of_files = {}
        for f in f_list:
            if isinstance(f, FolderObj):
                name_of_folder = f.name
                children_of_this_folder = f.generate_children()

                dict_of_files[name_of_folder] = children_of_this_folder
            else:
                current_files = dict_of_files.get('.', [])
                dict_of_files['.'] = current_files.append(f.name)
        return dict_of_files

    def __repr__(self):
        return f'Folder: {self.location}/{self.name}'


def folder_navigation(folder_location):
    files = []
    files_and_dirs = os.listdir(folder_location)

    # This would print all the files and directories
    for file_object in files_and_dirs:
        if path.isdir(file_object):
            this_sub_directory = folder_navigation(file_object)
            folder = FolderObj(
                file_object,
                folder_location
            )
            folder.append_files(this_sub_directory)
            files.append(folder)
        elif path.isfile(file_object):
            this_file = FileObj(
                file_object,
                folder_location
            )
            files.append(this_file)
    return files


def folder_test():
    """This is a test function to test the creation of the folder object

    Returns:
        folder_obj: .

    """

    path_to_walk = "."
    folder_structure = folder_navigation(path_to_walk)
    print(folder_structure)


if __name__ == '__main__':
    folder_test()
