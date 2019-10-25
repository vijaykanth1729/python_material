def create_files(file1,file2):
    file1 = open(file1,'r+')
    file1.write("vijay a kanth")
    file2 = open(file2,'r+')
    file2.write('vi ijayv kanth')
    file1.close()
    file2.close()


def anagram(file1, file2):
    # word_list = [file1, file2]
    data1 = open(file1,'r')
    data1 = data1.read()
    data1 = data1.split(' ')

    data2 = open(file2,'r')
    data2 = data2.read()
    data2 = data2.split(' ')


    data =[]
    for i in data1:
        for j in data2:
            if (sorted(j)) ==  (sorted(i)):
                # print("anagram words are: ", i)
    #
                data.append(i)
            else:
                pass


    print("The anagram data from both files are:",data)
    new_data = []
    for key in data1:
        if (key not in data):
            new_data.append(key)

    print("this data is not a angram:", new_data)





create_files('file1.txt','file2.txt')
anagram('file1.txt', 'file2.txt')
# without_anagram('file1.txt','file2.txt')