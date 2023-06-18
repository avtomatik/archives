
import datetime
from pathlib import Path

from archives.src.lib import push_files_to_zip_conditional

PATH = '/media/green-machine/KINGSTON'
DATE = datetime.date(2017, 8, 23)
# =============================================================================
# https://apps.bea.gov/national/FA2004/Details/Index.htm
# =============================================================================
ARCHIVE_NAME = f'dataset_usa_bea-fa2004-release-{DATE}.zip'
FILE_NAME = Path(PATH).joinpath(ARCHIVE_NAME)
SEQUENCE = 'detailnon'

push_files_to_zip_conditional(FILE_NAME, SEQUENCE)
