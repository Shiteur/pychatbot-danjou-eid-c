from fonctions import *
# appelle la fonction list_of_files
directory = "speeches"
files_names = list_of_files(directory, "txt")
# appelle la fonction convertion_minuscule
convertion_minuscule()
surpession_ponctuation()

def menu():
    print("1. Pour accéder aux fonctionnalités classiques.")
    print("2. Pour accéder au générateur de réponses automatiques.")
    print("3. Pour quitter.")
def fonctionnalites():
    print("Les fonctionnalités classiques:")
    print("1. Affiche la liste des mots les moins importants")
    print("2. Affiche le mot avec le score TD-IDF le plus élevé")
    print("3. Indique le(s) mot(s) le(s) plus répété(s) par le président Chirac")
    print("4. Indique le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation »")
    print("5. Indique le premier président à parler du climat et/ou de l'écologie")
    print("6. Mot(s) évoqués par tous les présidents (hormis les mots non importants)")
    print("7. Pour retourner en arrière.")
def generateur_de_reponse():
    print("1. Pour poser une question.")
    print("2. Pour retourner en arrière.")
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

