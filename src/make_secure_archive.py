#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 09:18:21 2021

@author: Alexander Mikhailov
"""

import subprocess

from core.config import BASE_PATH

if __name__ == '__main__':
    file_to_compress = BASE_PATH / 'file.pdf'
    output_zip = BASE_PATH / 'compressed.zip'

    popenargs = [
        'zip',
        '-P',
        'topsecret',
        '-r',
        str(output_zip),
        str(file_to_compress)
    ]

# =============================================================================
# Create Password Protected Zip Archive
# =============================================================================
    rc = subprocess.call(popenargs)
