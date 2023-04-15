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
print("_________________________SUCCESS!___________________________")
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


@app.route('/register_customer')
def register_customer():
    return render_template('register_customer.html')


@app.route('/register_staff')
def register_staff():
    return render_template('register_staff.html')


@app.route('/register_agent')
def register_agent():
    return render_template('register_agent.html')

# Authenticates the login


@app.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
    # grabs information from the forms
    username = request.form['username']
    password = request.form['password']

    # cursor used to send queries
    cursor = mysql.cursor()
    # executes query
    query = "SELECT * FROM test_register WHERE username = '{}' and password = MD5('{}')"
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
        # encrypting the password
        ins = "INSERT INTO test_register VALUES('{}', MD5('{}'))"
        cursor.execute(ins.format(username, password))
        mysql.commit()  # commit the newly registered entry to the table
        cursor.close()
        return render_template('index.html')


@app.route('/registerCustomer', methods=['GET', 'POST'])
def registerCustomer():
    # grabs information from the forms
    email = request.form['email']
    password = request.form['password']
    name = request.form['name']
    building_number = request.form['building_number']
    street = request.form['street']
    city = request.form['city']
    state = request.form['state']
    phone_number = request.form['phone_number']
    passport_number = request.form['passport_number']
    passport_expiration = request.form['passport_expiration']
    passport_country = request.form['passport_country']
    date_of_birth = request.form['date_of_birth']

    # cursor used to send queries
    cursor = mysql.cursor()
    # executes query
    query = "SELECT * FROM customer WHERE email = '{}'"
    cursor.execute(query.format(email))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    error = None
    if (data) is not None:
        # If the previous query returns data, then user exists
        error = "The email is already occupied!"
        return render_template('register_customer.html', error=error)
    else:
        # encrypting the password
        ins = "INSERT INTO customer VALUES('{}', '{}', MD5('{}'), '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
        cursor.execute(ins.format(email, name, password, building_number, street, city, state,
                       phone_number, passport_number, passport_expiration, passport_country, date_of_birth))
        mysql.commit()  # commit the newly registered entry to the table
        cursor.close()
        return render_template('success.html')


@app.route('/registerStaff', methods=['GET', 'POST'])
def getAirlines():
    query_for_airlines = "SELECT * FROM airline"
    cursor = mysql.cursor()
    cursor.execute(query_for_airlines)
    airlines = cursor.fetchall()
    cursor.close()
    return airlines


def registerStaff():
    # grabs information from the forms
    username = request.form['username']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    date_of_birth = request.form['date_of_birth']
    airline_name = request.form['airline_name']

    # TODO:think how this should be implemented
    permission = "EMPTY"
    airlines = getAirlines()
    # cursor used to send queries
    cursor = mysql.cursor()

    # checking whether the USERNAME is in the DB
    query = "SELECT * FROM airline_staff WHERE username = '{}'"
    cursor.execute(query.format(username))
    data = cursor.fetchone()
    error = None
    if (data) is not None:
        # If the previous query returns data, then user exists
        error = "The username is already occupied! Please choose another one."
        return render_template('register_staff.html', error=error)
    else:
        # encrypting the password
        ins = "INSERT INTO airline VALUES('{}', MD5('{}'), '{}', '{}', '{}', '{}')"
        cursor.execute(ins.format(username, password, first_name,
                       last_name, date_of_birth, airline_name, permission))
        mysql.commit()  # commit the newly registered entry to the table
        cursor.close()
        return render_template('success.html')
    # TODO: I never pass the airlines to the form
    return render_template('register_staff.html', airlines=airlines)


@app.route('/home')
def home():
    username = session['username']
    cursor = mysql.cursor()
    # similar logic for the display of the flight info
    query = "SELECT * FROM test_register WHERE username = '{}'"
    cursor.execute(query.format(username))
    data1 = cursor.fetchall()
    cursor.close()
    return render_template('home.html', username=username, posts=data1)

# airline staff page


# @app.route('/airline_staff')
# def home():
#     username = session['username']
#     cursor = mysql.cursor()
#     # similar logic for the display of the flight info
#     query = "SELECT * FROM test_register WHERE username = '{}'"
#     cursor.execute(query.format(username))
#     data1 = cursor.fetchall()
#     cursor.close()
#     return render_template('home.html', username=username, posts=data1)

# customer page


# @app.route('/customer_page')
# def home():
#     username = session['username']
#     cursor = mysql.cursor()
#     # similar logic for the display of the flight info
#     query = "SELECT * FROM test_register WHERE username = '{}'"
#     cursor.execute(query.format(username))
#     data1 = cursor.fetchall()
#     cursor.close()
#     return render_template('home.html', username=username, posts=data1)
# booking agent page


# @app.route('/booking_agent')
# def home():
#     username = session['username']
#     cursor = mysql.cursor()
#     # similar logic for the display of the flight info
#     query = "SELECT * FROM test_register WHERE username = '{}'"
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
