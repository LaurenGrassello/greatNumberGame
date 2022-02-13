from flask import Flask, render_template, session, request, redirect
import random


app = Flask(__name__)
app.secret_key = 'secretsecretsarenofun'


@app.route('/')
def index():
    if 'randnum' in session:
        pass
    else:
        session['randnum'] = random.randint(1,100)
    if 'user_attempt' in session:
        pass
    else:
        session['user_attempt'] = 0
    if 'guess' in session:
        pass
    else:
        if request.form.get('guess'):
            session['guess'] = int(request.form['guess'])
        else:
            session['guess'] = -1
    return render_template("index.html")

@app.route('/play_again')
def play_again():
    session.clear()
    return redirect("/")

@app.route('/guess', methods=['POST'])
def guess():
    if 'user_attempt' in session:
        session['user_attempt'] += 1
    else:
        session['user_attempt'] = 0
    session['guess'] = int(request.form['guess'])
    session['randnum'] = int(session['randnum'])
    return redirect("/")


@app.route('/destroy_session')
def destroy():
    session.clear()
    return render_template('index.html')
        

if __name__=="__main__":
    app.run(debug=True)