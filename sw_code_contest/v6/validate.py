#################################################
# Date:         27 JUL'20    
# Author:       Rishabh Jain
# Description:  Validate Structures of two files
# Result:       Pass Percentage/Mismatch & 
#               Run time of the design (Optional)                
#################################################

# DONE: Calculate execution runtime in us.
# DONE: Order change shows less %.
# DONE: If extra present in input file show less %.

# Precedence:
# 1. Incomplete File.
# 2. Extra Data in File.
# 3. Order Descrepancy in File.

import sys
import os
import time
import difflib
import subprocess
from collections import Counter

print ("##############################\n")
#print (" Reading Input File ")

# Input File
INPUT_FILE = sys.argv[1]

#print ("------------------------------")
#print (" Reading Golden File ")

# Golden File
GOLDEN_FILE = 'design.txt'

# Convert file into ordered list
# Discard new lines, tabs and whitespaces
def file_list(FILE):
    with open(FILE,'r') as f:
        fi_li = filter(None, map(lambda s: s.strip(), f.readlines()))
        fi_li = [v.translate(None, ' \t') for v in fi_li]
        return fi_li
        
# Difference between two list(Unordered)
# l1: golden, l2: input
def comp(li1, li2): 
    li_dif = list((li1 - li2).elements()) 
    return li_dif

# Check for similarity and order
# l1: golden, l2: input
# return value=
# 0 ==> Perfect match. 
# 1 ==> Extra Data in Input File. (Order, Don't Care) 
# 2 ==> Order discrepancy 
def check_same(l1, l2):
    if len(l1)==len(l2):
        if len(l1)==sum([1 for i, j in zip(l1, l2) if i==j]):
            return 0    
        else:
            return 2
    else:
        return 1

# Calculate match percentage
# l1: golden, l2: input
def percent(l1, l2):
    l1_size = float(len(l1))
    
    # Number of uncommon lines
    nomatch_size = float(len(comp(Counter(l1), Counter(l2))))

    # Number of common lines
    match_size = float(l1_size - nomatch_size)
    
    result = (match_size/l1_size)*100
    return int(result)

# Show differences between files (Missing or Unordered)
# l1: golden, l2: input
# return count for lessening the percentage
def diff(f1, f2, match):
    diff = difflib.unified_diff(f1, f2, fromfile='inp', tofile='gold', lineterm='', n=0)
    lines = list(diff)[2:]
    added = [line[1:] for line in lines if line[0] == '+']
    removed = [line[1:] for line in lines if line[0] == '-']
    count = 0
    
    print ("------------------------------")
    if match:
        identical = check_same(inp_file, gold_file)
        if identical == 2:
            print ("ERROR: Order Discrepancy ")
            print ("INFO: Positional Ambiguity at:")
            for line in added:
                if line in removed:
                    count = count + 1
                    print "-->", line
        elif identical == 1:
            print ("ERROR: Exceeded Data Limit ")
            print ("INFO: Extra Elements are:")
            for line in added:
                count = count + 1
                print "-->", line
        else:
            print ("!! PASSED SUCCESSFULLY !!")
    else:
        print ("ERROR: Incomplete File")
        print ("INFO: Missing Elements are:")
        for line in removed:
            print "-->", line
    
    return count

# Calculate execution time of the design
# If second argument is provided.
def exec_time(command):
    start_time = time.time()

    with open(os.devnull, "w") as fnull:
        result = subprocess.call(command, stdout = fnull, stderr = fnull)
    
    end_time = time.time()
    time_taken = end_time - start_time

    print ("\n---- RUNTIME TIME ELAPSED -----")
    print '\t ', round(time_taken * 1000 * 1000, 2),'us'

# Converting files 
inp_file = file_list(INPUT_FILE)
gold_file = file_list(GOLDEN_FILE)

#print ("------------------------------")
#print (" Comparing the Files... \n")
match_cent = percent(gold_file, inp_file)

# Check for full match
if match_cent == 100:
    file_match = True
else:
    file_match = False

# Show the differences
cent_diff = diff(gold_file, inp_file, file_match)

print ("------------------------------")

print ("\n------ PASS PERCENTAGE -------")
print '\t  ', match_cent - cent_diff,'%'

# Check for 2nd Argument and check runtime
if len(sys.argv) > 2:
    exe = sys.argv[2]
    exe = "./" + exe
    exec_time(exe)

print ("\n##############################")
