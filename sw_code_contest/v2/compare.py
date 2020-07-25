###################################
# Date:         21 JUL'20    
# Author:       Rishabh Jain
# Description:  Compare two files
# Result:       Pass Percentage
###################################

import sys

print ('##############################')
print (' Reading input file ')

# Input File
INPUT_FILE = sys.argv[1]

print ('##############################')
print (' Reading Golden file ')

# Golden File
GOLDEN_FILE = 'golden_file.csv'

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

# Calculate percentage
perc = (match_lines/num_lines)*100

print ('###### PASS PERCENTAGE: ######')
print '\t',perc,'%'

