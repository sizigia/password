import os
import json
from helpers import generer_donnee, encoder_mdp, verifier_mdp

def afficher_menu():
    """
    Affiche le menu principal de l'application de gestion des mots de passe.

    Le menu permet à l'utilisateur de choisir entre plusieurs options, notamment :
    - Ajouter un nouveau mot de passe
    - Afficher tous les mots de passe enregistrés
    - Quitter l'application

    Pour choisir une option, l'utilisateur doit saisir le numéro correspondant à l'option désirée.
    """

    print(""":::GESTION DES MOTS DE PASSE:::
    Menu :
    1. Ajouter un nouveau mot de passe
    2. Afficher tous les mots de passe
    3. Quitter
    """)

def localiser_fichier():
    """
    Cette fonction localise le fichier 'data_pwd.json' dans le même répertoire que le fichier Python qui contient cette fonction.
    
    Returns:
        str: Le chemin d'accès complet au fichier 'data_pwd.json'.
    """
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    filename = "data_pwd.json"
    filepath = os.path.join(script_dir, filename)
    return filepath

def ajouter_mdp():
    """
    Cette fonction permet à l'utilisateur d'ajouter un nom d'utilisateur et un mot de passe dans une base de données
    de mots de passe. Elle demande d'abord à l'utilisateur d'entrer son nom d'utilisateur et son mot de passe, puis 
    vérifie que le mot de passe est valide en appelant la fonction 'verifier_mdp()'. Si le mot de passe n'est pas valide,
    elle demande à l'utilisateur d'en entrer un nouveau jusqu'à ce qu'il soit valide.

    La fonction utilise la fonction 'localiser_fichier()' pour localiser le fichier de base de données de mots de passe,
    puis crée un nouveau fichier de base de données avec le nom d'utilisateur et le mot de passe si le fichier n'existe
    pas encore. Sinon, elle ajoute le nom d'utilisateur et le mot de passe à la liste des utilisateurs existants si le 
    nom d'utilisateur n'existe pas déjà dans la base de données.

    La fonction renvoie un message indiquant si le mot de passe a été ajouté ou non.
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

def afficher_mdp():
    """
    Affiche les mots de passe hashés des utilisateurs stockés dans le fichier JSON spécifié. Le chemin du fichier est obtenu en utilisant la fonction 'localiser_fichier()'. Les mots de passe sont affichés en utilisant la fonction 'print()', séparés par des sauts de ligne.

    Note: Cette fonction ne modifie pas le fichier JSON, elle ne fait que lire les mots de passe stockés.
    """

    filepath = localiser_fichier()

    with open(filepath, "r+") as file:
        data = json.load(file)
        mdp = (user["password_hash"] + '\n' for user in data["users"])
        print(*mdp)
    return None

def demarrage():
    """
    Fonction permettant d'afficher un menu et de demander à l'utilisateur de choisir une option.

    La fonction appelle la fonction "afficher_menu" pour afficher le menu, puis demande à l'utilisateur de saisir une option en utilisant la fonction "input". La valeur saisie par l'utilisateur est renvoyée par la fonction comme résultat.

    Retourne :

    La valeur saisie par l'utilisateur en tant que chaîne de caractères.
    """
    
    afficher_menu()
    choix = input("Veuillez choisir une option : ")
    
    return choix

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