import random

mot_de_passe =""

lettres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffres = "0123456789"
caracteres_speciaux = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
caracteres_finaux = lettres

taille_mot_de_passe = int(input("Combien de caractères souhaitez-vous dans votre mot de passe ? "))
utilisation_chiffres_input = input("Voulez vous inclure des chiffres ? (oui/non) ")
utilisation_chiffres_input = utilisation_chiffres_input.lower()
utilisation_symboles_input = input("Voulez vous inclure des caractères spéciaux ? (oui/non) ")
utilisation_symboles_input = utilisation_symboles_input.lower()

if utilisation_chiffres_input == "oui" :
    caracteres_finaux += chiffres
    mot_de_passe += random.choice(chiffres)  
if utilisation_symboles_input == "oui" :
    caracteres_finaux += caracteres_speciaux
    mot_de_passe += random.choice(caracteres_speciaux)

restants = taille_mot_de_passe - len(mot_de_passe)

for i in range(restants):
    mot_de_passe += random.choice(caracteres_finaux)
    mot_de_passe = ''.join(random.sample(mot_de_passe, len(mot_de_passe)))
print("Mot de passe généré :", mot_de_passe)