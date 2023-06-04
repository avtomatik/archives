import os
import zipfile
from zipfile import ZipFile


def main():
    # =============================================================================
    # Separate Procedure
    # =============================================================================
    # =============================================================================
    # Model R1-4F
    # =============================================================================
    PATH_EXP = 'C:\\Projects\\Temporary'
    archive.extractall(path=PATH_EXP)

    archive_name = 'TextReview.zip'
    file_names = []
    with ZipFile(archive_name, 'w') as archive:
        for file_name in file_names:
            archive.write(file_name, compress_type=zipfile.ZIP_DEFLATED)
            os.unlink(file_name)

    PATH_SRC = 'D:'
    os.chdir(PATH_SRC)
