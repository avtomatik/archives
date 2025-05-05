#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  5 20:39:33 2025

@author: alexandermikhailov
"""

from core.config import ARCHIVE_NAME, BASE_PATH
from core.funcs import zip_files_matching_sequence

if __name__ == '__main__':
    file_path = BASE_PATH.joinpath(ARCHIVE_NAME)

    SEQUENCE = 'detailnon'

    zip_files_matching_sequence(file_path, SEQUENCE)
