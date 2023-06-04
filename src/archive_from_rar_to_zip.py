# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:29:45 2020

@author: Alexander Mikhailov
"""
import os
import re
import shutil
import zipfile
from pathlib import Path
from zipfile import ZipFile

import rarfile

rarfile.TRY_ENCODINGS = ('utf8', 'utf-16le',)
rarfile.PATH_SEP = '/'


def push_rename_files_to_zip(archive_name, file_names_in, file_names_ot):
    with ZipFile(f'{archive_name}.zip', 'w') as archive:
        for f_name_in, f_name_ot in zip(file_names_in, file_names_ot):
            os.rename(f_name_in, f_name_ot)
            archive.write(f_name_ot, compress_type=zipfile.ZIP_DEFLATED)
            os.unlink(f_name_ot)


def get_file_names(matchers: tuple):
    return [file_name for file_name in os.listPATH() if all(match in file_name for match in matchers)]


PATH_SOURCE = '/media/green-machine/KINGSTON'
PATH_DESTINATION = '/home/green-machine/Documents'


matchers = ('reference-ru-mathematical-biology',)
os.chdir(PATH_SOURCE)


file_names = sorted(get_file_names(matchers))


for _, file_name in enumerate(file_names):
    print(f'{file_name:=^50}')
    os.chdir(PATH)
    with rarfile.RarFile(file_name) as rf:
        for f in rf.infolist():
            if f.file_name.endswith('.pdf'):
                print('{}: {:,.2f} MB'.format(f.file_name, f.file_size/1024**2))
                # Extract from Archive
                rf.extract(f.file_name, path=PATH_DESTINATION)
                shutil.move(Path(PATH_DESTINATION).joinpath(f.file_name),
                            Path(PATH_DESTINATION).joinpath(f.file_name[8:]))  # Move Closer to Root
                # Delete Previous Folder
                os.rmdir(Path(PATH_DESTINATION).joinpath(f.file_name[:8]))
                os.chdir(PATH_DESTINATION)  # Change Folder
                # Create New Archive
                with ZipFile(f'reference-ru-mathematical-biology{_:02n}.zip', 'w') as archive:
                    new_file_name = re.sub(' ', '_', f.file_name[8:])
                    # Rename Extracted File
                    os.rename(f.file_name[8:], new_file_name)
                    # Write Extracted File to New Archive
                    archive.write(
                        new_file_name, compress_type=zipfile.ZIP_DEFLATED)
                    # Delete Extracted File
                    os.unlink(new_file_name)
                shutil.move(Path(PATH_DESTINATION).joinpath(f'reference-ru-mathematical-biology{_:02n}.zip'),
                            Path(PATH).joinpath(f'reference-ru-mathematical-biology{_:02n}.zip'))  # Move New Archive
                os.chdir(Path(PATH).joinpath(file_name))  # Delete Archive
                print(f'{new_file_name}: Done')


file_name = 'dataset-rus_trud'
print(f'{file_name:=^50}')
shutil.copy(Path(PATH_SOURCE).joinpath(f'{file_name}.rar'),
            Path(PATH_DESTINATION).joinpath(f'{file_name}.rar'))
os.chdir(PATH_DESTINATION)  # Change Folder
with ZipFile(f'{archive_name}.zip', 'w') as archive:  # Create New Archive
    rf = rarfile.RarFile(f'{archive_name}.rar')
    for f in rf.infolist():
        print('{}: {:,.2f} MB'.format(f.file_name, f.file_size/1024**2))
        rf.extract(f.file_name)  # Extract from Archive
        # Write Extracted File to New Archive
        archive.write(f.file_name, compress_type=zipfile.ZIP_DEFLATED)
        os.unlink(f.file_name)  # Delete Extracted File
        print(f'{f.file_name}: Done')

shutil.move(Path(PATH_DESTINATION).joinpath(f'{file_name}.zip'),
            Path(PATH_SOURCE).joinpath(f'{file_name}.zip'))
