from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/apps')
def apps():
    return render_template('apps.html')

@app.route('/sites')
def sites():
    return render_template('sites.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/peter')
def peter():
    return render_template('peter.html')

@app.route('/bekhruz')
def bekhruz():
    return render_template('bekhruz.html')

if __name__ == "__main__":
    app.run()
