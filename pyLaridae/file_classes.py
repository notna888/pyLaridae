import os
from os import path


class FileObj:

    name = ''
    location = ''
    # total_size = 0.0  # TODO

    def to_html(self):
        tag = f'<li><a href="#">{self.name}</a></li>'
        return tag

    def __init__(self, name, location='.'):
        self.name = name
        self.location = location

    def __repr__(self):
        return f'File: {self.location}/{self.name}'


class FolderObj(FileObj):

    internal_files = []

    def to_html(self):
        tag = f'<li><a href="#">{self.name}</a></li>'
        ul_tag = '<ul>'
        for i, internal_file in enumerate(self.internal_files):
            # print(i, ':', internal_file)
            # breakpoint()
            ul_tag += internal_file.to_html()
        ul_tag += '</ul>'

        return tag+ul_tag

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
        folder_part = f'Folder: {self.location}/{self.name}'
        file_count = f'({len(self.internal_files)} files)'
        return folder_part + file_count


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


def real_folder_test():
    """
        This is a test function to test the creation of the folder object
        based off of a directory
    """

    path_to_walk = "."
    folder_structure = folder_navigation(path_to_walk)
    print(folder_structure)
    # for f in folder_structure:
    #     print(f.to_html())

def fake_folder_test():
    File1 = FileObj('File1')
    File2 = FileObj('File2')
    File3 = FileObj('File3')
    File4 = FileObj('File4')
    File5 = FileObj('File5')
    File6 = FileObj('File6')

    Folder1 = FolderObj('Folder1')
    Folder2 = FolderObj('Folder2', 'Folder1')
    Folder3 = FolderObj('Folder3', 'Folder1/Folder2')
    Folder4 = FolderObj('Folder4')

    Folder1.append_files([File1, Folder2, Folder4])
    Folder2.append_files([Folder3, File2, File3])
    Folder3.append_files([File4, File5])
    Folder4.append_files([File6])

    print(Folder1.to_html())


if __name__ == '__main__':
    # real_folder_test()
    fake_folder_test()
