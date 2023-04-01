from flask import Flask, render_template, request, url_for, redirect, session
import mysql.connector
import os
from dotenv import load_dotenv

# Initialize the app from Flask
app = Flask(__name__)

my_password = os.getenv('MYSQL_ROOT_PASSWORD')
my_database = os.getenv('MYSQL_DATABASE')

# configure database connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = my_password
app.config['MYSQL_DB'] = my_database

# create MySQL connection object
mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB'],
    # you might not even need the "port" part of the code, unless you have multiple MySQL instances running on your machine
    port=3306
)

# create a cursor object for executing queries
cursor = mysql.cursor()

# test the connection
cursor.execute("SELECT DATABASE()")
data = cursor.fetchone()
print("____________________________________________________")
print("Connected to database:", data[0])

# close the cursor and connection objects
cursor.close()
# TODO: is it generally okay if we do not close the connection to the database?
# mysql.close()


@app.route('/')
def welcome():
    if 'username' in session:
        return redirect(url_for('home'))
    return render_template('index.html')

# Define route for login


@app.route('/login')
def login():
    return render_template('login.html')

# Define route for register


@app.route('/register')
def register():
    return render_template('register.html')

# Authenticates the login


@app.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
    # grabs information from the forms
    username = request.form['username']
    password = request.form['password']

    # cursor used to send queries
    cursor = mysql.cursor()
    # executes query
    query = "SELECT * FROM test_register WHERE username = '{}' and password = '{}'"
    cursor.execute(query.format(username, password))
    # stores the results of the query in a variable
    data = cursor.fetchone()  # use fetchall() if you are expecting more than 1 data row
    cursor.close()
    error = None
    if (data):
        # creates a session for the the user
        # session is a built in
        session['username'] = username
        return redirect(url_for('home'))
    else:
        # returns an error message to the html page
        error = 'Invalid login or username'
        return render_template('login.html', error=error)


# Authenticates the register
@app.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
    # grabs information from the forms
    username = request.form['username']
    password = request.form['password']

    # cursor used to send queries
    cursor = mysql.cursor()
    # executes query
    query = "SELECT * FROM test_register WHERE username = '{}'"
    cursor.execute(query.format(username))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    error = None
    if (data):
        # If the previous query returns data, then user exists
        error = "This user already exists"
        return render_template('register.html', error=error)
    else:
        ins = "INSERT INTO test_register VALUES('{}', '{}')"
        cursor.execute(ins.format(username, password))
        mysql.commit()  # commit the newly registered entry to the table
        cursor.close()
        return render_template('index.html')


# @app.route('/home')
# def home():
#     username = session['username']
#     cursor = conn.cursor()
#     query = "SELECT ts, blog_post FROM blog WHERE username = '{}' ORDER BY ts DESC"
#     cursor.execute(query.format(username))
#     data1 = cursor.fetchall()
#     cursor.close()
#     return render_template('home.html', username=username, posts=data1)


# @app.route('/post', methods=['GET', 'POST'])
# def post():
#     username = session['username']
#     cursor = conn.cursor()
#     blog = request.form['blog']
#     query = "INSERT INTO blog (blog_post, username) VALUES('{}', '{}')"
#     cursor.execute(query.format(blog, username))
#     conn.commit()
#     cursor.close()
#     return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('username')
    # I am not sure if that's the right place to close the mysql connection
    mysql.close()
    return redirect('/')


app.secret_key = 'some key that you will never guess'
# Run the app on localhost port 5000
# debug = True -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
