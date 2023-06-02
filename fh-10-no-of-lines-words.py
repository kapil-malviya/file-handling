"""
# program to print the number of lines, words and characters present in the given file :


"""

import os, sys

fname = input('enter file name : ')
if os.path.isfile(fname) :
	print(fname, 'file exists...')
	f = open(fname, 'r')
else :
	print(fname, 'file does not exist..')
	sys.exit(0)

lcount = wcount = ccount = 0
for line in f :
	lcount = lcount + 1
	ccount = ccount + len(line)
	words = line.split()
	wcount = wcount + len(words)
print('the total no. of lines : ', lcount)
print('the total no. of words : ', wcount)
print('the total no. of characters : ', ccount)