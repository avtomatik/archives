#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  5 20:39:33 2025

@author: alexandermikhailov
"""

from core.config import ARCHIVE_NAME, BASE_PATH
from core.funcs import push_files_to_zip_conditional

if __name__ == '__main__':
    file_path = BASE_PATH.joinpath(ARCHIVE_NAME)

    SEQUENCE = 'detailnon'

    push_files_to_zip_conditional(file_path, SEQUENCE)
