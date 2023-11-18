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
        president.append(files_names[i][11:-4]) # extrait la partie nom+numéro du nom de fichier
        while 49<=ord(president[i][-1])<=57: # permet d'enlevé les chiffres à la fin des noms de présidents
            president[i]= president[i][:-1]
    return president

def prénom_président(nom):
    prenom={"Chirac":"Jacques","Giscard dEstaing":"Valéry","Mitterrand":"François","Sarkozy":"Nicolas","Macron":"Emmanuel","Hollande":"François"}
    for cle in prenom.keys():
        if nom == cle:
            return nom,prenom[nom]

def retourne_nom_président(liste_nom):
    i=0
    while i < len(liste_nom):
        if liste_nom[i] in liste_nom[i+1:]:
            del(liste_nom[i])
        else:
            i+=1
    print(liste_nom)

def convertion_minuscule():
    list_text = list_of_files("speeches", "txt")#récuprère la liste des fichier .txt du répertoir speeches
    if "cleaned" not in os.listdir():           #recherche si le  répertoire cleaned n'existe pas dans le projet
        os.mkdir("cleaned")                     #création du répertoire cleaned dans ce cas
    for i in list_text:
        with open("speeches/"+i, "r") as f1, open("cleaned/"+i, "w") as f2:
            line= f1.readline()
            while line !="":
                line2=""
                for j in range(len(line)):
                    if 65<=ord(line[j])<=90:
                        line2=line2+chr(ord(line[j])+32)
                    else:
                        line2= line2+line[j]
                f2.write(line2)
                line = f1.readline()
            
def surpession_ponctuation():
    list_text = list_of_files("cleaned", "txt")#récuprère la liste des fichier .txt du répertoir cleaned
    for i in list_text:
        with open("cleaned/"+i, "r") as f1, open("cleaned/new.txt", "w") as f2: #écrit le contenu sans la ponctuation dans un autre fichier
            line = f1.readline()
            while line!="":
                line2=""
                if line[0]=="-":
                    debut = 2
                else:
                    debut = 0
                for j in range(debut, len(line)):
                    if line[j] in "'()[]:!;,?.-_"or line[j]=='"':
                        if line[j]=="'"or line[j]=="-" :
                            line2=line2+" "
                    else:
                        line2=line2+line[j]
                f2.write(line2)
                line = f1.readline()
        os.remove("cleaned/"+i)                         #supprime le fichier lut
        os.rename("cleaned/new.txt", "cleaned/"+i)      #renome le nouveau fichier avec le nom de l'ancien fichier
