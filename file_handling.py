file = open('file_handling.txt')

#data = file.read()
#data = file.readline()
#data = file.readlines()
data = file.read(50)
print(data)

'''file2 = open('new.txt', 'w')
file2.write('New data')
file2.close()'''

file2 = open('new.txt', 'a+')
file2.write('Some more data')
file2.seek(10)
data = file2.read()
print(data)
file2.close()
