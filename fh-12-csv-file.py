"""

Handling csv(comma seperated values) files :
[creating & writing data in csv file]

==>> python provides csv module to handle csv files


"""

import csv

with open('emp.csv', 'w', newline='') as f :
	w = csv.writer(f)      # returns csv writer object pointing to f
	w.writerow(['ENo', 'EName', 'ESal', 'EAddr'])
	n = int(input('Enter no. of employees : '))
	for i in range(n) :
		eno = int(input('Enter Employee No. : '))
		ename = input('Enter Employee Name : ')
		esal = float(input('Enter Employee Salary : '))
		eaddr = input('Enter Employee Address : ')
		w.writerow([eno, ename, esal, eaddr])
print('Total employees data written to csv file successfully...')