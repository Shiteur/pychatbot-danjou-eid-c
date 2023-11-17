import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def nom_président(files_names):
    president = []
    for  i in range(len(files_names)):
        president.append(files_names[i][11:])
        while 49<=ord(president[i][-1])<=57:
            president[i]= president[i][:-1]
    return president
