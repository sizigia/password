import os
import json
from helpers import generer_donnee, encoder_mdp, verifier_mdp

def afficher_menu():
    """
    """

    print(""":::GESTION DES MOTS DE PASSE:::
    Menu :
    1. Ajouter un nouveau mot de passe
    2. Afficher tous les mots de passe
    3. Quitter
    """)
# end def

def localiser_fichier():
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    filename = "data_pwd.json"
    filepath = os.path.join(script_dir, filename)
    return filepath

def ajouter_mdp():
    """
    """
    utilisateur = input("Veuillez entrer votre nom d'utilisateur : ")
    mdp = input("Veuillez entrer votre mot de passe : ")
    
    while not verifier_mdp(mdp):
        print("Votre mot de passe n'est pas valide.")
        mdp = input("Veuillez entrer votre mot de passe : ")
    
    filepath = localiser_fichier()

    message = ''

    if not os.path.exists(filepath):
        with open(filepath, "w") as file:
            db_start = { "users": [
                generer_donnee(utilisateur, mdp)
            ] }
            json.dump(db_start, file)
            message = "Mot de passe ajouté."
    else:
        with open(filepath, "r+") as file:
            data = json.load(file)
            user = next((item for item in data['users'] if item.get('username') == utilisateur), None)
            if user is None:
                data["users"].append(generer_donnee(utilisateur, mdp))
                file.seek(0)
                json.dump(data, file)
                file.truncate()
                message = "Mot de passe ajouté."
            else:
                message = "L'utilisateur existe déjà mais le mot de passe n'a pas été ajouté,"
                if encoder_mdp(mdp) == user['password_hash']:
                    message = f"{message} il est correct."
                else:
                    message = f"{message} il est incorrect."
    print(message)
    return None 
# end def

def afficher_mdp():
    """
    """
    filepath = localiser_fichier()

    with open(filepath, "r+") as file:
        data = json.load(file)
        mdp = (user["password_hash"] + '\n' for user in data["users"])
        print(*mdp)
    return None
# end def

def demarrage():
    """
    """
    afficher_menu()
    choix = input("Veuillez choisir une option : ")
    
    return choix
# end def

OPTIONS = {
    "1": ajouter_mdp,
    "2": afficher_mdp,
    "3": exit
}

choix = demarrage()

while True:
    if choix in OPTIONS:
        OPTIONS[choix]()
        choix = demarrage()
    else:
        print("Option invalide. Veuillez réessayer.")
        while not choix in OPTIONS:
            choix = demarrage()