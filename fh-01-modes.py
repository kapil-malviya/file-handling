"""
# File Handeling : 

=>> files are very common permanent storage areas to store our data


Types of Files =>> 

- text files : to store character data (abc.txt,..)
- binary files : to store binary data like images, video files, audio files etc...


## Opening a File =>> 


=>> before performing any operation (like read or write) on the file,first we 
	have to open that file, for this we have to use python's inbuilt function 
	open(), but at the time of open, we have to specify mode, which represents 
	the purpose of opening a file...


f = open(filename, mode)



=>> the allowed modes in python are :

r -> open an existing file for read operation, the file pointer is positioned at 
	 the begining of the file, if the specified file does not exist then we will 
	 get FileNotFoundError, this is default mode..

w -> open an existing file for write operation, if the file contains some data 
	 then it will be overridden, if the specified file is not already available 
	 then this mode will create that file.

a -> open an existing file for append operation, it won't override existing data,
	 if the specified file is not already available then this mode will create a 
	 new file.

r+ -> to read and write data into the file, the previous data in the file will 
	  not be deleted, the file pointer is placed at the begining of the file.

w+ -> to write and read data, it will override existing data.

a+ -> to append and read data from the file, it won't override existing data.

x  -> to open a file in exclusive creation mode for write operation, if the 
	  file already exists then we will get FileExistsError.


=>>> all these above modes are applicable for text files, if the above modes 
		suffixed with 'b' then these represents for binary files.

	eg => rb, wb, ab, r+b, w+b, a+b, xb


## Closing a File =>>

=>> after completing our operations on the file, it is highly recommended to close the file,
	for this we have to use close() function :

f.close()

----------------------------------

## Various properties of File Object =>> 

 ->> once we opened a file and we got file object, we can get various details related 
 	  to that file by using its properties : 

name -> Name of opened file
mode -> Mode in which the file is opened
closed -> Returns boolean value indicates that file is closed or not
readable() -> Retruns boolean value indicates that whether file is readable or not
writable() -> Returns boolean value indicates that whether file is writable or not


"""
'''
f = open('file01.txt','w') 		# no existing file required
print('file name : ',f.name)
print('file mode : ',f.mode)
print('is file readable : ',f.readable())
print('is file writable : ',f.writable())
print('is file closed : ',f.closed)
print()
f.close()
print('is file closed : ',f.closed)



file name :  file01.txt
file mode :  w
is file readable :  False
is file writable :  True
is file closed :  False

is file closed :  True

'''



f = open('file01.txt','r')     		# here compulsory this file must be there, if it's not present then : FileNotFoundError 
print('file name : ',f.name)
print('file mode : ',f.mode)
print('is file readable : ',f.readable())
print('is file writable : ',f.writable())
print('is file closed : ',f.closed)
print()
f.close()
print('is file closed : ',f.closed)


'''
file name :  file01.txt
file mode :  r
is file readable :  True
is file writable :  False
is file closed :  False

is file closed :  True

'''