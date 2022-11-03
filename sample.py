import os

#extracting the current working directory
def current():
    cwd=os.getcwd()
    return cwd

#extracting the path of a particular file
def filePath(filename):
    path=os.path.abspath((filename))
    return path

print(current())
a="sample.txt"
print(filePath(a))