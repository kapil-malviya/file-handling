"""
	With Statement : 

with statement can be used while opening a file. we can use this to group file
operation statements within a block.
the advantage of with statement is it will take care closing of file,after completing all
operations automatically even in the case of exceptions also, and we are not required to
close explicitly...,

"""


#  with open('__.txt','w') as _ :


with open("file05.txt","w") as f:         # in any mode we can use with => w/a/r/x 
	f.write("Action\n")
	f.write("Trust\n")
	f.write("of India\n")
	print("Is File Closed: ",f.closed)              # false
 
print("Is File Closed: ",f.closed)                  # True