import datetime


DATE = datetime.date(2015, 3, 2)
FILE_NAMES = tuple(
    map(
        lambda _: f'dataset USA BEA Release {DATE} Section{_}ALL_Hist.xls',
        range(1, 8)
    )
)


DATE = datetime.date(2015, 3, 2)
FILE_NAMES = tuple(
    map(
        lambda _: f'dataset USA BEA Release {DATE} Section{_}all_xls.xls',
        range(1, 8)
    )
)


DATE = datetime.date(2013, 11, 26)
FILE_NAMES = (
    f'dataset USA BEA Release {DATE} Section1All_xls.xlsx',
    f'dataset USA BEA Release {DATE} Section2All_xls.xls',
    f'dataset USA BEA Release {DATE} Section3All_xls.xls',
    f'dataset USA BEA Release {DATE} Section4All_xls.xls',
    f'dataset USA BEA Release {DATE} Section5All_xls.xls',
    f'dataset USA BEA Release {DATE} Section6All_xls.xls',
    f'dataset USA BEA Release {DATE} Section7All_xls.xls',
)
