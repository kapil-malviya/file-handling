"""
To perform unzip operation :
	we have to create ZipFile object as follows
	
	f = ZipFile("files.zip","r",ZIP_STORED)

ZIP_STORED represents unzip operation, this is default value and hence we are not required to specify.
Once we created ZipFile object for unzip operation, we can get all file names present in
that zip file by using namelist() method.
names = f.namelist()

"""

from zipfile import *

f = ZipFile('files1.zip', 'r', ZIP_STORED)
names = f.namelist()
for name in names :
	print('file name : ', name)
	print('the content of this file is : ')
	f1 = open(name, 'r')
	print(f1.read())
	print()



"""
D:\file handeling>fh-15-unzipping-file.py
file name :  file03.txt
the content of this file is :
dollar
silver
rupee
gold
billion


file name :  file04.txt
the content of this file is :
sunny
bunny
vinny
chinny

file name :  file05.txt
the content of this file is :
Action
Trust
of India


"""