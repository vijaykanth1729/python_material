x = open('file1.txt')
print(x.tell()) # this will tells the current file pointer position..
x.seek(10)   # seek method is used for specifying the position from it will read the data..
print(x.tell())

print(x.read())
print(x.tell())
x.close()
