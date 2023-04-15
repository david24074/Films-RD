from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    c.execute('SELECT * FROM movies')
    movies = c.fetchall()
    conn.close()
    return render_template('index.html', users=users, movies=movies)

@app.route('/users')
def login():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()
    return render_template('login.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
