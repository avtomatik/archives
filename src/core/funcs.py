# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:29:45 2020

@author: Alexander Mikhailov
"""

import datetime
import os
import zipfile
from pathlib import PosixPath
from zipfile import ZipFile

from file_system.src.core.funcs import get_file_names_match


def push_files_to_zip(archive_name: str, file_names: tuple[str]) -> None:
    with ZipFile(archive_name, 'w') as archive:
        for file_name in file_names:
            archive.write(file_name, compress_type=zipfile.ZIP_DEFLATED)
            os.unlink(file_name)


def push_files_to_zip_if_exists(archive_path, MATCHERS):
    if archive_path.exists():
        with ZipFile(archive_path) as archive:
            archive.extractall()

    push_files_to_zip(
        archive_name=archive_path,
        file_names=sorted(get_file_names_match(matchers=MATCHERS))
    )


def push_files_to_zip_something(archive_path, MATCHERS):
    with ZipFile(archive_path) as archive:
        file_names = set(archive.namelist()) | set(
            get_file_names_match(matchers=MATCHERS))
        archive.extractall()

        push_files_to_zip(
            archive_path,
            tuple(file_names)
        )

        archive_path = f'auto_insurance_{datetime.date.today()}'
        push_files_to_zip(
            archive_path,
            tuple(get_file_names_match(matchers=MATCHERS))
        )


def push_rename_files_to_zip(archive_name: str, mapping: dict[str, str]):
    with ZipFile(archive_name, 'w') as archive:
        for fn_in, fn_ut in mapping.items():
            os.rename(fn_in, fn_ut)
            archive.write(fn_ut, compress_type=zipfile.ZIP_DEFLATED)
            os.unlink(fn_ut)


def push_files_to_zip_unlink(archive_name: str, file_names: tuple[str], to_unlink: tuple[str]) -> None:
    with ZipFile(archive_name, 'w') as archive:
        for file_name in file_names:
            archive.write(file_name, compress_type=zipfile.ZIP_DEFLATED)

    for file_name in to_unlink:
        os.unlink(file_name)


def push_files_to_zip_conditional(file: PosixPath, sequence: str) -> None:
    with ZipFile(file, 'w') as archive:
        for file_name in os.listdir(file.parent):
            if sequence in file_name.lower():
                archive.write(file_name, compress_type=zipfile.ZIP_DEFLATED)
                os.unlink(file_name)
