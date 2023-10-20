from flask import Flask, request, render_template, redirect, url_for, session
import mysql.connector

#create MySQL connection
cnx = mysql.connector.connect(host='127.0.0.1', port = '3306', user='root', password = 'bowl7173', database='db_cita450')

app = Flask(__name__)

app.secret_key = 'secretkey12'

@app.route('/')
def home():
    if 'username' in session:
        return 'Logged in as ' + session['username']
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM users WHERE email=%s AND passwd=%s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    cnx.close()
    if user:
        session['username'] = username
        return render_template('main.html')
    else:
        return 'Login failed. Invalid credentials.'

#@app.route('/logout')
#def logout():
#    session.pop('email', None)
#    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)