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

from python.archives.src.lib import get_file_names

rarfile.TRY_ENCODINGS = ('utf8', 'utf-16le',)
rarfile.PATH_SEP = '/'


PATH_SRC = '/media/green-machine/KINGSTON'
PATH_EXP = '/home/green-machine/Documents'


matchers = ('reference-ru-mathematical-biology',)
os.chdir(PATH_SRC)


file_names = sorted(get_file_names(matchers))


for _, file_name in enumerate(file_names):
    print(f'{file_name:=^50}')
    os.chdir(PATH_SRC)
    with rarfile.RarFile(file_name) as rf:
        for f in rf.infolist():
            if f.file_name.endswith('.pdf'):
                print('{}: {:,.2f} MB'.format(f.file_name, f.file_size/1024**2))
                # Extract from Archive
                rf.extract(f.file_name, path=PATH_EXP)
                shutil.move(Path(PATH_EXP).joinpath(f.file_name),
                            Path(PATH_EXP).joinpath(f.file_name[8:]))  # Move Closer to Root
                # Delete Previous Folder
                os.rmdir(Path(PATH_EXP).joinpath(f.file_name[:8]))
                os.chdir(PATH_EXP)  # Change Folder
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
                shutil.move(Path(PATH_EXP).joinpath(f'reference-ru-mathematical-biology{_:02n}.zip'),
                            Path(PATH_SRC).joinpath(f'reference-ru-mathematical-biology{_:02n}.zip'))  # Move New Archive
                os.chdir(Path(PATH_SRC).joinpath(file_name))  # Delete Archive
                print(f'{new_file_name}: Done')


archive_name = 'dataset-rus_trud'
print(f'{archive_name:=^50}')
shutil.copy(Path(PATH_SRC).joinpath(f'{archive_name}.rar'),
            Path(PATH_EXP).joinpath(f'{archive_name}.rar'))
os.chdir(PATH_EXP)  # Change Folder
with ZipFile(f'{archive_name}.zip', 'w') as archive:  # Create New Archive
    rf = rarfile.RarFile(f'{archive_name}.rar')
    for f in rf.infolist():
        print('{}: {:,.2f} MB'.format(f.file_name, f.file_size/1024**2))
        rf.extract(f.file_name)  # Extract from Archive
        # Write Extracted File to New Archive
        archive.write(f.file_name, compress_type=zipfile.ZIP_DEFLATED)
        os.unlink(f.file_name)  # Delete Extracted File
        print(f'{f.file_name}: Done')

shutil.move(Path(PATH_EXP).joinpath(f'{file_name}.zip'),
            Path(PATH_SRC).joinpath(f'{file_name}.zip'))
