from app import app, socketio, history
from flask import render_template, request, redirect, url_for, session
from flask_socketio import send

username = None

@socketio.on('message')
def handleMessage(msg):
    username = "Anonym"
    if "username" in session:
        username = session["username"]
    else:
        session["username"] = username
    new_msg = {"username":username, "message":msg}
    send(new_msg, broadcast=True)
    history.insert_one(new_msg)

@app.route('/')
def index():
    messages = history.find({},{"_id":0})
    return render_template('index.html', messages=messages)

@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form["username"] != '':
            session["username"] = request.form["username"]
        else:
            session["username"] = "Anonym"
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout/')
def logout():
    session.pop("username")
    return redirect(url_for("index"))

if __name__ == '__main__':
    socketio.run(app, port=8000)