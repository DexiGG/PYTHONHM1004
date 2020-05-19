import os, sys

tree = os.walk('test')
print(tree)
for i in os.walk('test'):
    print(i)
folder = []
for i in os.walk('test'):
    folder.append(i)
    print(i)
for address, dirs, files in folder:
    for file in files:
        print(address + '/' + file)
for i in folder:
    for j in i[2]:
        print(i[0] + '/' + j)

# 2
path = "test"
dirs = os.listdir(path)
for file in dirs:
    print(file)
