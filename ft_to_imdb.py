#!/usr/bin/python

import xlrd
import csv
import sys

# Append tt and extra zeroes
def to_imdb_title(title_nr):

    #Strip decimal from excel number format
    title_nr = title_nr[:-2]

    if (len(title_nr) < 7) :
        extra_z = 7 - len(title_nr)
        z = ''
        print(title_nr + ' : ' + str(extra_z))
        for i in range(extra_z):
           z += '0'
        return 'tt' + z + title_nr + '\n'
    else:
        return 'tt' + title_nr + '\n'

# Just multiply by 2
def modify_grade(grade):
    double = str(grade*2)[:-2]
    return double

# Read excel make csv and txt
def csv_from_excel(input):

    wb = xlrd.open_workbook(input)
    sh = wb.sheet_by_name('Sheet1')
    no_imdb_csv_file = open('samples/not_in_imdb.csv', 'w')
    output_file = open('samples/ratings.txt', 'w')
    ni = csv.writer(no_imdb_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        imdb_nr = (str(sh.cell_value(rownum,sh.ncols-1)))
        if (len(imdb_nr) < 1):
            ni.writerow(sh.row_values(rownum))
        else:
            imdb_nr = to_imdb_title(str(sh.cell_value(rownum,sh.ncols-1)))
            grade = modify_grade(sh.cell_value(rownum,4))
            output_file.write(grade + "," + imdb_nr)
    no_imdb_csv_file.close()
    output_file.close()

# First argument is input file
input_path = sys.argv[1]
print ('Filmtipset file:', str(input_path))
csv_from_excel(input_path)
print ('done')
