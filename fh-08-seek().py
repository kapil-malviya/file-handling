"""
# seek()

==> we can use seek() method to move cursor (file pointer) to specified location, [can you please seek the 
	cursor to a particular location]

f.seek(offset, from where)

	offset represents the number of positions0 (going to jump) ..,

The allowed values for second attribute(from where) are :

	0 ---> from beginning of file(default value)
	1 ---> from current position
	2 ---> from end of the file
	
Note: python 2 supports all 3 values but python 3 supports only zero...

"""


data = 'All students are stupids'
f = open('file06.txt', 'w')
f.write(data)
with open('file06.txt', 'r+') as f:
	text = f.read()
	print(text)
	print('the current cursor position is : ', f.tell())
	f.seek(17)
	print('the current cursor position is : ', f.tell())
#	f.write('gems..!!')      # all characters of "stupids" replaced
	f.write('gems')          # ".... gemsids" -> only 4 characters replaced ;
	f.seek(0)
	text = f.read()
	print('the data after modification : ')
	print(text)