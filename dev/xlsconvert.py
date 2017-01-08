#!/usr/bin/python

import xlrd
import csv
import sys

def csv_from_excel(input):

    wb = xlrd.open_workbook(input)
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open('samples/not_in_imdb.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        imdb_nr = (str(sh.cell_value(rownum,sh.ncols-1)))
        if (len(imdb_nr) < 1):
            wr.writerow(sh.row_values(rownum))
    your_csv_file.close()

input_path = sys.argv[1]
print ('Filmtipset file:', str(input_path))
csv_from_excel(input_path)
print ('done')
