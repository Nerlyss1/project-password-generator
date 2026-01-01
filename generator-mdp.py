import random

mot_de_passe =""

lettres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffres = "0123456789"
caracteres_speciaux = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
caracteres_finaux = lettres

nombre_fois = int(input("Combien de caractères souhaitez-vous dans votre mot de passe ? "))
chiffre_oui = input("Voulez vous inclure des chiffres ? (oui/non) ")
chiffre_oui = chiffre_oui.lower()
caracteres_speciaux_oui = input("Voulez vous inclure des caractères spéciaux ? (oui/non) ")
caracteres_speciaux_oui = caracteres_speciaux_oui.lower()

if chiffre_oui == "oui" :
    caracteres_finaux += chiffres
    mot_de_passe += random.choice(chiffres)  
if caracteres_speciaux_oui == "oui" :
    caracteres_finaux += caracteres_speciaux
    mot_de_passe += random.choice(caracteres_speciaux)

restants = nombre_fois - len(mot_de_passe)

for i in range(restants):
    mot_de_passe += random.choice(caracteres_finaux)
    mot_de_passe = ''.join(random.sample(mot_de_passe, len(mot_de_passe)))
print("Mot de passe généré :", mot_de_passe)