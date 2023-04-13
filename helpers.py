import re
from hashlib import sha256

def verifier_mdp(mdp):
    """
    Vérifie si un mot de passe respecte les critères de complexité suivants :
    - Au moins 8 caractères
    - Au moins une lettre minuscule
    - Au moins une lettre majuscule
    - Au moins un chiffre
    - Au moins un caractère spécial parmi !@#$%^&*
    
    Args:
        mdp (str): Le mot de passe à vérifier.
        
    Returns:
        re.Match object: L'objet résultant de la recherche de motif si le mot de passe est valide,
        None: Sinon.
    """
    pattern = re.compile(r"^(?=.*[a-z]+)(?=.*[A-Z]+)(?=.*[0-9]+)(?=.*[!@#\$%\^&\*]+){8,}")
    return re.match(pattern, mdp)

def encoder_mdp(mdp):
    """
    La fonction encoder_mdp prend un mot de passe en paramètre et renvoie son hash SHA256 encodé en hexadécimal.

    :param mdp: le mot de passe à encoder
    :type mdp: str
    :return: le hash SHA256 encodé en hexadécimal du mot de passe
    :rtype: str
    """
    password_bytes = mdp.encode("utf-8")
    hash_obj = sha256(password_bytes).hexdigest()
    return hash_obj

def generer_donnee(utilisateur, mdp):
    """
    La fonction generer_donnee prend un nom d'utilisateur et un mot de passe en paramètres, puis renvoie un dictionnaire contenant le nom d'utilisateur et le hash SHA256 encodé en hexadécimal du mot de passe.

    :param utilisateur: le nom d'utilisateur
    :type utilisateur: str
    :param mdp: le mot de passe à encoder
    :type mdp: str
    :return: un dictionnaire contenant le nom d'utilisateur et le hash SHA256 encodé en hexadécimal du mot de passe
    :rtype: dict
    """
    return {
        "username": utilisateur,
        "password_hash": encoder_mdp(mdp)
        }