from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Define a list of 200 data elements (you can load them from a file or a database)
data_elements = ["Element1", "Element2", "Element3","Element4","Element5","Element6","Element7","Element8","Element9","Element10","Element11","Element12",]

@app.route('/')
def index():
    return render_template('index.html', data_elements=data_elements)

@app.route('/submit', methods=['POST'])
def submit():
    server_details = request.form['server_details']
    persists_data = request.form.get('persists_data')
    tokenizes_data = request.form.get('tokenizes_data')
    retrievable_data = request.form.get('retrievable_data')
    email = request.form['email']

    # Store the responses in a SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO responses (server_details, persists_data, tokenizes_data, retrievable_data, email) VALUES (?, ?, ?, ?, ?)',
                   (server_details, persists_data, tokenizes_data, retrievable_data, email))
    conn.commit()
    conn.close()

    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return "Thank you for submitting the survey!"

if __name__ == '__main__':
    app.run(debug=True)
