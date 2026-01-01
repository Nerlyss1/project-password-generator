from flask import Flask, make_response, render_template, request
import random

app = Flask(__name__)

lettres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffres = "0123456789"
caracteres_speciaux = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

MIN_LENGTH = 4
MAX_LENGTH = 64

@app.route('/', methods=['GET', 'POST'])
def index():
    mot_de_passe = ""

    # Valeurs par défaut depuis les cookies
    longueur = int(request.cookies.get('longueur', 16))
    include_chiffres = request.cookies.get('chiffres', '0') == '1'
    include_symboles = request.cookies.get('symboles', '0') == '1'

    if request.method == 'POST':
        try:
            longueur = int(request.form.get('longueur', 16))
        except ValueError:
            longueur = 16
        longueur = max(MIN_LENGTH, min(longueur, MAX_LENGTH))

        include_chiffres = request.form.get('chiffres') == 'on'
        include_symboles = request.form.get('symboles') == 'on'

        caracteres_finaux = lettres
        if include_chiffres:
            caracteres_finaux += chiffres
            mot_de_passe += random.choice(chiffres)
        if include_symboles:
            caracteres_finaux += caracteres_speciaux
            mot_de_passe += random.choice(caracteres_speciaux)

        restants = longueur - len(mot_de_passe)
        for _ in range(restants):
            mot_de_passe += random.choice(caracteres_finaux)

        mot_de_passe = ''.join(random.sample(mot_de_passe, len(mot_de_passe)))

    response = make_response(render_template(
        'index.html',
        mot_de_passe=mot_de_passe,
        longueur=longueur,
        include_chiffres=include_chiffres,
        include_symboles=include_symboles
    ))

    response.set_cookie('longueur', str(longueur))
    response.set_cookie('chiffres', '1' if include_chiffres else '0')
    response.set_cookie('symboles', '1' if include_symboles else '0')

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
