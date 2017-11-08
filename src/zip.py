#import files
import re
import math
from collections import defaultdict
import heapq
import sys

#reading the files from run.sh
infile = sys.argv[1]
inp= open(infile,"r")
ofile=sys.argv[2]
out= open(ofile,"w")

#intializing the values
mdict=defaultdict(list)
zkey=""
median=0

#function to calculate the median
def runningMedian(vals):
    #intializing max and min heaps
    maxh = []
    minh = []
    for val in vals:
    # Initialize the data-structure and insert/push the 1st streaming value
     if not maxh and not minh:
        heapq.heappush(maxh,-val)
        if len(vals) == 1:
            return -maxh[0]
     elif maxh:
        # Insert/push the other streaming values
         if val >= -maxh[0]:
            heapq.heappush(minh,val)
         else:
            heapq.heappush(maxh,-val)
        # Calculate the median
         if len(maxh)==len(minh):
            return ( float(-maxh[0]+minh[0])/2)
         elif len(maxh)==len(minh)+1:
            return ( float(-maxh[0]))
         elif len(minh)==len(maxh)+1:
            return ( float(minh[0]))

        # If min-heap and max-heap grow unbalanced we rebalance them by
        # removing/popping one element from a heap and inserting/pushing
        # it into the other heap, then we calculate the median
         elif len(minh)==len(maxh)+2:
            heapq.heappush(maxh,-heapq.heappop(minh))
            return float(-maxh[0]+minh[0])/2
         elif len(maxh)==len(minh)+2:
            heapq.heappush(minh,-heapq.heappop(maxh))
            return float(-maxh[0]+minh[0])/2
#parsing the file
for line in inp:
   #splitting the lines  
   word = line.split('|')
   # storing zipcode as key to dictionary
   zkey= word[10][:5]
   #checking the other_id is empty or not 
   if word[15]=='':
      #creating a list of values and adding the contributions by recipent to list
        mdict[zkey].append(int(word[14])) 
     #calculating the total number of transactions received by recipient 
        total= sum(mdict[zkey]) 
     #calculating total amount of contributions received by recipient
        num=len(mdict[zkey]) 
     #calling the median function
        median=runningMedian(mdict[zkey]) 
      #writing the values to the output file
        out.write ("%s|%s|%d|%d|%d \n" % (word[0],zkey,math.ceil(median),num,total))

