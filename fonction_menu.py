# pychatbot-danjou-eid-d,Rayan EID et Thomas DANJOU,script contenant l'affichage de l'interface menu.
#fonction permettant d'afficher le menu principale, pas besoin de paramètre.
def menu():
    print("1. Pour accéder aux fonctionnalités classiques.")
    print("2. Pour accéder au générateur de réponses automatiques.")
    print("3. Pour quitter.")
#fonction qui affiche le menu des fonctionnalités. Pas de paramètre nécessaire.
def fonctionnalites():
    print("Les fonctionnalités classiques:")
    print("1. Affiche la liste des mots les moins importants.")
    print("2. Affiche le mot avec le score TD-IDF le plus élevé.")
    print("3. Indique le(s) mot(s) le(s) plus répété(s) par le président Chirac.")
    print("4. Indique le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation ».")
    print("5. Indique le premier président à parler du climat et/ou de l'écologie.")
    print("6. Mot(s) évoqués par tous les présidents (hormis les mots non importants).")
    print("7. Pour retourner en arrière.")
#fonction qui affiche de menu du générateur de réponses aucun paramètre nécessaire.
def generateur_de_reponse():
    print("Les fonctionnalités du générateur de réponses automatiques:")
    print("1. Pour poser une question.")
    print("2. Pour retourner en arrière.")