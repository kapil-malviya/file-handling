"""

# Writing data to the text file : 

=>> we can write character data to the text files by using following 2 methods : 

-  x.write(str)
-  f.writelines(list of lines)

"""

f = open('file03.txt','w')
f.write('dollar\n')
f.write('silver\n')
f.write('rupee\n')
f.write('gold\n')
f.write('billion\n')
f.close()

print('data written successfully to the file03.txt')