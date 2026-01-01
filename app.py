from flask import Flask, render_template, request
import random

app = Flask(__name__)

lettres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffres = "0123456789"
caracteres_speciaux = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

@app.route('/', methods=['GET', 'POST'])
def index():
    mot_de_passe =""    
    if request.method == 'POST':
        longueur = int(request.form.get('longueur', 8))
        include_chiffres = request.form.get('chiffres') == 'on'
        include_symboles = request.form.get('symboles') == 'on'  # <-- correspond au HTML

        caracteres_finaux = lettres
        if include_chiffres:
            caracteres_finaux += chiffres
            mot_de_passe += random.choice(chiffres)
        if include_symboles:
            caracteres_finaux += caracteres_speciaux
            mot_de_passe += random.choice(caracteres_speciaux)

        restants = longueur - len(mot_de_passe)

        for i in range(restants):
            mot_de_passe += random.choice(caracteres_finaux)

        mot_de_passe = ''.join(random.sample(mot_de_passe, len(mot_de_passe)))

    return render_template('index.html', mot_de_passe=mot_de_passe)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
