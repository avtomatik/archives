# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:29:45 2020

@author: Alexander Mikhailov
"""

import datetime
import os
import re
import shutil
import zipfile
from pathlib import Path
from zipfile import ZipFile

import pandas as pd
import rarfile
from rarfile import RarFile
from win32com.client.dynamic import Dispatch
from win32com.client.gencache import EnsureDispatch


def extract_rar_pack_zip():
    PATH = '/media/green-machine/KINGSTON'
    PATH_EXP = '/home/green-machine/Documents'
    ARCHIVE_NAME = 'dataset RUS trud.rar'
    _FILE_NAME = f'{os.path.splitext(ARCHIVE_NAME)[0]}.zip'

    print(f'<{ARCHIVE_NAME}>')
    shutil.copy(
        Path(PATH).joinpath(ARCHIVE_NAME),
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
                    Path(PATH).joinpath(_FILE_NAME)
                )
        # =============================================================================
        # Delete Archive
        # =============================================================================
        os.unlink(Path(PATH).joinpath(ARCHIVE_NAME))


def rar_extract_zip_pack_iterable():
    # =========================================================================
    # 'KINGSTON'
    # =========================================================================
    PATH = '/media/green-machine/KINGSTON'
    PATH_EXP = '/home/green-machine/Documents'
    NAME_PATTERN = 'Reference RU Mathematical Methods in Biology book_{:02n}.rar'
    FILE_NAMES = tuple(NAME_PATTERN.format(1 + _) for _ in range(31))

    rarfile.TRY_ENCODINGS = ('utf8', 'utf-16le')
    rarfile.PATH_SEP = '/'

    for _, archive_name in enumerate(FILE_NAMES, start=1):
        archive_name = f'ReferenceRUMathematicalBiology{_:02n}.zip'
        print(f'<{archive_name}>')
        with RarFile(Path(PATH).joinpath(archive_name)) as rar:
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
                        Path(PATH).joinpath(archive_name)
                    )
                    # =========================================================
                    # Delete Archive
                    # =========================================================
                    os.unlink(Path(PATH).joinpath(archive_name))
                    print(f'{_file_name}: Done')


FILE_NAMES = (
    'dataset USA BEA Release 2015-03-02 Section1ALL_Hist.xls',
    # 'dataset USA BEA Release 2015-03-02 Section2ALL_Hist.xls',
    # 'dataset USA BEA Release 2015-03-02 Section3ALL_Hist.xls',
    # 'dataset USA BEA Release 2015-03-02 Section4ALL_Hist.xls',
    # 'dataset USA BEA Release 2015-03-02 Section5ALL_Hist.xls',
    # 'dataset USA BEA Release 2015-03-02 Section6ALL_Hist.xls',
    'dataset USA BEA Release 2015-03-02 Section7ALL_Hist.xls',
)
FILE_NAMES = (
    'dataset USA BEA Release 2015-03-02 Section1all_xls.xls',
    # 'dataset USA BEA Release 2015-03-02 Section2all_xls.xls',
    # 'dataset USA BEA Release 2015-03-02 Section3all_xls.xls',
    # 'dataset USA BEA Release 2015-03-02 Section4all_xls.xls',
    # 'dataset USA BEA Release 2015-03-02 Section5all_xls.xls',
    # 'dataset USA BEA Release 2015-03-02 Section6all_xls.xls',
    'dataset USA BEA Release 2015-03-02 Section7all_xls.xls',
)
FILE_NAMES = (
    'dataset USA BEA Release 2013-11-26 Section1All_xls.xlsx',
    # 'dataset USA BEA Release 2013-11-26 Section2All_xls.xls',
    # 'dataset USA BEA Release 2013-11-26 Section3All_xls.xls',
    # 'dataset USA BEA Release 2013-11-26 Section4All_xls.xls',
    # 'dataset USA BEA Release 2013-11-26 Section5All_xls.xls',
    # 'dataset USA BEA Release 2013-11-26 Section6All_xls.xls',
    'dataset USA BEA Release 2013-11-26 Section7All_xls.xls',
)


# =============================================================================
# Separate Procedure
# =============================================================================
# =============================================================================
# Model R1-4F
# =============================================================================
PATH = 'C:\\Projects\\Temporary'
archive.extractall(path=PATH)


# =============================================================================
# Procedure: Compare All Files from Archive with the Same on Flash Drive
# =============================================================================
PATH = 'D:'
PATH_EXP = '/media/green-machine/KINGSTON'


with ZipFile(Path(PATH).joinpath('TextReview.zip')) as archive:
    for file_name in archive.namelist():
        if not file_name.endswith('.txt'):
            _file_name = re.sub('[ .]', '-', file_name)
            try:
                print(file_name)
                archive.extract(file_name, path=PATH_EXP)
                Application = EnsureDispatch('Word.Application')
                Application = Dispatch('Word.Application')
                Document = Application.Documents.Add()
                Application.CompareDocuments(
                    Application.Documents.Open(
                        Path(PATH_EXP).joinpath(file_name)),
                    Application.Documents.Open(Path(PATH).joinpath(file_name))
                )
                # =================================================================
                # prevent that word opens itself
                # =================================================================
                Application.ActiveDocument.ActiveWindow.View.Type = 3
                Application.ActiveDocument.SaveAs(
                    os.path.join(
                        PATH_EXP, 'compared{:02n}-{}.docx'.format(_, _file_name))
                )
                Application.Quit()
                del Application, Document
                os.unlink(Path(PATH_EXP).joinpath(file_name))
            except:
                pass

# =============================================================================
# Separate Procedure
# =============================================================================

for _, file_name in enumerate(FILE_NAMES, start=1):
    PATH = 'D:'
    os.chdir(PATH)
    with pd.ExcelFile(file_name) as xl_file:
        print('\t<New File>\t')
        df = pd.read_excel(
            xl_file, xl_file.sheet_names[1], header=None, nrows=6, usecols=0)
        df = df.T
        df['file_name'] = file_name
        df['source'] = xl_file.sheet_names[1]
        for sheet in xl_file.sheet_names[2:]:
            print(f'<{sheet}>')
            chunk = pd.read_excel(
                xl_file, sheet, header=None, nrows=6, usecols=0)
            chunk = chunk.T
            chunk['file_name'] = file_name
            chunk['source'] = sheet
            df = df.append(chunk, sort=False)

            PATH = '/media/green-machine/KINGSTON'
            os.chdir(PATH)
            df.to_excel(f'df{_:02}.xlsx', index=False)
            _ += 1

            df = pd.read_excel(f'df{1:02}.xlsx')
            for _ in range(1, 7):
                chunk = pd.read_excel(f'df{1+_:02}.xlsx')
                df = df.append(chunk, sort=False)
                df['date'] = df.iloc[:, 5]
                df.iloc[:, 8] = df.iloc[:, 8].astype(
                    str).str.replace('File created ', '')
                df.iloc[:, 8] = pd.to_datetime(df.iloc[:, 8])
                df.to_excel('df.xlsx', index=False)


archive_name = 'TextReview.zip'
file_names = []
with ZipFile(archive_name, 'w') as archive:
    for file_name in file_names:
        archive.write(file_name, compress_type=zipfile.ZIP_DEFLATED)
        os.unlink(file_name)

PATH = '/media/green-machine/KINGSTON'
os.chdir(PATH)
archive = ZipFile('Survey.zip')

for file_name in archive.namelist():
    if file_name.endswith('.xlsx'):
        print(file_name)
        with pd.ExcelFile(archive.open(file_name)) as xl_file:
            print('\t<New File>\t')
            df = pd.read_excel(
                xl_file, xl_file.sheet_names[1], header=None, nrows=6, usecols=0)
            df = df.T
            df['file_name'] = file_name
            df['source'] = xl_file.sheet_names[1]
            for sheet in xl_file.sheet_names[2:]:
                print(f'<{sheet}>')
                chunk = pd.read_excel(
                    xl_file, sheet, header=None, nrows=6, usecols=0)
                chunk = chunk.T
                chunk['file_name'] = file_name
                chunk['source'] = sheet
                df = df.append(chunk, sort=False)

            df.to_excel(f'df{_:02}.xlsx', index=False)
            _ += 1


df = pd.read_excel(f'df{1:02}.xlsx')
for _ in range(1, 8):
    chunk = pd.read_excel(f'df{1+_:02}.xlsx')
    df = df.append(chunk, sort=False)
df['date'] = df.iloc[:, 5]
df.iloc[:, 8] = df.iloc[:, 8].astype(
    str).str.replace('File created ', '')
df.iloc[:, 8] = pd.to_datetime(df.iloc[:, 8])
df.to_excel('df.xlsx', index=False)
PATH = 'D:'
os.chdir(PATH)

df_a = stockpile_usa_bea(
    'dataset USA BEA SFAT Release 2012-08-15 SectionAll_xls.zip',
    'Section3ALL_xls.xls',
    '303ES Ann',
    1947,
    2011,
    11
)
df_b = pd.read_csv('beanipaUnknownsfatk3n31gd1es000.zip', usecols=range(9, 11))
df_b.columns = df_b.columns.str.title()
df_b = df_b.set_index('Period')
df = pd.concat([df_a, df_b], axis=1, sort=False)
df['div'] = (df.iloc[:, 0] - df.iloc[:, 1]).div(df.iloc[:, 0])
print(df.iloc[:, 2].mean())
df.iloc[:, 2].plot(grid=True)
# signal processing

archive_name = 'dataset USA BEA FA2004 2017-08-23.zip'
with ZipFile(archive_name, 'w') as archive:
    for file_name in os.listPATH():
        if 'detailnon' in file_name.lower():
            archive.write(file_name, compress_type=zipfile.ZIP_DEFLATED)
            os.unlink(file_name)

df = pd.read_csv('dataset USA FRB gvp_sa.txt', sep='\s+',
                 header=None, skiprows=1, nrows=29)


df = pd.read_excel('Mitsubishi L200 Payments.xlsx')
df = df.append(
    [{
        'reference': '{:05n}'.format(0),
        'date': datetime.datetime(2018, 5, 10),
        'amount': 630000
    }],
    ignore_index=True
)
df.fillna('RUB', inplace=True)

df.sort_values(['date'], inplace=True)
for _ in range(len(df)):
    df.iloc[_, 0] = '{:05n}'.format(int(df.iloc[_, 0]))
df.to_excel('Mitsubishi L200 Payments.xlsx', index=False)

PATH = '/media/green-machine/KINGSTON'
os.chdir(PATH)
df = pd.read_excel('schedule_books.xlsx')
for _, column in df.items():
    column.values = column.str.title()
for _ in range(df.shape[1]):
    df.iloc[:, _] = df.iloc[:, _].str.title()
df.fillna('None', inplace=True)
df.to_excel('schedule_books.xlsx', index=False)
os.rename('Книга1.xlsx', 'translation.xlsx')
