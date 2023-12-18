# chatbot2000,Rayan EID et Thomas DANJOU,script qui permet de générer une réponse à une question donné.
import math
from fonctions_de_bases import *
from fonction_methodeTFIDF import *
#prend en entré une chaîne de caractères. Nous lui avons donc donné un nom de variable explicite avec chaine.
#Cette fonction retourne une liste de mots sans ponctuation de la chaîne de caractères entré.
def Tokenisation_question(chaine):
    chaine2=""
    for j in range(len(chaine)):
        if 65<=ord(chaine[j])<=90:
            chaine2=chaine2+chr(ord(chaine[j])+32)
        elif chaine[j] in "'()[]:!;,?.-_" or chaine[j]=='"':
            if chaine[j]=="'"or chaine[j]=="-" :
                chaine2=chaine2+" "
        else:
            chaine2=chaine2+chaine[j]
    return chaine2.split(" ")
#Cette fonction prend en entré une list de mots et retourne la list de mots en commun avec le dossier cleaned.
#La variable intersection n'est pas très explicite comme entré mais comme en renvoie la même list cela est explicite en sortie c'est pour cela qu'on la choisi.
def intersection_corpus_question(intersection): 
    mot_L= TF_IDF("cleaned")[0]
    i=0
    while i<len(intersection):
        if intersection[i] not in  mot_L:       #recherche si i est dans les mots du corpus
            del(intersection[i])
        else:
            i+=1
    return intersection
#Cette fonction prend en entré une liste de mots préalabrement traité pour être forcément contenu dans la liste de mot du dossier cleaned.
#Elle retourne ensuite un tuple avec la liste des mots du dossier cleaned et la matrice associé représentant le vecteur TF-IDF de chauqe document plus celui de la list de mots entré.
#Cette varible est donc toute trouvé car elle doit contenir uniqument des mots présents dans les textes du dossier cleaned. 
def vecteur_TF_IDF(intersection):
    tf_idf = TF_IDF("cleaned")
    IDF_score=IDF("cleaned")
    mat_int=[]
    for i in range(len(tf_idf[1][0])): #fait une transposé de materice.
        L=[]
        for j in range(len(tf_idf[1])):
            L.append(tf_idf[1][j][i])
        mat_int.append(L)
    TF_question=[]
    i=0
    while i <len(intersection): #calcule le TF des mots de la question 
        tf=1
        j=i+1
        while j <len(intersection):
            if intersection[j]==intersection[i]:
                tf+=1
                del(intersection[j])
            j+=1
        TF_question.append(tf)
        i+=1
    L=[]
    for key, val in IDF_score.items(): #calcule du TF_IDF de la question
        inter=True
        j=0
        while j < len(intersection) and inter:
            if intersection[j]== key:
                L.append(TF_question[j]*val)
                inter=False
            j+=1
        if inter:                      
            L.append(0*val)
    mat_int.append(L)
    return tf_idf[0],mat_int
######début du calcule de similarité
#Cette fonction calcule le produit scalaire de deux vecteurs qui sont les listes de nombres. La sortie est donc un nombre unique.
#Les variables sont vecteur1 et vecteur2 car l'opération réalisé se fait généralement sur des vecteurs.
def produit_scalaire(vecteur1,vecteur2):#calcule le produits scalaire de deux vecteurs de longueur identique
    if len(vecteur1)==len(vecteur2):
        somme=0
        for i in range(len(vecteur1)):
            somme += vecteur1[i]*vecteur2[i]
        return somme
    else:
        return 0
#Cette fonction clacule le norme d'un vecteur qui est une liste de nombres. La variable d'entré est donc explicite car c'est le terme vecteur. La sortie est donc un nombre unique.
def norme_vecteur(vecteur):
    somme=0
    for i in range(len(vecteur)):
        somme+= vecteur[i]**2
    return math.sqrt(somme)
#Cette fonction calcule la similarité de deux vecteurs en utilisant les deux fonctions précédentes c'esrt pour cela que les noms de variable sont identiques. La sortie est donc un nombre unique.
def similarite(vecteur1,vecteur2): #calcule la similarité de deux vecteurs de longueur identique
    return produit_scalaire(vecteur1,vecteur2)/(norme_vecteur(vecteur1)*norme_vecteur(vecteur2))
######fin du calcule de similarité
#fonction à en entré trois variable: la list des nom de fichier, leur vecteur associé dans une matrice et le vecteur de la question.
#Cette fonction renvoie le mon du fichier qui possède la plus grande valeur de similarité. Le nom des variables sont donc explicite par rapport à leur rôle.
#mat_doc est la matrice contenant le veteur de chaque fichier de cleaned, vecteur_question est le vecteur question et list_noms est la list des nom de documents dans le dossier cleaned qui est égal au nom des fichiers dans le dossier speeches.
def document_pertinent(mat_doc,vecteur_question,list_noms):
    pertinent=similarite(mat_doc[0],vecteur_question)
    fichier=list_noms[0]
    for i in range(1,len(mat_doc)):
        if pertinent<similarite(mat_doc[i],vecteur_question):
            pertinent=similarite(mat_doc[i],vecteur_question)
            fichier=list_noms[i]
    return fichier
#Cette fonction retourne une réponse à une question que l'on entre en entré. L'entré est une chaîne de caractères tout comme la sorti de cette fonction.
#La variable question est très explicite car on attend en entré une question.
def generation_reponse(Question):                   #Génère une raponse à une chaine de carcatère
    files=list_of_files("cleaned", "txt")
    Question=vecteur_TF_IDF(intersection_corpus_question(Tokenisation_question(Question)))
    mat=Question[1][:-1]
    #début de la recherche du mot le plus important
    mot_important=Question[1][-1][0]
    indice=0
    for i in range(len(Question[1][-1])):
        if mot_important<Question[1][-1][i]:
            mot_important=Question[1][-1][i]
            indice=i
    mot_important=Question[0][indice]
    #fin de la recherche du mot le plus important de la question
    Question=Question[1][-1]
    text_important=document_pertinent(mat,Question,files)
    with open("cleaned/"+text_important, "r", encoding="utf-8")as f:
        fichier=f.readlines()
        i=0
        trouve=True
        
        while i<len(fichier) and trouve:
            if mot_important in fichier[i]:
                reponse=fichier[i]
                trouve=False
            i+=1
    if reponse!="...":
        with open("speeches/"+text_important, "r", encoding="utf-8")as f:
            fichier=f.readlines()
            reponse=fichier[i-1]
    return reponse
#Cette fonction prend deux chaînes de caractères en entré et retourne une seule chaîne de caractère en sortie.
#La première chaîne est celle de la question et la seconde est celle de la réponse déjà écrite les noms de variables sont donc significatif.
def affine_reponse(Question, Reponse):
    question_starter={"Comment": "Après analyse, ","Pourquoi": "Car, ","Peux-tu": "Oui, bien sûr!"}
    reponse_starter=""
    Question=Question.split(" ")
    for key,val in question_starter.items():
        if key==Question[0]:
            reponse_starter=val
    if reponse_starter=="":
        reponse_starter="Je ne connais pas cette question mais je dirais, "
    if reponse_starter[-1]== " ":
        reponse_starter+=chr(ord(Reponse[0])-32)
    else:
        reponse_starter+=Reponse[0]
    return reponse_starter+Reponse[1:]
