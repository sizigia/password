import json
import os
import re
from hashlib import sha256
from helpers import verifier_mdp, encoder_mdp, generer_donnee
from gerer_mdps import ajouter_mdp, localiser_fichier

utilisateur = input("Veuillez entrer votre nom d'utilisateur : ")
mdp = input("Veuillez entrer votre mot de passe : ")

while not verifier_mdp(mdp):
    print("Votre mot de passe n'est pas valide.")
    mdp = input("Veuillez entrer votre mot de passe : ")
    
ajouter_mdp(utilisateur, mdp)