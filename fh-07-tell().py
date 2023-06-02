"""
	The seek() and tell() methods : 


# tell()

==> we can use tell() method to return current position of the cursor (file pointer) from beginning of the file, 
	[ can you plese telll current cursor position ], the position(index) of first character in files is zero just like string index...

"""



f = open('file05.txt', 'r')
print(f.tell())             #  =>> 0 (cursor is at 0th index)
print(f.read(4))            #  =>> reading four characters here
print(f.tell())             #  =>> 4 (cursor is at 4th index)
print(f.read(5))            #  =>> reading 5 characters again
print(f.tell())             #  =>> 10 (cursor is at 10th index)


