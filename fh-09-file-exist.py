"""
how to check a particular file exists or not : 

==> we can use os library to get information about files in our computer, os module has path sub module, 
	which contains isFile() function to check whether a particular file exists or not...

os.path.isfile(file-name) 

[if file available then print its content also]

==>>> 



import os, sys

fname = input("Enter File Name : ")
if os.path.isfile(fname):
	print("File exists : ",fname)
	f = open(fname,"r")
else:
	print("File does not exist : ",fname)
	sys.exit(0)
print("The content of file is : ")
data = f.read() 
print(data)


or 

"""

import os 
fname = input('enter file name : ')
if os.path.isfile(fname):
	print(fname, 'file exists')
	f = open(fname, 'r')
	print('the content of the file is : ')
	text = f.read()
	print(text)
else : 
	print(fname, 'file does not exists...')