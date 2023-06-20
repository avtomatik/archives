# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 09:18:21 2021

@author: Alexander Mikhailov
"""

# =============================================================================
# Create Password Protected Zip Archive
# =============================================================================
import os
import subprocess

if __name__ == '__main__':
    PATH = '/home/green-machine/Downloads'

    os.chdir(PATH)

    popenargs = [
        'zip',
        '-P',
        'topsecret',
        '-r',
        'compressed.zip',
        '/home/green-machine/Downloads/file.pdf'
    ]

    rc = subprocess.call(popenargs)
