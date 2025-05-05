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


kwargs = {
    'archive_path': 'projectCensusComplex.zip',
    'file_paths': (
        'projectCensusComplex.py',
        'projectCensusComplexPlotKZF.pdf',
        'projectCensusComplexPlotKZF.xlsm',
        'projectCensusComplexPlotPearsonRTest.xlsm',
        'projectCensusComplexPlotSES.xlsm',
        'dataset_uscb.zip',
        'dataset_uscb.zip',
        'dataset_usa_cobb-douglas.zip',
        'dataset_douglas.zip',
    ),
    'paths_to_unlink': (
        'projectCensusComplex.py',
        'projectCensusComplexPlotKZF.pdf',
        'projectCensusComplexPlotKZF.xlsm',
        'projectCensusComplexPlotPearsonRTest.xlsm',
        'projectCensusComplexPlotSES.xlsm',
    ),
}


kwargs = {
    'archive_path': 'projectApproximation.zip',
    'file_paths': (
        'projectApproximation.py',
        'projectApproximationPlotApproxLinear.xlsm',
        'projectApproximationPlotApproxLogLinearA.xlsm',
        'projectApproximationPlotApproxLogLinearB.xlsm',
        'dataset_uscb.zip',
        'dataset_usa_0022_m1.txt',
        'dataset_usa_0025_p_r.txt',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1929_1969.zip',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1969_2012.zip',
        'dataset_usa_bea-sfat-release-2012-08-15-SectionAll_xls.zip',
        'dataset USA FRB_H6.csv',
        'mcConnellBrue.zip',
    ),
    'paths_to_unlink': (
        'projectApproximation.py',
        'projectApproximationPlotApproxLinear.xlsm',
        'projectApproximationPlotApproxLogLinearA.xlsm',
        'projectApproximationPlotApproxLogLinearB.xlsm',
    ),
}


kwargs = {
    'archive_path': 'projectCapital.zip',
    'file_paths': (
        'projectCapital.py',
        'projectCapitalInteractive.py',
        'projectCapital.pdf',
        'projectCapitalInteractiveCapitalAcquisitions.xlsm',
        'projectCapitalInteractiveCapitalRetirement.xlsm',
        'NipaDataA.txt',
        'dataset USA BLS cpiai.txt',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1929_1969.zip',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1969_2012.zip',
        'dataset USA FRB_G17_All_Annual 2013-06-23.csv',
        'dataset_usa_bea-sfat-release-2017-08-23-SectionAll_xls.zip',
    ),
    'paths_to_unlink': (
        'projectCapital.py',
        'projectCapitalInteractive.py',
        'projectCapital.pdf',
        'projectCapitalInteractiveCapitalAcquisitions.xlsm',
        'projectCapitalInteractiveCapitalRetirement.xlsm',
    ),
}


kwargs = {
    'archive_path': 'projectElasticity.zip',
    'file_paths': (
        'projectElasticity.py',
        'projectElasticityPlotElasticity.docx',
        'projectElasticityPlotElasticity.xlsm',
        'dataset_uscb.zip',
        'dataset_usa_0022_m1.txt',
        'dataset_usa_0025_p_r.txt',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1929_1969.zip',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1969_2012.zip',
        'dataset_usa_bea-sfat-release-2012-08-15-SectionAll_xls.zip',
        'dataset USA FRB_H6.csv',
    ),
    'paths_to_unlink': (
        'projectElasticity.py',
        'projectElasticityPlotElasticity.docx',
        'projectElasticityPlotElasticity.xlsm',
    ),
}


kwargs = {
    'archive_path': 'projectMSpline.zip',
    'file_paths': (
        'projectMSpline.py',
        'projectMSplineEA.xlsm',
        'projectMSplineEB.xlsm',
        'projectMSplineLA.xlsm',
        'projectMSplineLB.xlsm',
        'projectMSplineLLS.xlsm',
        'projectMSplineE.docx',
        'projectMSplineL.docx',
        'projectMSplineLLS.docx',
        'dataset_uscb.zip',
        'dataset_usa_cobb-douglas.zip',
        'dataset_douglas.zip',
    ),
    'paths_to_unlink': (
        'projectMSpline.py',
        'projectMSplineEA.xlsm',
        'projectMSplineEB.xlsm',
        'projectMSplineLA.xlsm',
        'projectMSplineLB.xlsm',
        'projectMSplineLLS.xlsm',
        'projectMSplineE.docx',
        'projectMSplineL.docx',
        'projectMSplineLLS.docx',
    ),
}


kwargs = {
    'archive_path': 'projectAntipov.zip',
    'file_paths': (
        'projectAntipov.py',
        'projectAntipov.docx',
        'projectAntipov.pdf',
        'dataset_uscb.zip',
        'dataset_usa_0022_m1.txt',
        'dataset_usa_0025_p_r.txt',
        'NipaDataA.txt',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1929_1969.zip',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1969_2012.zip',
        'dataset_usa_bea-release-2015-02-27-SectionAll_xls_1929_1969.zip',
        'dataset_usa_bea-release-2015-02-27-SectionAll_xls_1969_2015.zip',
        'dataset_usa_bea-sfat-release-2012-08-15-SectionAll_xls.zip',
        'dataset_usa_bea-sfat-release-2017-08-23-SectionAll_xls.zip',
        'dataset USA FRB_H6.csv',
    ),
    'paths_to_unlink': (
        'projectAntipov.py',
        'projectAntipov.docx',
        'projectAntipov.pdf',
    ),
}


kwargs = {
    'archive_path': 'projectPrices.zip',
    'file_paths': (
        'prices.py',
        'prices.pdf',
        'pricesDatasetBeaGdp.xlsm',
        'pricesDirect.xlsm',
        'pricesInverse.xlsm',
        'dataset USA BEA GDPDEF.xls',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1929_1969.zip',
        'dataset_usa_bea-release-2013-01-31-SectionAll_xls_1969_2012.zip',
        'dataset USA BLS cpiai.txt',
    ),
    'paths_to_unlink': (
        'prices.py',
        'prices.pdf',
        'pricesDatasetBeaGdp.xlsm',
        'pricesDirect.xlsm',
        'pricesInverse.xlsm',
    ),
}


kwargs = {
    'archive_path': 'projectAutocorrelation.zip',
    'file_paths': (
        'projectAutocorrelation.py',
        'projectAutocorrelation.xlsm',
        'projectAutocorrelationAlpha.docx',
        'projectAutocorrelationAlpha.pdf',
        'CHN_TUR_GDP.zip',
        'dataset USA FRB_G17_All_Annual 2013-06-23.csv',
        'datasetAutocorrelation.txt',
    ),
    'paths_to_unlink': (
        'projectAutocorrelation.py',
        'projectAutocorrelation.xlsm',
        'projectAutocorrelationAlpha.docx',
        'projectAutocorrelationAlpha.pdf',
        'CHN_TUR_GDP.zip',
        'datasetAutocorrelation.txt',
    ),
}


kwargs = {
    'archive_path': 'graduate_project.zip',
    'file_paths': (
        'Graduate Project fg_s.xlsx',
        'Graduate Project Financial Plan Revised.xlsx',
        'Graduate Project Financial Plan.xlsx',
        'Graduate Project Method Pyati Sil Portera.xlsx',
        'Graduate Project Sales Forecast.xlsx',
        'Graduate Project.xlsx',
        'Graduate Project-1.xlsx',
    ),
}


kwargs = {
    'file_paths': (
        'favppvpdf.pdf',
        'GraphDd1-12.zip',
        'TableDd1-12-csv.zip',
        'TableDd1-12-ris.zip',
        'TablePdf.jsp',
    )
}
