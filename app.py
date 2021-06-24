import sqlite3

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
db = sqlite3
app.config['SECRET_KEY'] = 'hexabyte'


def get_db_connection():
    conn = sqlite3.connect('lukas.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM delivery').fetchall()
    conn.close()
    return render_template('index.html', data=data)


@app.route('/register', methods=['GET', 'POST'])
def action():
    if request.method == 'POST':
        name = ['Lukas Vanden Branden']
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO delivery (worker) VALUES (?)', name)
        conn.commit()
        conn.close()
        return redirect(url_for('hello_world'))


@app.route('/delete/<string:id>', methods=['GET', 'POST'])
def delete(id):
    if request.method == 'POST':
        conn = get_db_connection()
        conn.execute(
            'Delete from delivery  where id = ?', (id,))
        conn.commit()
        conn.close()
        return redirect(url_for('hello_world'))


@app.route('/<string:page>')
def page(page):
    try:
        return redirect(url_for('hello_world')) or render_template('index.html')
    except:
        return redirect(url_for('hello_world')) or render_template('index.html')


if __name__ == '__main__':
    app.run()
