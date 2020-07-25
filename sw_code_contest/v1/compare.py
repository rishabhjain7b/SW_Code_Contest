###################################
# Date:         21 JUL'20    
# Author:       Rishabh Jain
# Description:  Compare two files
# Result:       Pass Percentage
###################################

#from __future__ import division
import sys

print ('##############################')
print (' Reading input file ')

# Input File
INPUT_FILE = sys.argv[1]
#'data_file2.csv'

print ('##############################')
print (' Reading Golden file ')

# Golden File
GOLDEN_FILE = 'data_file.csv'

# Calculate the number of lines in golden file
num_lines = float(sum(1 for line in open(GOLDEN_FILE)))

print ('##############################')
print (' Comparing the Results \n')

with open(INPUT_FILE, 'r') as file1:
    with open(GOLDEN_FILE, 'r') as file2:
        same = set(file1).intersection(file2)
        #print(''.join(same))

# Number of common lines
match_lines = float(len(same))

perc = (match_lines/num_lines)*100

print ('###### PASS PERCENTAGE: ######')
print '\t',perc,'%'

#same.discard('\n')
#
#with open('some_output_file.txt', 'w') as file_out:
#    for line in same:
#        file_out.write(line)
