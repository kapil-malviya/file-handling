"""
# Reading Character Data from text files

=>> read character data from text file by using the following read methods :

	read() : to read total data from the file
	read(n) : to read 'n' characters from the file
	readline() : to read only one line
	readlines() : to read all lines into a list

"""

f = open('file03.txt','r')

# data = f.read()
# data = f.read(10)   # will read only first 10 characters

data = f.readlines()   # will read all the lines
for line in data:
	print(line, end='')

"""
print(f.readline())             # read only one line
print(f.readline(),end='')
print(f.readline(),end='')
print(f.readline())
"""

# print(data)

f.close()