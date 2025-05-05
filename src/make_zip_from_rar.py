#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:29:45 2020

@author: Alexander Mikhailov
"""

# Requires Python 3.11 and Higher

import re
import zipfile
from pathlib import Path

import rarfile

from core.config import BASE_PATH, PATH_DST
from core.funcs import get_file_names_match

rarfile.TRY_ENCODINGS = ['utf8', 'utf-16le']
rarfile.PATH_SEP = '/'

MATCHERS = ['reference-ru-mathematical-biology']
MAGIC_NUMBER = 8
BASE_PATH.chdir()

ARCHIVE_NAMES = sorted(get_file_names_match(MATCHERS))


for _, archive_name in enumerate(ARCHIVE_NAMES, start=1):
    print(f'<{archive_name:=^50}>')
    with rarfile.RarFile(BASE_PATH / archive_name) as archive_rar:
        for f in archive_rar.infolist():
            SUFFIX = '.pdf'
            if f.file_name.endswith(SUFFIX):
                print(f'{f.filename}: {f.file_size / 1024 ** 2:,.2f} MB')
                # =========================================================
                # Extract from Archive
                # =========================================================
                archive_rar.extract(f.file_name, path=PATH_DST)
                # =========================================================
                # Move Closer to Root
                # =========================================================
                (PATH_DST / f.file_name).replace(PATH_DST /
                                                 f.file_name[MAGIC_NUMBER:])
                # =========================================================
                # Delete Previous Folder
                # =========================================================
                (PATH_DST / f.file_name[:MAGIC_NUMBER]).rmdir()
                PATH_DST.chdir()  # Change Folder
                # =========================================================
                # Create New Archive
                # =========================================================
                with zipfile.ZipFile(f'reference-ru-mathematical-biology{_:02n}.zip', 'w') as archive_zip:
                    new_file_name = re.sub(
                        ' ', '_', f.file_name[MAGIC_NUMBER:])
                    # =====================================================
                    # Rename Extracted File
                    # =====================================================
                    (PATH_DST / f.file_name[MAGIC_NUMBER:]
                     ).rename(PATH_DST / new_file_name)
                    # =====================================================
                    # Write Extracted File to New Archive
                    # =====================================================
                    archive_zip.write(
                        new_file_name, compress_type=zipfile.ZIP_DEFLATED)
                    # =====================================================
                    # Delete Extracted File
                    # =====================================================
                    (PATH_DST / new_file_name).unlink()
                # =========================================================
                # Move New Archive
                # =========================================================
                (PATH_DST / f'reference-ru-mathematical-biology{_:02n}.zip').replace(
                    BASE_PATH / f'reference-ru-mathematical-biology{_:02n}.zip'
                )
                # =========================================================
                # Delete Archive
                # =========================================================
                (BASE_PATH / archive_name).chdir()
                print(f'{new_file_name}: Done')

archive_name = 'dataset_rus_trud.rar'
print(f'{archive_name:=^50}')
# =============================================================================
# Copy Archive
# =============================================================================
path_src = BASE_PATH / archive_name
path_dst = PATH_DST / archive_name
path_dst.write_bytes(path_src.read_bytes())
# =============================================================================
# Change Folder
# =============================================================================
PATH_DST.chdir()
# =============================================================================
# Create New Archive
# =============================================================================
with zipfile.ZipFile(Path(archive_name).with_suffix('.zip'), 'w') as archive_zip:
    with rarfile.RarFile(archive_name) as archive_rar:
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
            Path(f.file_name).unlink()
            print(f'{f.file_name}: Done')

# Move archive back
(PATH_DST / archive_name).replace(BASE_PATH / archive_name)
