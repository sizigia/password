import json
import os
import re
from hashlib import sha256
from helpers import verifier_mdp, encoder_mdp, generer_donnee

utilisateur = input("Veuillez entrer votre nom d'utilisateur : ")
mdp = input("Veuillez entrer votre mot de passe : ")

while not verifier_mdp(mdp):
    print("Votre mot de passe n'est pas valide.")
    mdp = input("Veuillez entrer votre mot de passe : ")


script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
filename = "data_pwd.json"
filepath = os.path.join(script_dir, filename)

if not os.path.exists(filepath):
    with open(filepath, "w") as file:
        db_start = { "users": [
            generer_donnee(utilisateur, mdp)
        ] }
        json.dump(db_start, file)
        print("Mot de passe ajouté.")
else:
    with open(filepath, "r+") as file:
        data = json.load(file)
        user = next((item for item in data['users'] if item.get('username') == utilisateur), None)
        if user is None:
            data["users"].append(generer_donnee(utilisateur, mdp))
            json.dump(data, file)
            print("Mot de passe ajouté.")
        else:
            ut_mssg = "L'utilisateur existe déjà mais le mot de passe n'a pas été ajouté,"
            if encoder_mdp(mdp) == user['password_hash']:
                print(f"{ut_mssg} il est correct.")
            else:
                print(f"{ut_mssg} il est incorrect.")
