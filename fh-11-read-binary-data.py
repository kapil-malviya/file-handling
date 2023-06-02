"""
Handling Binary Data : 

=>> it is very common requirement to read or write binary data like images, video files, audio
	files etc.

==> program to read image file and write it to a new image file : 


"""

f1 = open('rose.jpg', 'rb')
f2 = open('picture01.jpg', 'wb')
bytes = f1.read()
f2.write(bytes)
print('new image is available with the name : picture01.jpg')


# just same code for the video files (only extension will be changed) ;