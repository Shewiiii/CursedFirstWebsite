from flask import Flask, render_template

# mydb = mysql.connector.connect(
#     host=""
# )
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/nerd')

def nerd():
    return render_template('nerd.html')

@app.route('/ressources')

def ressources():
    return render_template('ressources.html')

@app.route('/idsd')

def idsd():
    return render_template('idsd.html')

@app.route('/Comparaison rapide entre le format OGG 320 et MP3 320 vs lossless')

def mp3ogg():
    return render_template('Comparaison rapide entre le format OGG 320 et MP3 320 vs lossless.html')

@app.route('/filtres_test_hqp')

def hqp():
    return render_template('filtres_test_hqp.html')

@app.route('/clic(exercice)/clic')

def clic():
    return render_template('clic(exercice)/clic.html')

@app.route('/gear')

def gear():
    return render_template('gear.html')







if __name__ == "__main__": #toujours à la fin!
    app.run(debug=True)