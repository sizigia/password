from helpers import generer_donnee, encoder_mdp

def afficher_menu():
    """
    """

    print("""GESTION DES MOTS DE PASSE.
    Menu :
    1. Ajouter un nouveau mot de passe
    2. Afficher tous les mots de passe
    3. Quitter
    """)
# end def

def ajouter_mdp(utilisateur, mdp):
    """
    """
    print()
    generer_donnee(utilisateur, mdp)
    return None
# end def

def afficher_mdp():
    """
    """
    print()
    return None
# end def

afficher_menu()
choix = input("Veuillez choisir une option : ")

options = {
    "1": ajouter_mdp,
    "2": afficher_mdp,
    "3": exit
}

if choix in options:
    options[choix]()
else:
    print("Option invalide. Veuillez réessayer.")
    while not choix in options:
        afficher_menu()
        choix = input("Veuillez choisir une option : ")