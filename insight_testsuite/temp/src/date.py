import re
import math
from collections import defaultdict
import heapq
import sys

#reading the files from run.sh
infile = sys.argv[1]
inp= open(infile,"r")
ofile = sys.argv[2]
out= open(ofile,"w")
#intialisating the values
mdict=defaultdict(list)
dkey=""
dm={}
did={}
#calculating the running median
def runningMedian(vals):
    maxh = []
    minh = []
    median = 0.0
    for val in vals:
    # Initialize the data-structure and insert/push the 1st streaming value
     if not maxh and not minh:
        heapq.heappush(maxh,-val)
        #if len(vals) == 1:
         #   return -maxh[0]
     elif maxh:
        # Insert/push the other streaming values
         if val >= -maxh[0]:
            heapq.heappush(minh,val)
         else:
            heapq.heappush(maxh,-val)
        # Calculate the median
         if len(maxh)==len(minh):
            median = float(-maxh[0]+minh[0])/2
         elif len(maxh)==len(minh)+1:
            median =  float(-maxh[0])
         elif len(minh)==len(maxh)+1:
            median =  float(minh[0])

        # If min-heap and max-heap grow unbalanced we rebalance them by
        # removing/popping one element from a heap and inserting/pushing
        # it into the other heap, then we calculate the median
         elif len(minh)==len(maxh)+2:
            heapq.heappush(maxh,-heapq.heappop(minh))
            median = float((-maxh[0]+minh[0])/2)
         elif len(maxh)==len(minh)+2:
            heapq.heappush(minh,-heapq.heappop(maxh))
            median = float((-maxh[0]+minh[0])/2)
    return median
for line in inp:
   #splitting the words in the line
   word = line.split('|')
   #extracting the date value 
   dkey= int(word[13])
   idkey= word[0]
   #checking if the other_id is empty or not 
   if word[15]=='':
       #dictionary to store contributions received by recipient on that date 
        mdict[dkey].append(int(word[14]))
       #calling median function
        median=runningMedian(mdict[dkey])
       #dictionary to store the median value
        dm[dkey]= [idkey,math.ceil(median)]
       #dictionary to store recipeint of the contribution CMTE_ID
        sorted_values=sorted(dm,key=lambda k: (dm[k],k))
#sorting the dictionary according the date  
for key  in sorted_values:
    if key in dm:
    #printing the data to output file
       out.write ("%s|%d|%d|%d|%d \n" % (dm[key][0],key,dm[key][1],len(mdict[key]),sum(mdict[key])))
    
