# Helper script for importing filmtipset grades to IMDB
# Takes rating and imdb movie title id and pads
# tt and additional zeroes so that the title can be found using
# https://greasyfork.org/sv/scripts/11617-imdb-list-helper
# 
# file) full path to a csv file containing rating and imdbid w/o tt and trailing zeros
#
# outfile) full path to file that should hold the result

file = '/Users/elias/Documents/imdbtest.csv'

file_handle = open(file, 'r')
file_content = file_handle.readlines()
file_handle.close()

entries = len(file_content)

outfile = '/Users/elias/Documents/imdbout.txt'


file_handle = open(outfile, 'w')
for line in file_content:

    a = line.split(',')
    grade = a[0]
    title_nr = a[1].strip()

    if (len(title_nr) < 7) :
        extra_z = 7 - len(title_nr)
        z = ''
        print(title_nr + ' : ' + str(extra_z))
        for i in range(extra_z):
           z += '0'
        file_handle.write(grade + ',' + 'tt' + z + title_nr + '\n')
    else:
        file_handle.write(grade + ',' + 'tt' + title_nr + '\n')

file_handle.close()

print('done')