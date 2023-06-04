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

from python.archives.src.main import main


def extract_rar_pack_zip():
    PATH_SRC = '/media/green-machine/KINGSTON'
    PATH_EXP = '/home/green-machine/Documents'
    ARCHIVE_NAME = 'dataset RUS trud.rar'
    _FILE_NAME = f'{os.path.splitext(ARCHIVE_NAME)[0]}.zip'

    print(f'<{ARCHIVE_NAME}>')
    shutil.copy(
        Path(PATH_SRC).joinpath(ARCHIVE_NAME),
        Path(PATH_EXP).joinpath(ARCHIVE_NAME)
    )
    # =========================================================================
    # Create New Archive
    # =========================================================================
    with ZipFile(Path(PATH_EXP).joinpath(_FILE_NAME), 'w') as archive:
        with RarFile(ARCHIVE_NAME) as rar:
            for f in rar.infolist():
                print('{}: {:,.2f} MB'.format(
                    f.filename, f.file_size / 1024 ** 2))
                # =============================================================
                # Extract from Archive
                # =============================================================
                rar.extract(f.filename)
                # =============================================================
                # Write Extracted File to New Archive
                # =============================================================
                archive.write(f.filename, compress_type=zipfile.ZIP_DEFLATED)
                # =============================================================
                # Delete Extracted File
                # =============================================================
                os.unlink(f.filename)
                print(f'{f.filename}: Done')
                shutil.move(
                    Path(PATH_EXP).joinpath(_FILE_NAME),
                    Path(PATH_SRC).joinpath(_FILE_NAME)
                )
        # =============================================================================
        # Delete Archive
        # =============================================================================
        os.unlink(Path(PATH_SRC).joinpath(ARCHIVE_NAME))


def rar_extract_zip_pack_iterable():
    # =========================================================================
    # 'KINGSTON'
    # =========================================================================
    PATH_SRC = '/media/green-machine/KINGSTON'
    PATH_EXP = '/home/green-machine/Documents'
    NAME_PATTERN = 'Reference RU Mathematical Methods in Biology book_{:02n}.rar'
    FILE_NAMES = tuple(NAME_PATTERN.format(1 + _) for _ in range(31))

    rarfile.TRY_ENCODINGS = ('utf8', 'utf-16le')
    rarfile.PATH_SEP = '/'

    for _, archive_name in enumerate(FILE_NAMES, start=1):
        archive_name = f'ReferenceRUMathematicalBiology{_:02n}.zip'
        print(f'<{archive_name}>')
        with RarFile(Path(PATH_SRC).joinpath(archive_name)) as rar:
            for f in rar.infolist():
                if f.filename.endswith('.pdf'):
                    print('{}: {:,.2f} MB'.format(
                        f.filename, f.file_size / 1024 ** 2))
                    # =========================================================
                    # Extract from Archive
                    # =========================================================
                    rar.extract(f.filename, path=PATH_EXP)
                    # =========================================================
                    # Move Closer to Root
                    # =========================================================
                    shutil.move(
                        Path(PATH_EXP).joinpath(f.filename),
                        Path(PATH_EXP).joinpath(f.filename[8:])
                    )
                    # =========================================================
                    # Delete Previous Folder
                    # =========================================================
                    os.rmdir(Path(PATH_EXP).joinpath(f.filename[:8]))
                    # =========================================================
                    # Create New Archive
                    # =========================================================
                    with ZipFile(Path(PATH_EXP, archive_name)).joinpath('w') as archive:
                        _file_name = re.sub(' ', '_', f.filename[8:])
                        # =====================================================
                        # Rename Extracted File
                        # =====================================================
                        os.rename(
                            Path(PATH_EXP).joinpath(f.filename[8:]),
                            Path(PATH_EXP).joinpath(_file_name)
                        )
                        # =====================================================
                        # Write Extracted File to New Archive
                        # =====================================================
                        archive.write(
                            _file_name, compress_type=zipfile.ZIP_DEFLATED)
                        # =====================================================
                        # Delete Extracted File
                        # =====================================================
                        os.unlink(Path(PATH_EXP).joinpath(_file_name))
                    # =========================================================
                    # Move New Archive
                    # =========================================================
                    shutil.move(
                        Path(PATH_EXP).joinpath(archive_name),
                        Path(PATH_SRC).joinpath(archive_name)
                    )
                    # =========================================================
                    # Delete Archive
                    # =========================================================
                    os.unlink(Path(PATH_SRC).joinpath(archive_name))
                    print(f'{_file_name}: Done')


def push_rename_files_to_zip(archive_name, file_names_in, file_names_ot):
    with ZipFile(f'{archive_name}.zip', 'w') as archive:
        for fn_in, fn_ut in zip(file_names_in, file_names_ot):
            os.rename(fn_in, fn_ut)
            archive.write(fn_ut, compress_type=zipfile.ZIP_DEFLATED)
            os.unlink(fn_ut)


def get_file_names(matchers: tuple[str]) -> list[str]:
    return [
        file_name for file_name in os.listdir() if all(match in file_name for match in matchers)
    ]
