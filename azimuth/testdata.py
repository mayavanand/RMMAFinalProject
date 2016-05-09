import xlrd
import numpy as np

def get_test_data(data_file):
	workbook = xlrd.open_workbook(data_file)
	worksheet = workbook.sheet_by_name('Sheet1')
	print("Loading test data")
	Guide = np.array(worksheet.col_values(0), dtype='a30')
	Cut_Position = np.array(worksheet.col_values(1))
	Percent_Peptide = np.array(worksheet.col_values(2))
	return Guide, Cut_Position, Percent_Peptide

	