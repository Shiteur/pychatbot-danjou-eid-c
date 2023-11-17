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
        while 49<=ord(president[i][-1])<=57: # permet d'enlevé les chiffres à la fin des noms de présidents
            president[i]= president[i][:-1]
    return president

def prénom_président(nom):
    prenom={"Chirac":"Jacques","Giscard dEstaing":"Valéry","Mitterrand":"François","Sarkozy":"Nicolas","Macron":"Emmanuel","Hollande":"François"}
    for cle, valeur in prenom.items():
        if nom ==cle:
            return prenom[nom]
