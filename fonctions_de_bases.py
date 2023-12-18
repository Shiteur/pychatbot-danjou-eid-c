# chatbot2000,Rayan EID et Thomas DANJOU,script contenant les fonctions fondamentales du projet. 
import os
#fonction qui retourne la liste de fichier contenant une certaine extention dans un dossier. Deux arguments à donner le dossier et l'extention les deux sous forme de chaîne de caractères.
#Les nom de variable sont explicite avec dossier pour signifié le nom du dossier et la varible extention pour l'extention.
def list_of_files(dossier, extention):
    nom_fichier = []
    for filename in os.listdir(dossier):
        if filename.endswith(extention):
            nom_fichier.append(filename)
    return nom_fichier
#fonction qui prend en paramètre une liste de nom de fichier et qui enlève le nom de de l'extention et tous les numéros qui suit de nom du fichier pour ensuite retourner la list modifié.
#c'est pour cela que le nom de varible est nom_fichier car il contient une list de nom fichier.
def nom_president(nom_fichier):
    president = []
    for  i in range(len(nom_fichier)):
        president.append(nom_fichier[i][11:-4]) # extrait la partie nom+numéro du nom de fichier
        while 49<=ord(president[i][-1])<=57:    # permet d'enlevé les chiffres à la fin des noms de présidents
            president[i]= president[i][:-1]
    return president
#fonction qui prend en argument une chaine de caracère et qui retourne le prenom assicié.
#D'ou le nom de variable nom qui fait directement référence au nom.
def prenom_president(nom):
    prenom={"Chirac":"Jacques","Giscard dEstaing":"Valéry","Mitterrand":"François","Sarkozy":"Nicolas","Macron":"Emmanuel","Hollande":"François"}
    for cle in prenom.keys():
        if nom == cle:
            return nom,prenom[nom]
    return "Aucun nom prénom est associé au nom saisie."
#Cette fonction prend en paramètre une list de nom de président d'où le nom de variable list_nom et elle supprime les doublons afin de retourner une liste avec un exemplaire de nom de président.
def retourne_nom_president(liste_nom):
    i=0
    while i < len(liste_nom):
        if liste_nom[i] in liste_nom[i+1:]:
            del(liste_nom[i])
        else:
            i+=1
    return liste_nom
#Cette fonction permet de prendre les  textes du dissier speeches les converties les Majuscules en minuscule et stocke le rendu dans le dossier cleaned.Pas de parmètre nécessaire.
#Cette fonction n'a donc pas besoin d'avoir de sortie.
def convertion_minuscule():
    list_text = list_of_files("speeches", "txt")#récuprère la liste des fichier .txt du répertoir speeches
    if "cleaned" not in os.listdir():           #recherche si le  répertoire cleaned n'existe pas dans le projet
        os.mkdir("cleaned")                     #création du répertoire cleaned dans ce cas
    for i in list_text:
        with open("speeches/"+i, "r", encoding="utf-8") as f1, open("cleaned/"+i, "w", encoding="utf-8") as f2:
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
#Cette fonction prend les fichiers du dossier cleaned et enlève la ponctuation pour qu'il ne reste que des suite de mots séparés par ddes espaces.
#Pas de paramètre pour cette fonction.Cette fonction n'a donc pas besoin d'avoir de sortie.        
def surpession_ponctuation():
    list_text = list_of_files("cleaned", "txt")#récuprère la liste des fichier .txt du répertoir cleaned
    for i in list_text:
        with open("cleaned/"+i, "r", encoding="utf-8") as f1, open("cleaned/new.txt", "w", encoding="utf-8") as f2: #écrit le contenu sans la ponctuation dans un autre fichier
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

