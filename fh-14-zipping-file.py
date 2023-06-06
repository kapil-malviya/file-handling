"""

Zipping and Unzipping Files :

It is very common requirement to zip and unzip files, main advantages are :
	- to improve memory utilization
	- we can reduce transport time
	- we can improve performance

To perform zip and unzip operations, Python contains one in-bulit module zip file
This module contains a class : ZipFile

To create Zip file:
	we have to create ZipFile class object with name of the zip file, mode and constant
	ZIP_DEFLATED. This constant represents we are creating zip file.

f = ZipFile("files.zip","w","ZIP_DEFLATED")

Once we create ZipFile object, we can add files by using write() method

f.write(filename)


"""

from zipfile import *
f = ZipFile('files1.zip', 'w', ZIP_DEFLATED)
f.write('file03.txt')
f.write('file04.txt')
f.write('file05.txt')
f.close()
print('files1.zip file has been created successfully...')