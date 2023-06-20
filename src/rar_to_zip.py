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
from rarfile import RarFile

from file_system.src.core.funcs import get_file_names_match

rarfile.TRY_ENCODINGS = ['utf8', 'utf-16le']
rarfile.PATH_SEP = '/'


PATH_SRC = '/media/green-machine/KINGSTON'
PATH_EXP = '/home/green-machine/Documents'


MATCHERS = ['reference-ru-mathematical-biology']
os.chdir(PATH_SRC)


ARCHIVE_NAMES = sorted(get_file_names_match(MATCHERS))


for _, archive_name in enumerate(ARCHIVE_NAMES, start=1):
    print(f'<{archive_name:=^50}>')
    with RarFile(Path(PATH_SRC).joinpath(archive_name)) as archive_rar:
        for f in archive_rar.infolist():
            SUFFIX = '.pdf'
            if f.file_name.endswith(SUFFIX):
                print(f'{f.filename}: {f.file_size / 1024 ** 2:,.2f} MB')
                # =========================================================
                # Extract from Archive
                # =========================================================
                archive_rar.extract(f.file_name, path=PATH_EXP)
                # =========================================================
                # Move Closer to Root
                # =========================================================
                shutil.move(
                    Path(PATH_EXP).joinpath(f.file_name),
                    Path(PATH_EXP).joinpath(f.file_name[8:])
                )
                # =========================================================
                # Delete Previous Folder
                # =========================================================
                os.rmdir(Path(PATH_EXP).joinpath(f.file_name[:8]))
                os.chdir(PATH_EXP)  # Change Folder
                # =========================================================
                # Create New Archive
                # =========================================================
                with ZipFile(f'reference-ru-mathematical-biology{_:02n}.zip', 'w') as archive_zip:
                    new_file_name = re.sub(' ', '_', f.file_name[8:])
                    # =====================================================
                    # Rename Extracted File
                    # =====================================================
                    os.rename(f.file_name[8:], new_file_name)
                    # =====================================================
                    # Write Extracted File to New Archive
                    # =====================================================
                    archive_zip.write(
                        new_file_name, compress_type=zipfile.ZIP_DEFLATED)
                    # =====================================================
                    # Delete Extracted File
                    # =====================================================
                    os.unlink(new_file_name)
                # =========================================================
                # Move New Archive
                # =========================================================
                shutil.move(
                    Path(PATH_EXP).joinpath(
                        f'reference-ru-mathematical-biology{_:02n}.zip'),
                    Path(PATH_SRC).joinpath(
                        f'reference-ru-mathematical-biology{_:02n}.zip')
                )
                # =========================================================
                # Delete Archive
                # =========================================================
                os.chdir(Path(PATH_SRC).joinpath(archive_name))
                print(f'{new_file_name}: Done')


archive_name = 'dataset_rus_trud.rar'
print(f'{archive_name:=^50}')
shutil.copy2(
    Path(PATH_SRC).joinpath(archive_name),
    Path(PATH_EXP).joinpath(archive_name)
)
# =============================================================================
# Change Folder
# =============================================================================
os.chdir(PATH_EXP)
# =============================================================================
# Create New Archive
# =============================================================================
with ZipFile(f'{Path(archive_name).stem}.zip', 'w') as archive_zip:
    with RarFile(archive_name) as archive_rar:
        for f in archive_rar.infolist():
            print(f'{f.filename}: {f.file_size / 1024 ** 2:,.2f} MB')
            # =================================================================
            # Extract from Archive
            # =================================================================
            archive_rar.extract(f.file_name)
            # =================================================================
            # Write Extracted File to New Archive
            # =================================================================
            archive_zip.write(f.file_name, compress_type=zipfile.ZIP_DEFLATED)
            # =================================================================
            # Delete Extracted File
            # =================================================================
            os.unlink(f.file_name)
            print(f'{f.file_name}: Done')

shutil.move(
    Path(PATH_EXP).joinpath(archive_name),
    Path(PATH_SRC).joinpath(archive_name)
)
