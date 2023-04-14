import os
import json
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

def localiser_fichier():
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    filename = "data_pwd.json"
    filepath = os.path.join(script_dir, filename)
    return filepath

def ajouter_mdp(utilisateur, mdp):
    """
    """
    
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