# chatbot2000,Rayan EID et Thomas DANJOU,script permetant de calculer le TF,l'IDF et le TF-IDF d'un élément donné.
from fonctions_de_bases import *
import math
#Prend en paramètre une chaîne de caractères et retourne le nombre d'occurence de chaque mot dans cette chaine de caraèteres.
#La variable s'appele chaine car cela ce raproche du type de la variable qui est chaîne de caractères.
def TF(chaine):
    frequency = {}
    mot = chaine.split(" ")
    mot[-1] = mot[-1][:-1]
    for i in range(len(mot)):
        if mot[i] in frequency.keys():
            frequency[mot[i]] += 1
        else:
            frequency[mot[i]] = 1
    return frequency
#Prend en paramètre un dossier d'où le nom de variable.Le nom du dossier doit être une chaîne de caractères. La fonction va ensuite calculer d'IDF du dossier à l'aide de la fonction précédente.
def IDF(dossier):
    IDF_score = {}
    files = list_of_files(dossier, "txt")
    for i in range(len(files)):
        with open(dossier+"/"+files[i], "r", encoding="utf-8") as f1:
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
        IDF_score[keys] = math.log10(len(files)/IDF_score[keys]) 
    return IDF_score
#Prend en paramètre un dossier donc nous avons appelé la variable repertoire car cela se raproche du dossier et que la vriable présedente s'appele déjà dossier.
#Le nom du dossier doit être une chaîne de caractères. La fonction va ensuite calculer de TF-IDE du dossier grâce aux deux fonctions précédentes.
def TF_IDF(repertoire):
    list_mot=[]
    matrice=[]
    IDF_score = IDF(repertoire)
    files = list_of_files(repertoire, "txt")
    for key in IDF_score.keys():
        TF_score=[]
        for i in range(len(files)):
            val_TF=0
            with open(repertoire+"/"+files[i], "r", encoding="utf-8") as f1:
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