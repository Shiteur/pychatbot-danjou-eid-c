# pychatbot-danjou-eid-d,Rayan EID et Thomas DANJOU,script contenant les fonctonnalités demandé à développer.
from fonctions_de_bases import *
from fonction_methodeTFIDF import *
#Cette fonction retourne la liste des mots du dossier cleaned ayant un TF-IDF=0.Il n'y a pas besoin de varible pour cette fonction.
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
#Cette fonction retourne la list de mots qui ont le TF-IDF le plus élévée dans le dossier cleaned. Il n'y a donc pas besoin de mettre une variable pour appeler cette fonction.
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
#Retourne la list des mots les plus répété par le président Chirac en enlevant les mots nom impartant. Il n'y a pas besoin de mettre de variable en entré.
def mot_plus_repeter_par_chirac():
    TF_score = {}
    mot_plus_dit= []
    files = list_of_files("cleaned", "txt")
    for i in range(0,2):                            #calcule le nombre de fois que chriac à prononcé un mot
        with open("cleaned/"+files[i], "r", encoding="utf-8") as f1:
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
#Cette fonction renvoie le nom du ou des présidents qui ont le plus parler de la Nation. C'est pour cela qu'il n'y apas de varable en entré.
def nation():
    president = list_of_files("cleaned", "txt")
    president = nom_president(president)
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
    president=retourne_nom_president(president)
    print(f"Le nom des présidents qui ont le parler de la nation sont {president} et celui qui en à le plus parler est {nom}.")
#retourne de nom du premier président qui à parler de l'écologie et/ou du réchauffement climatique. Il n'y a donc pas de variable d'entré.
def ecologie():
    president_nom=["Giscard dEstaing","Mitterrand","Chirac","Hollande","Sarkozy","Macron"]
    president = list_of_files("cleaned", "txt")
    president = nom_president(president)
    tf_idf = TF_IDF("cleaned")
    n=0
    i=0
    while i <len(tf_idf[0]) and tf_idf[0][i]!="écologique":
        i+=1
    n=i
    nom=len(president_nom)
    for i in range(len(tf_idf[1][n])):
        if tf_idf[1][n][i]!=0.0:
            for j in range(len(president_nom)):
                if president[i]== president_nom[j] and j<nom:
                    nom=j
    print(f"Le premier président qui a parlé de l'écologie est {president_nom[nom]}.")
#Cette fonction renvoie les mots évoquées par tous les présidents et qui ne sont pas non important.Elle n'a pas besoin de variable d'entré pour cette raison.
def mots_evoques():
    mots_non_important = mot_pas_important()
    files = list_of_files("cleaned", "txt")
    temp_mot_1 = []
    temp_mot_double_discourt = []
    for i in range(len(files)):
        temp_mot_2 = []
        with open("cleaned"+"/"+files[i], "r", encoding="utf-8") as f1: #Dresse la liste des mots dans chaque document un par un.
            line= f1.readline()
            line=line[:-1]
            while line !="":
                line = line.split(' ')
                for mot in line :
                    if mot not in temp_mot_2:
                        if mot not in mots_non_important:
                            temp_mot_2.append(mot)
                line = f1.readline()
                line=line[:-1]
        if files[i][-5]=="1": #regarde si le document sur lequel on travail est le premier discourt d'un président qui en à fait plusieurs.
            temp_mot_double_discourt = temp_mot_2
        elif i == 6:            #regarde si le document est le deuxième discourt de Mitterrand.
            for mot in temp_mot_1 :
                if not(mot in temp_mot_2 or mot in temp_mot_double_discourt):
                    temp_mot_1.remove(mot)
        elif files[i][-5]!="2": #regarde si le document est celui d'un présidents qui n'a pas parler plusieurs fois.
            for mot in temp_mot_1 :
                if not(mot in temp_mot_2):
                    temp_mot_1.remove(mot)
        else:
            for mot in temp_mot_double_discourt:
                if not(mot in temp_mot_2):
                    temp_mot_2.append(mot)
            temp_mot_1 = temp_mot_2
    print(temp_mot_1)
