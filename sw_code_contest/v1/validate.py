#################################################
# Date:         21 JUL'20    
# Author:       Rishabh Jain
# Description:  Validate Structures of two files
# Result:       Pass Percentage
#################################################

#from __future__ import division
import sys
from collections import Counter

print ('##############################')
print (' Reading input file ')

# Input File
INPUT_FILE = sys.argv[1]

print ('##############################')
print (' Reading Golden file ')

# Golden File
GOLDEN_FILE = 'design.txt'

# Calculate the number of lines in golden file
golden_lines = float(sum(1 for line in open(GOLDEN_FILE)))

print ('##############################')
print (' Comparing the Results \n')

def comp(li1, li2): 
    li_dif = list((li2 - li1).elements()) 
    return li_dif

with open(INPUT_FILE,'r') as f:
    inp_file = Counter(f.readlines())
with open(GOLDEN_FILE,'r') as f:
    gold_file = Counter(f.readlines())

# Number of uncommon lines
unmatch_lines = float(len(comp(inp_file, gold_file)))

# Number of common lines
match_lines = golden_lines - unmatch_lines


#with open(INPUT_FILE) as f1:
#    f1_text = f1.read()
#with open(GOLDEN_FILE) as f2:
#    f2_text = f2.read()
## Find and print the diff:
#for line in difflib.unified_diff(f1_text, f2_text, fromfile='file1', tofile='file2', lineterm=''):
#    print line

#with open(INPUT_FILE, 'r') as file1:
#    with open(GOLDEN_FILE, 'r') as file2:
#        same = not (file1).intersection(file2)
#        print(same)

# Number of common lines
#match_lines = float(len(same))

perc = (match_lines/golden_lines)*100

print ('###### PASS PERCENTAGE: ######')
print '\t',int(perc),'%'

#same.discard('\n')
#
#with open('some_output_file.txt', 'w') as file_out:
#    for line in same:
#        file_out.write(line)
