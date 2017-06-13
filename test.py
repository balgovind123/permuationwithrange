from __future__ import print_function 
from itertools import permutations
list = "1258ahiklnorstAHIKLNORST!@#-_"
#open('permu.txt','rw')
for it in range(9,11):
  for i in permutations(list, it):
	  print ("".join(i))
	  with open('permu.txt','a') as f:
		f.write("".join(i)+'\n')
	  #print ("".join(i),file=f)
print ("Success")