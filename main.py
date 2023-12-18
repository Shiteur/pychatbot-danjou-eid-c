# chatbot2000,Rayan EID et Thomas DANJOU,script principal du projet.
from fonctions_de_bases import *
from fonction_menu import *
from fonctions_fonctionnalites import *
from fonction_generateur_de_reponse import *
# permet de faire un traitement de tous les fichiers du répertoire speeches lors du lancement du script.
convertion_minuscule()
surpession_ponctuation()
#corp du script principal permettant d'appeler les fonctions développé dans les autres scripts .py sur la demande du l'utilisateur.
start=True
while start:
    decision=0
    menu()
    choix = input("Choisissez une option: ")
    if choix =="1":
       decision=1
    elif choix == "2":
        print("Vous quitter l'aplication.")
        decision=2
    elif choix== "3":
        start=False
    else:
        print("Choix invalide.")
    while decision==1:
        fonctionnalites()
        choix=input("Choisissez une fonctionnalité: ")
        if choix == "1":
            mots_non_importants = mot_pas_important()
            print("Mots non importants:", mots_non_importants)
        elif choix == "2":
            mot_tfidf_max = mot_important()
            print("Mot(s) avec le score TD-IDF le plus élevé:", mot_tfidf_max)
        elif choix == "3":
            mots_chirac = mot_plus_repeter_par_chirac()
            print("Mot(s) le(s) plus répété(s) par le président Chirac:", mots_chirac)
        elif choix == "4":
            nation()
        elif choix == "5":
            ecologie()
        elif choix == "6":
            mots_evoques()
        elif choix == "7":
            print("Vous retrouner au menu principal.")
            decision=0
        else:
            print("Choix invalide.")
    while decision==2:
        generateur_de_reponse()
        choix=input("Choisissez une option: ")
        if choix=="1":
            question=input("Entez votre question:")
            print(affine_reponse(question,generateur_de_reponse(question)))
        elif choix=="2":
            print("Vous retrouner au menu principal.")
            decision=0
        else:
            print("Choix invalide.")

