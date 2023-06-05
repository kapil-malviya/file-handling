"""

Reading data from csv file : 

"""

import csv
f=open("emp.csv",'r')
r=csv.reader(f)       # returns csv reader object
data=list(r)
print(data, '\n')
for line in data:
	for word in line:
		print(word,"\t",end='')
	print()