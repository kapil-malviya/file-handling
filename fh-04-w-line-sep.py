"""
using list of lines

"""

f=open("file04.txt",'w')
list=["sunny\n","bunny\n","vinny\n","chinny"]
f.writelines(list)
print("List of lines written to the file successfully")
f.close() 

"""
while writing data by using write() methods, compulsory we have to provide line
seperator(\n),otherwise total data should be written to a single line

"""