import os
import math
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def nom_president(files_names):
    president = []
    for  i in range(len(files_names)):
        president.append(files_names[i][11:-4]) # extrait la partie nom+numéro du nom de fichier
        while 49<=ord(president[i][-1])<=57: # permet d'enlevé les chiffres à la fin des noms de présidents
            president[i]= president[i][:-1]
    return president

def prenom_president(nom):
    prenom={"Chirac":"Jacques","Giscard dEstaing":"Valéry","Mitterrand":"François","Sarkozy":"Nicolas","Macron":"Emmanuel","Hollande":"François"}
    for cle in prenom.keys():
        if nom == cle:
            return nom,prenom[nom]

def retourne_nom_president(liste_nom):
    i=0
    while i < len(liste_nom):
        if liste_nom[i] in liste_nom[i+1:]:
            del(liste_nom[i])
        else:
            i+=1
    return liste_nom

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

def TF(chaine):
    frequency = {}
    mot = chaine.split(" ")
    mot[-1] = mot[-1][:-1]
    for i in range(len(mot)):
        if mot[i] in frequency.keys():
            frequency[mot[i]] += 1/len(mot)
        else:
            frequency[mot[i]] = 1/len(mot)
    return frequency

def IDF(cleaned):
    IDF_score = {}
    files = list_of_files(cleaned, "txt")
    for i in range(len(files)):
        with open(cleaned+"/"+files[i], "r") as f1:
            line = f1.readline()
            mot=[]
            while line != "":               
                k = TF(line)
                for keys in k.keys():
                    if not(keys in IDF_score.keys()) :
                        IDF_score[keys] = 1
                        mot.append(keys)
                    else :
                        if not(keys in mot):
                            IDF_score[keys] += 1
                            mot.append(keys)
                line = f1.readline()        
    for keys in IDF_score.keys() :
        IDF_score[keys] = math.log(len(files)/IDF_score[keys]) 
    return IDF_score

def TF_IDF(repertoire):
    list_mot=[]
    matrice=[]
    IDF_score = IDF(repertoire)
    files = list_of_files(repertoire, "txt")
    for key in IDF_score.keys():
        TF_score=[]
        for i in range(len(files)):
            val_TF=0
            with open(repertoire+"/"+files[i], "r") as f1:
                line = f1.readline()
                while line != "":
                    k = TF(line)
                    if key in k.keys() :
                        val_TF += k[key]
                    line = f1.readline()
            TF_score.append(val_TF*IDF_score[key])
        matrice.append(TF_score)
        list_mot.append(key)
    return (list_mot, matrice)

def mot_pas_important():
    tf_idf = TF_IDF("cleaned")
    mot_non_impotant=[]
    for i in range(len(tf_idf[1])):
        s=0
        for j in range(len(tf_idf[1][i])):
            if tf_idf[1][i][j]==0.0:
                s+=1
        if s==len(tf_idf[1][i]):
            mot_non_impotant.append(tf_idf[0][i])
    return mot_non_impotant

def mot_important():
    tf_idf = TF_IDF("cleaned")
    mot_impotant=[]
    val=[]
    M=0
    for i in range(len(tf_idf[1])):
        s=0
        for j in range(len(tf_idf[1][i])):
            s+=tf_idf[1][i][j]
        if s>M:                             #recherche de maximum
           M=s
        val.append([s,i])
    for i in range(len(val)):
       if val[i][0]==M:
            mot_impotant.append(tf_idf[0][val[i][1]])
    return mot_impotant

def mot_plus_repeter_par_chirac():
    TF_score = {}
    mot_plus_dit= []
    files = list_of_files("cleaned", "txt")
    for i in range(0,2):                            #calcule le nombre de fois que chriac à prononcé un mot
        with open("cleaned/"+files[i], "r") as f1:
            line = f1.readline()
            while line != "":               
                k = TF(line)
                for keys in k.keys():
                    if keys in TF_score.keys() :
                        TF_score[keys] += k[keys]
                    else :
                        TF_score[keys] = k[keys]
                line = f1.readline() 
    M=0
    for key,values in TF_score.items() :            #recherche le maximum de fois que chirac à proncé un même mot
        if values>M:
            mot_plus_dit= []
            mot_plus_dit.append(key)
        else: 
            if values==M:
                mot_plus_dit.append(key)
    return mot_plus_dit

def nation():
    president = list_of_files("cleaned", "txt")
    president = nom_président(president)
    tf_idf = TF_IDF("cleaned")
    n=0
    i=0
    while i <len(tf_idf[0]) and tf_idf[0][i]!="nation":
        i+=1
    n=i
    m=1
    i=0
    while i<len(tf_idf[1][n]):
        if tf_idf[1][n][i]!=0.0:
            if m>tf_idf[1][n][i]:
                m=tf_idf[1][n][i]
                nom=president[i]
            i+=1
        else:
            del(president[i])
            del(tf_idf[1][n][i])
    president=retourne_nom_président(president)
    print(f"Le nom des présidents qui ont le parler de la nation sont {president} et celui qui en à le plus parler est {nom}.")

def ecologie():
    president_nom=["Giscard dEstaing","Mitterrand","Chirac","Hollande","Sarkozy","Macron"]
    president = list_of_files("cleaned", "txt")
    president = nom_président(president)
    tf_idf = TF_IDF("cleaned")
    n=0
    i=0
    while i <len(tf_idf[0]) and tf_idf[0][i]!="Ã©cologique":
        i+=1
    n=i
    nom=len(president_nom)
    for i in range(len(tf_idf[1][n])):
        if tf_idf[1][n][i]!=0.0:
            for j in range(len(president_nom)):
                if president[i]== president_nom[j] and j<nom:
                    nom=j
    print(f"Le premier président qui a parlé de l'écologie est {president_nom[nom]}.")

def mots_evoques():
    mots_non_important = mot_pas_important()
    files = list_of_files("cleaned", "txt")
    temp_mot_1 = []
    for i in range(len(files)):
        with open("cleaned"+"/"+files[i], "r") as f1:
            temp_mot_2 = []
            line = f1.readline().split(' ')
            for mot in line :
                if mot not in temp_mot_2:
                    if mot not in mots_non_important:
                        temp_mot_2.append(mot)
        if i != 0 :
            for mot in temp_mot_1 :
                if mot not in temp_mot_2 :
                    temp_mot_1.remove(mot)
        else:
            temp_mot_1 = temp_mot_2
    print(temp_mot_1)
       

    




            

            

 