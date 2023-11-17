from fonctions import *
# appelle la fonction list_of_files
directory = "../speeches"
files_names = list_of_files(directory, "txt")
print_list(files_names)