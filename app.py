from distutils.log import debug
from turtle import position
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MySQL_DATABASE_HOST'] = 'localhost'
app.config['MySQL_DATABASE_USER'] = 'root'
app.config['MySQL_DATABASE_PASSWORD'] = 'root'
app.config['MySQL_DATABASE_DB'] = 'crudapp'

mysql = MySQL(app)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/insert', methods=['POST'])
def insert():

    if request.method == "POST":
        playername = request.form['playername']
        squadnumber = request.form['squadnumber']
        position = request.form['position']
        appearances = request.form['apps']
        goals = request.form['goals']
        assists = request.form['assists']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO players (playername, squadnumber, position, appearances, goals, assists) VALUES (%s, %s, %s, %s, %s, %s)", (playername, int(squadnumber), position, appearances, int(goals), int(assists)))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('Index'))
if __name__ == "__main__":
    app.run(debug=True)