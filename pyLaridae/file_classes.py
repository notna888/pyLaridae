import os
from os import path
from urllib.parse import quote as html_escape


class FileObj:

    name = ''
    # file_size = 0.0  # TODO
    # file_type  # TODO - I'm thinking have images/documents/etc

    def __init__(self, name):
        self.name = name

    def html_name(self):
        return html_escape(self.name)

    def to_html(self):
        tag = f'<li><a href="#">{self.name}</a></li>'
        return tag

    def __repr__(self):
        return f'File: {self.name}'


class FolderObj(FileObj):

    def __init__(self, name):
        self.name = name
        self.internal_files = []

    def this_folder_li_tag(self):
        return f'<li><a href="/{self.html_name()}">{self.name}</a></li>'

    def to_html(self, depth=None):
        tag = self.this_folder_li_tag()
        ul_tag = '<ul>'
        internal_files = self.internal_files

        if(depth == None):
            ul_tag += full_depth(internal_files)
        elif(depth == 0):
            ul_tag += this_level_html(internal_files)
        else:
            new_depth = depth-1
            for internal_file in internal_files:
                ul_tag += internal_file.to_html(depth=new_depth)
        ul_tag += '</ul>'

        return tag+ul_tag

    def append_files(self, new_files):
        current_files = self.internal_files
        for file in new_files:
            current_files.append(file)
        self.internal_files = current_files

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
        folder_part = f'Folder: {self.name}'
        file_count = f'({len(self.internal_files)} files)'
        return folder_part + file_count


def full_depth(internal_files):
    ul_tag = ''
    for internal_file in internal_files:
        ul_tag += internal_file.to_html()
    return ul_tag


def this_level_html(internal_files):
    ul_tag = ''
    for internal_file in internal_files:
        if isinstance(internal_file, FolderObj):
            ul_tag += internal_file.this_folder_li_tag()
        else:
            ul_tag += internal_file.to_html()
    return ul_tag


def folder_navigation(folder_location):
    files = []
    files_and_dirs = os.listdir(folder_location)

    # This would print all the files and directories
    for file_object in files_and_dirs:
        if path.isdir(file_object):
            pass
            print(f'{file_object} is a directory')
        elif path.isfile(file_object):
            pass
            print(f'{file_object} is a file')
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

    Folder1 = FolderObj('Folder 1')
    Folder2 = FolderObj('Folder2')
    Folder3 = FolderObj('Folder3')
    Folder4 = FolderObj('Folder4')

    Folder1.append_files([File1, Folder2, Folder4])
    Folder2.append_files([Folder3, File2, File3])
    Folder3.append_files([File4, File5])
    Folder4.append_files([File6])

    return Folder1


if __name__ == '__main__':
    # real_folder_test()
    top_folder = fake_folder_test()
    print(top_folder.to_html())
