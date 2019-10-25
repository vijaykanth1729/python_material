x = open('file1.txt')

lines = x.readlines()   # readlines will read all the data , and stores in a list

#print(lines)

#print(type(lines))

for data in lines:
   # print(data, end="")   # removes the spaces between lines....

    print(data)

x.close()

