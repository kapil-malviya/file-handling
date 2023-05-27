"""
# File Handeling : 

=>>  Opening a File =>> 

f = open(filename, mode)


=>>  Closing a File =>>

f.close()

"""

# code will run only once


f = open('file02.txt','x')     		# there should not be any existing file with the same name 
								    # compulsory it'll create new file
print('file name : ',f.name)
print('file mode : ',f.mode)
print('is file readable : ',f.readable())
print('is file writable : ',f.writable())
print('is file closed : ',f.closed)
print()
f.close()
print('is file closed : ',f.closed)


'''
file name :  file02.txt
file mode :  x
is file readable :  False
is file writable :  True
is file closed :  False

is file closed :  True


# if program run for second time : 

Traceback (most recent call last):
  File "D:\file handeling\filehandeling-02.py", line 17, in <module>
    f = open('file02.txt','x')
        ^^^^^^^^^^^^^^^^^^^^^^
FileExistsError: [Errno 17] File exists: 'file02.txt'

=>> for this there must not be existing file (of same name)

'''