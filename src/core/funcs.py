#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:29:45 2020

@author: Alexander Mikhailov
"""

import datetime
import zipfile
from pathlib import Path

from core.funcs import get_file_names_match


def zip_and_delete_files(
    archive_path: Path,
    file_paths: tuple[Path, ...]
) -> None:
    with zipfile.ZipFile(archive_path, 'w') as archive:
        for file_path in file_paths:
            archive.write(
                file_path,
                arcname=file_path.name,
                compress_type=zipfile.ZIP_DEFLATED
            )
            file_path.unlink()


def zip_matched_files_over_existing(archive_path: Path, matchers) -> None:
    if archive_path.exists():
        with zipfile.ZipFile(archive_path) as archive:
            archive.extractall()

    matched_files = sorted(get_file_names_match(matchers=matchers))
    matched_paths = tuple(Path(f) for f in matched_files)
    zip_and_delete_files(archive_path, matched_paths)


def merge_and_zip_matched_files(archive_path: Path, matchers) -> None:
    with zipfile.ZipFile(archive_path) as archive:
        existing_files = set(archive.namelist())
        new_files = set(get_file_names_match(matchers=matchers))
        combined_files = existing_files | new_files
        archive.extractall()

        combined_paths = tuple(Path(f) for f in combined_files)
        zip_and_delete_files(archive_path, combined_paths)

        dated_archive = Path(f'auto_insurance_{datetime.date.today()}.zip')
        zip_and_delete_files(dated_archive, combined_paths)


def rename_and_zip_files(
    archive_path: Path,
    mapping: dict[Path, Path]
) -> None:
    with zipfile.ZipFile(archive_path, 'w') as archive:
        for src, dst in mapping.items():
            src.rename(dst)
            archive.write(
                dst,
                arcname=dst.name,
                compress_type=zipfile.ZIP_DEFLATED
            )
            dst.unlink()


def zip_files_and_unlink_selected(
    archive_path: Path,
    file_paths: tuple[Path, ...],
    paths_to_unlink: tuple[Path, ...]
) -> None:
    with zipfile.ZipFile(archive_path, 'w') as archive:
        for file_path in file_paths:
            archive.write(
                file_path,
                arcname=file_path.name,
                compress_type=zipfile.ZIP_DEFLATED
            )

    for file_path in paths_to_unlink:
        file_path.unlink()


def zip_files_matching_sequence(archive_path: Path, sequence: str) -> None:
    directory = archive_path.parent
    with zipfile.ZipFile(archive_path, 'w') as archive:
        for file_path in directory.iterdir():
            if sequence in file_path.name.lower() and file_path.is_file():
                archive.write(
                    file_path,
                    arcname=file_path.name,
                    compress_type=zipfile.ZIP_DEFLATED
                )
                file_path.unlink()
