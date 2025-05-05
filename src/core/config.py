#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  5 20:24:34 2025

@author: alexandermikhailov
"""

import datetime
from pathlib import Path

BASE_DIR = '/home/green-machine/Downloads'

DIR_DST = '/home/green-machine/Documents'

BASE_PATH = Path(BASE_DIR)

PATH_DST = Path(DIR_DST)

DATE = datetime.date(2017, 8, 23)

# =============================================================================
# https://apps.bea.gov/national/FA2004/Details/Index.htm
# =============================================================================
ARCHIVE_NAME = f'dataset_usa_bea-fa2004-release-{DATE}.zip'
