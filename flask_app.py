from flask import (
    Flask,
    flash,
    render_template,
    request,
    url_for,
    redirect,
    session,
    Response,
)
import mysql.connector
import os
from dotenv import load_dotenv

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io
import uuid


app = Flask(__name__)

my_password = os.getenv("MYSQL_ROOT_PASSWORD")
my_database = os.getenv("MYSQL_DATABASE")

# configure database connection
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = my_password
app.config["MYSQL_DB"] = my_database

app.config["UPLOAD_FOLDER"] = os.path.join(app.root_path, "static")
print("Destination folder: ", app.config["UPLOAD_FOLDER"])

# create MySQL connection object
mysql = mysql.connector.connect(
    host=app.config["MYSQL_HOST"],
    user=app.config["MYSQL_USER"],
    password=app.config["MYSQL_PASSWORD"],
    database=app.config["MYSQL_DB"],
    # you might not even need the "port" part of the code, unless you have multiple MySQL instances running on your machine
    port=3306,
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


@app.route("/")
def welcome():
    if "username" in session:
        return redirect(url_for("home"))
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/about_us")
def about_us():
    return render_template("about_us.html")


@app.route("/register_customer")
def register_customer():
    return render_template("register_customer.html")


@app.route("/register_staff", methods=["GET", "POST"])
def register_staff():
    query_for_airlines = "SELECT name FROM airline"
    cursor = mysql.cursor()
    cursor.execute(query_for_airlines)
    airlines = [row[0] for row in cursor.fetchall()]  # extract only the string values
    cursor.close()
    return render_template("register_staff.html", airlines=airlines)


@app.route("/register_agent")
def register_agent():
    return render_template("register_agent.html")


@app.route("/registerAgent", methods=["GET", "POST"])
def registerAgent():
    # grabs information from the forms
    email = request.form["email"]
    password = request.form["password"]
    booking_agent_id = request.form["booking_agent_id"]

    # cursor used to send queries
    cursor = mysql.cursor()
    # executes query
    query = "SELECT * FROM booking_agent WHERE email = '{}'"
    cursor.execute(query.format(email))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    error = None

    if (data) is not None:
        # If the previous query returns data, then user exists
        error = "User exists! Please log in!"
        return render_template("register_agent.html", error=error)

    else:
        # encrypting the password
        ins = "INSERT INTO booking_agent VALUES('{}', MD5('{}'), '{}')"
        cursor.execute(ins.format(email, password, booking_agent_id))
        mysql.commit()  # commit the newly registered entry to the table
        cursor.close()
        return render_template("success.html")


@app.route("/loginAuth", methods=["GET", "POST"])
def loginAuth():
    # grabs information from the forms
    user_type = request.form["user_type"]

    if user_type == "-- SELECT USER TYPE --":
        error = "Please select a user type!"
        return render_template("login.html", error=error)

    email = request.form["email"]
    password = request.form["password"]

    if user_type == "Customer":
        query = "SELECT * FROM customer WHERE email = '{}' and password = MD5('{}')"

    elif user_type == "Airline Staff":
        query = (
            "SELECT * FROM airline_staff WHERE username = '{}' and password = MD5('{}')"
        )

    else:
        query = (
            "SELECT * FROM booking_agent WHERE email = '{}' and password = MD5('{}')"
        )

    cursor = mysql.cursor()
    cursor.execute(query.format(email, password))
    data = cursor.fetchone()
    cursor.close()
    error = None

    if data:
        session["email"] = email
        session["user_type"] = user_type
        return redirect(url_for("home"))

    else:
        error = "Invalid login or email"
        return render_template("login.html", error=error)


@app.route("/registerCustomer", methods=["GET", "POST"])
def registerCustomer():
    # grabs information from the forms
    email = request.form["email"]
    password = request.form["password"]
    name = request.form["name"]
    building_number = request.form["building_number"]
    street = request.form["street"]
    city = request.form["city"]
    state = request.form["state"]
    phone_number = request.form["phone_number"]
    passport_number = request.form["passport_number"]
    passport_expiration = request.form["passport_expiration"]
    passport_country = request.form["passport_country"]
    date_of_birth = request.form["date_of_birth"]

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
        return render_template("register_customer.html", error=error)
    else:
        # encrypting the password
        ins = "INSERT INTO customer VALUES('{}', '{}', MD5('{}'), '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
        cursor.execute(
            ins.format(
                email,
                name,
                password,
                building_number,
                street,
                city,
                state,
                phone_number,
                passport_number,
                passport_expiration,
                passport_country,
                date_of_birth,
            )
        )
        mysql.commit()  # commit the newly registered entry to the table
        cursor.close()
        return render_template("success.html")


@app.route("/registerStaff", methods=["GET", "POST"])
def registerStaff():
    # grabs information from the forms
    username = request.form["username"]
    password = request.form["password"]
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    date_of_birth = request.form["date_of_birth"]
    airline_name = request.form["airline_name"]

    cursor = mysql.cursor()

    # checking whether the USERNAME is in the DB
    query = "SELECT * FROM airline_staff WHERE username = '{}'"
    cursor.execute(query.format(username))
    data = cursor.fetchone()
    error = None
    if (data) is not None:
        # If the previous query returns data, then user exists
        error = "The username is already occupied! Please choose another one."
        return render_template("register_staff.html", error=error)
    else:
        # by default the permission is N/A
        ins = "INSERT INTO airline_staff (username, password, first_name, last_name, date_of_birth, airline_name, permission) VALUES ('{}', MD5('{}'), '{}', '{}', '{}', '{}', 'N/A')"
        cursor.execute(
            ins.format(
                username, password, first_name, last_name, date_of_birth, airline_name
            )
        )

        mysql.commit()  # commit the newly registered entry to the table
        cursor.close()
        return render_template("success.html")


@app.route("/home")
def home():
    email = session["email"]
    user_type = session["user_type"]

    if user_type == "Customer":
        cursor = mysql.cursor()
        query = "SELECT F.flight_num, F.airline_name, F.departure_airport_name, F.departure_time, F.arrival_airport_name, F.arrival_time, F.dep_status FROM ticket as T JOIN flight as F ON T.flight_id = F.flight_num WHERE customer_email = '{}' AND dep_status = 'Upcoming';"
        cursor.execute(query.format(email))
        data = cursor.fetchall()
        cursor.close()
        return render_template(
            "home.html", email=email, user_type=user_type, upcoming_flights=data
        )

    elif user_type == "Airline Staff":
        query = "SELECT first_name, last_name, airline_name, permission FROM airline_staff WHERE username = '{}';"
        cursor = mysql.cursor()
        cursor.execute(query.format(email))

        output = cursor.fetchone()
        first_name = output[0]
        last_name = output[1]
        airline_name = output[2]
        permission = output[3]

        query = "SELECT airline_name, flight_num, departure_airport_name, departure_time, arrival_airport_name, arrival_time, dep_status FROM flight WHERE airline_name = '{}' AND departure_time BETWEEN NOW() AND DATE_ADD(NOW(), INTERVAL 30 DAY);"
        cursor.execute(query.format(airline_name))
        table_data = cursor.fetchall()
        cursor.close()

        return render_template(
            "home.html",
            email=email,
            user_type=user_type,
            first_name=first_name,
            last_name=last_name,
            airline_name=airline_name,
            permission=permission,
            upcoming_flights=table_data,
        )

    else:
        query = "SELECT airline_name FROM booking_agent_work_for WHERE email = '{}';"
        cursor = mysql.cursor()
        cursor.execute(query.format(email))
        output = cursor.fetchone()
        airline_name = output[0]

        query = "SELECT F.airline_name, F.flight_num, F.departure_airport_name, F.departure_time, F.arrival_airport_name, F.arrival_time, F.dep_status, T.customer_email FROM purchases as P JOIN ticket as T on P.ticket_id = T.id JOIN flight F on (T.flight_id = F.flight_num AND T.airline_name = F.airline_name) WHERE F.airline_name = '{}' AND P.booking_agent_id = '{}' AND F.dep_status = 'Upcoming';"
        cursor.execute(query.format(airline_name, email))
        table_data = cursor.fetchall()

        query = "SELECT DISTINCT F.departure_airport_name FROM purchases as P JOIN ticket as T on P.ticket_id = T.id JOIN flight F on (T.flight_id = F.flight_num AND T.airline_name = F.airline_name) WHERE F.airline_name = '{}' AND P.booking_agent_id = '{}'"
        cursor.execute(query.format(airline_name, email))
        departure_airports = cursor.fetchall()

        query = "SELECT DISTINCT F.departure_airport_name FROM purchases as P JOIN ticket as T on P.ticket_id = T.id JOIN flight F on (T.flight_id = F.flight_num AND T.airline_name = F.airline_name) WHERE F.airline_name = '{}' AND P.booking_agent_id = '{}'"
        cursor.execute(query.format(airline_name, email))
        arrival_airports = cursor.fetchall()

        cursor.close()
        return render_template(
            "home.html",
            user_type=user_type,
            email=email,
            upcoming_flights=table_data,
            airline_name=airline_name,
            departure_airports=departure_airports,
            arrival_airports=arrival_airports,
        )


@app.route("/staff_flight_search", methods=["POST"])
def staffFlightSearch():
    email = session["email"]
    user_type = session["user_type"]

    query = "SELECT first_name, last_name, airline_name, permission FROM airline_staff WHERE username = '{}';"
    cursor = mysql.cursor()
    cursor.execute(query.format(email))

    output = cursor.fetchone()
    first_name = output[0]
    last_name = output[1]
    airline_name = output[2]
    permission = output[3]

    start_date = request.form["start-date"]
    end_date = request.form["end-date"]
    departure_airport = request.form["departure_airport"]
    arrival_airport = request.form["arrival_airport"]

    start_date_f = bool(start_date == "")
    end_date_f = bool(end_date == "")
    departure_airport_f = bool(departure_airport == "")
    arrival_airport_f = bool(arrival_airport == "")

    attributes = []
    if not departure_airport_f:
        attributes.append('departure_airport_name = "{}"'.format(departure_airport))
    if not arrival_airport_f:
        attributes.append('arrival_airport_name = "{}"'.format(arrival_airport))
    if not start_date_f:
        attributes.append(
            'departure_time BETWEEN DATE("{}") and DATE("{}")'.format(
                start_date, end_date
            )
        )

    # concatenate all the attributes and produce a query
    if len(attributes) > 0:
        for i in range(len(attributes)):
            if i == 0:
                query = (
                    "SELECT airline_name, flight_num, departure_airport_name, departure_time, arrival_airport_name, arrival_time, dep_status FROM flight WHERE "
                    + attributes[i]
                )
            else:
                query = query + " AND " + attributes[i]
        query = query + ";"
        cursor.execute(query)
        table_data = cursor.fetchall()
        return render_template(
            "home.html",
            email=email,
            user_type=user_type,
            first_name=first_name,
            last_name=last_name,
            airline_name=airline_name,
            permission=permission,
            upcoming_flights=table_data,
        )

    if len(attributes) == 0 or len(table_data) == 0:
        query = "SELECT airline_name, flight_num, departure_airport_name, departure_time, arrival_airport_name, arrival_time, dep_status FROM flight WHERE airline_name = '{}' AND departure_time BETWEEN NOW() AND DATE_ADD(NOW(), INTERVAL 30 DAY);".format(
            airline_name
        )
        error = "Results based on your search critera are empty! Showing all upcoming flights for the next 30 days."
        cursor.execute(query)
        table_data = cursor.fetchall()
        return render_template(
            "home.html",
            email=email,
            user_type=user_type,
            first_name=first_name,
            last_name=last_name,
            airline_name=airline_name,
            permission=permission,
            upcoming_flights=table_data,
            error=error,
        )


@app.route("/staff_add_airplane")
def staffAddAirplane():
    query = "SELECT permission FROM airline_staff WHERE username = '{}';"
    staff_email = session["email"]

    cursor = mysql.cursor()
    cursor.execute(query.format(staff_email))
    permission = cursor.fetchone()[0]
    cursor.close()

    if permission != "admin":
        return render_template("invalid_auth.html")
    else:
        return render_template("staff_add_airplane.html")


@app.route("/addAirplane", methods=["POST"])
def addAirplane():
    seats = request.form["seats"]
    airplane_id = request.form["airplane_id"]

    staff_email = session["email"]
    user_type = session["user_type"]

    # check if the airplane_id already exists
    query = "SELECT * FROM airplane WHERE id = '{}';"
    cursor = mysql.cursor()
    cursor.execute(query.format(airplane_id))
    data = cursor.fetchall()
    cursor.close()

    # get the permission of the staff
    query = "SELECT permission FROM airline_staff WHERE username = '{}';"
    cursor = mysql.cursor()
    cursor.execute(query.format(staff_email))
    permission = cursor.fetchone()[0]
    cursor.close()

    # check if airplane_id already exists and display the error message
    if data:
        error = "Airplane ID already exists!"
        flash(error, "error")
        return redirect(url_for("home"))

    # check if the staff is authorized to add airplane (permission)
    if (
        permission == "N/A"
        or permission == "operator"
        or user_type == "Customer"
        or user_type == "Booking Agent"
    ):
        error = "You are not authorized to add airplane!"
        flash(error, "error")
        return redirect(url_for("home"))

    query = "SELECT airline_name FROM airline_staff WHERE username = '{}';"
    cursor = mysql.cursor()
    cursor.execute(query.format(staff_email))
    airline_name = cursor.fetchone()[0]
    cursor.close()

    query = "INSERT INTO airplane (id, seats, airline_name) VALUES ('{}', '{}', '{}');"
    cursor = mysql.cursor()
    cursor.execute(query.format(airplane_id, seats, airline_name))
    mysql.commit()
    cursor.close()

    flash("Airplane added successfully!", "success")
    return redirect(url_for("home"))


@app.route("/staff_add_airport")
def staffAddAirport():
    query = "SELECT permission FROM airline_staff WHERE username = '{}';"
    staff_email = session["email"]

    cursor = mysql.cursor()
    cursor.execute(query.format(staff_email))
    permission = cursor.fetchone()[0]
    cursor.close()

    if permission != "admin":
        return render_template("invalid_auth.html")
    else:
        return render_template("staff_add_airport.html")


@app.route("/addAirport", methods=["POST"])
def addAirport():
    airport_code = request.form["airport_code"]
    city_name = request.form["city_name"]

    staff_email = session["email"]
    user_type = session["user_type"]

    # check if the airport already exists
    query = "SELECT * FROM airport WHERE name = '{}';"
    cursor = mysql.cursor()
    cursor.execute(query.format(airport_code))
    data = cursor.fetchall()
    cursor.close()

    # get the permission of the staff
    query = "SELECT permission FROM airline_staff WHERE username = '{}';"
    cursor = mysql.cursor()
    cursor.execute(query.format(staff_email))
    permission = cursor.fetchone()[0]
    cursor.close()

    # check if airplane_id already exists and display the error message
    if data:
        error = "Airport already exists!"
        flash(error, "error")
        return redirect(url_for("home"))

    # check if the staff is authorized to add airplane (permission)
    if permission == "N/A" or permission == "operator" or user_type != "Airline Staff":
        error = "You are not authorized to add airport!"
        flash(error, "error")
        return redirect(url_for("home"))

    query = "INSERT INTO airport (name, city) VALUES ('{}', '{}');"
    cursor = mysql.cursor()
    cursor.execute(query.format(airport_code, city_name))
    mysql.commit()
    cursor.close()

    flash("Airport added successfully!", "success")
    return redirect(url_for("home"))


@app.route("/staff_create_flight")
def staffCreateFlight():
    query = "SELECT permission FROM airline_staff WHERE username = '{}';"
    staff_email = session["email"]

    cursor = mysql.cursor()
    cursor.execute(query.format(staff_email))
    permission = cursor.fetchone()[0]
    cursor.close()

    if permission != "admin":
        return render_template("invalid_auth.html")
    else:
        airline_name_query = (
            "SELECT airline_name FROM airline_staff WHERE username = '{}';"
        )

        airplane_ids_query = "SELECT id FROM airplane WHERE airline_name = '{}';"
        airports_query = "SELECT name FROM airport;"

        cursor = mysql.cursor()
        cursor.execute(airline_name_query.format(staff_email))
        airline_name = cursor.fetchone()[0]
        cursor.close()

        cursor = mysql.cursor()
        cursor.execute(airplane_ids_query.format(airline_name))
        airplane_ids = [row[0] for row in cursor.fetchall()]
        cursor.close()

        cursor = mysql.cursor()
        cursor.execute(airports_query)
        airports = [row[0] for row in cursor.fetchall()]
        cursor.close()

        return render_template(
            "staff_create_flight.html", airplane_ids=airplane_ids, airports=airports
        )


@app.route("/createFlight", methods=["POST"])
def createFlight():
    airline_name_query = "SELECT airline_name FROM airline_staff WHERE username = '{}';"
    cursor = mysql.cursor()
    cursor.execute(airline_name_query.format(session["email"]))
    airline_name = cursor.fetchone()[0]
    cursor.close()

    flight_num = request.form["flight_num"]
    departure_airport = request.form["departure_airport"]
    departure_time = request.form["departure_time"]
    arrival_airport = request.form["arrival_airport"]
    arrival_time = request.form["arrival_time"]
    price = request.form["price"]
    airplane_id = request.form["airplane_id"]
    departure_status = request.form["departure_status"]

    # check if the flight already exists
    query = "SELECT * FROM flight WHERE flight_num = '{}';"
    cursor = mysql.cursor()
    cursor.execute(query.format(flight_num))
    data = cursor.fetchall()
    cursor.close()

    if data:
        error = "Flight with the given flight number already exists!"
        flash(error, "error")
        return redirect(url_for("home"))

    # check if any of the fields is empty
    if (
        flight_num == ""
        or departure_airport == "Select an airport..."
        or departure_time == ""
        or arrival_airport == "Select an airport..."
        or arrival_time == ""
        or price == ""
        or airplane_id == "Select an airplane ID..."
        or departure_status == "Select departure status..."
    ):
        error = "Please fill out all the fields!"
        flash(error, "error")
        return redirect(url_for("staffCreateFlight"))

    insert_query = "INSERT INTO flight (flight_num, departure_time, arrival_time, price, airplane_id, airline_name, departure_airport_name, arrival_airport_name, dep_status) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');"
    cursor = mysql.cursor()
    cursor.execute(
        insert_query.format(
            flight_num,
            departure_time,
            arrival_time,
            price,
            airplane_id,
            airline_name,
            departure_airport,
            arrival_airport,
            departure_status,
        )
    )
    mysql.commit()
    cursor.close()

    flash("Flight added successfully!", "success")
    return redirect(url_for("home"))


@app.route("/staff_change_flight_status")
def staffChangeFlightStatus():
    query = "SELECT permission, airline_name FROM airline_staff WHERE username = '{}';"
    staff_email = session["email"]

    cursor = mysql.cursor()
    cursor.execute(query.format(staff_email))
    output = cursor.fetchone()
    permission = output[0]
    print(permission)
    airline_name = output[1]
    cursor.close()

    cursor = mysql.cursor()
    query = "SELECT flight_num FROM flight WHERE airline_name = '{}';"
    cursor.execute(query.format(airline_name))
    flights = [row[0] for row in cursor.fetchall()]
    cursor.close()

    if permission == "admin" or permission == "operator":
        return render_template("staff_change_flight_status.html", flights=flights)
    else:
        return render_template("invalid_auth.html")


@app.route("/changeFlightStatus", methods=["POST"])
def changeFlightStatus():
    flight_num = request.form["flight_num"]
    flight_status = request.form["departure_status"]

    query = "SELECT airline_name FROM airline_staff WHERE username = '{}';"
    staff_email = session["email"]
    cursor = mysql.cursor()
    cursor.execute(query.format(staff_email))
    airline_name = cursor.fetchone()[0]
    cursor.close()

    # check if any of the fields is empty
    if flight_num == "" or flight_status == "Select departure status...":
        error = "Please fill out all the fields!"
        flash(error, "error")
        return redirect(url_for("staffChangeFlightStatus"))

    update_query = "UPDATE flight SET dep_status = '{}' WHERE flight_num = '{}' AND airline_name = '{}';"
    cursor = mysql.cursor()
    cursor.execute(update_query.format(flight_status, flight_num, airline_name))
    mysql.commit()
    cursor.close()

    flash("Flight status updated successfully!", "success")
    return redirect(url_for("home"))


@app.route("/flightSearchA", methods=["POST"])
def fligthSearchA():
    method = request.form["searchFactorA"]

    if method == "-- SELECT THE CRITERIA --":
        error = "No search criteria selected!"
        return render_template("main_page.html", error=error)

    cursor = mysql.cursor()

    if method == "Source City/Airport":
        query = "SELECT flight_num, airline_name, departure_airport_name, arrival_airport_name, departure_time, arrival_time, dep_status FROM flight WHERE departure_airport_name = '{}'"
        parameter = request.form["sourceCityA"]

    elif method == "Destination City/Airport":
        query = "SELECT flight_num, airline_name, departure_airport_name, arrival_airport_name, departure_time, arrival_time, dep_status FROM flight WHERE arrival_airport_name = '{}'"
        parameter = request.form["destinationCityA"]

    else:
        query = "SELECT flight_num, airline_name, departure_airport_name, arrival_airport_name, departure_time, arrival_time, dep_status FROM flight WHERE DATE(departure_time) = '{}'"
        parameter = request.form["dateA"]

    cursor.execute(query.format(parameter))
    data1 = cursor.fetchall()
    cursor.close()

    if len(data1) == 0:
        return render_template(
            "main_page.html",
            table_content=data1,
            error="No flights found for the given criteria. Try again!",
        )

    return render_template("main_page.html", table_content=data1)


@app.route("/flightSearchB", methods=["POST"])
def fligthSearchB():
    method = request.form["searchFactorB"]

    if method == "-- SELECT THE CRITERIA --":
        error = "No search criteria selected!"
        return render_template("main_page.html", error=error)

    cursor = mysql.cursor()

    if method == "Flight Number":
        parameter = request.form["flightNumber"]
        query = "SELECT flight_num, airline_name, departure_airport_name, arrival_airport_name, departure_time, arrival_time, dep_status FROM flight WHERE flight_num = '{}'"
        cursor.execute(query.format(parameter))
        data1 = cursor.fetchall()
        cursor.close()

    else:
        dateB = request.form["dateB"]
        if not dateB:
            return render_template(
                "main_page.html",
                table_content=[],
                error="Please select a date to search by.",
            )
        query = "SELECT flight_num, airline_name, departure_airport_name, arrival_airport_name, departure_time, arrival_time, dep_status FROM flight WHERE DATE(departure_time) = '{}'"
        parameter = dateB
        cursor.execute(query.format(parameter))
        data1 = cursor.fetchall()
        cursor.close()

    if len(data1) == 0:
        return render_template(
            "main_page.html",
            table_content=data1,
            error="No flights found for the given criteria. Try again!",
        )

    return render_template("main_page.html", table_content=data1)


@app.route("/customer_flight_search")
def customer_flight_search(error=None):
    cursor = mysql.cursor()

    query = "SELECT DISTINCT arrival_airport_name FROM flight"
    cursor.execute(query)
    arrival_airports = cursor.fetchall()

    query = "SELECT DISTINCT departure_airport_name FROM flight"
    cursor.execute(query)
    departure_airports = cursor.fetchall()

    query = "SELECT DISTINCT flight_num FROM flight"
    cursor.execute(query)
    flights = cursor.fetchall()

    cursor.close()
    return render_template(
        "customer_flight_search.html",
        flights=flights,
        departure_airport=departure_airports,
        arrival_airport=arrival_airports,
        error=error,
    )


@app.route("/customer_search", methods=["POST"])
def customer_search():
    cursor = mysql.cursor()

    query = "SELECT DISTINCT arrival_airport_name FROM flight"
    cursor.execute(query)
    arrival_airports = cursor.fetchall()

    query = "SELECT DISTINCT departure_airport_name FROM flight"
    cursor.execute(query)
    departure_airports = cursor.fetchall()

    query = "SELECT DISTINCT flight_num FROM flight"
    cursor.execute(query)
    all_flights = cursor.fetchall()

    cursor.close()

    # requesting searching parameters
    selected_flight = request.form["flights"]
    departure_airport = request.form["departure_airport"]
    arrival_airport = request.form["arrival_airport"]
    flight_date = request.form["flight_date"]

    cursor = mysql.cursor()

    flight_num_f = bool(selected_flight == "all")
    departure_airport_f = bool(departure_airport == "all")
    arrival_airport_f = bool(arrival_airport == "all")
    flight_date_f = bool(flight_date == "")

    attributes = []
    if not departure_airport_f:
        attributes.append('departure_airport_name = "{}"'.format(departure_airport))
    if not arrival_airport_f:
        attributes.append('arrival_airport_name = "{}"'.format(arrival_airport))
    if not flight_date_f:
        attributes.append('DATE(departure_time) = "{}"'.format(flight_date))
    if not flight_num_f:
        attributes.append('flight_num = "{}"'.format(selected_flight))

    # concatenate all the attributes and produce a query
    if len(attributes) > 0:
        for i in range(len(attributes)):
            if i == 0:
                query = (
                    "SELECT flight_num, airline_name, departure_airport_name, arrival_airport_name, departure_time, arrival_time, dep_status FROM flight WHERE "
                    + attributes[i]
                    + " AND dep_status = 'Upcoming'"
                )
            else:
                query = query + " AND " + attributes[i]
        query = query + " ORDER BY departure_time ASC;"
    else:
        return render_template(
            "customer_flight_search.html",
            flights=all_flights,
            departure_airport=departure_airports,
            arrival_airport=arrival_airports,
            error="At least one search parameter should be specified!",
        )

    cursor.execute(query)
    available_flights = cursor.fetchall()
    cursor.close()

    if len(available_flights) == 0:
        return render_template(
            "customer_flight_search.html",
            flights=all_flights,
            departure_airport=departure_airports,
            arrival_airport=arrival_airports,
            error="No flights found for the given criteria. Try again!",
        )

    cursor = mysql.cursor()
    available_seats = []

    for flight in available_flights:
        flight_num = flight[0]
        airline = flight[1]

        airplane_id_query = "SELECT airplane_id FROM flight WHERE airline_name = '{}' AND flight_num = '{}'".format(
            airline, flight_num
        )
        cursor.execute(airplane_id_query)
        # find the airplane id for that flight
        airplane_id = cursor.fetchone()[0]

        total_query = (
            "SELECT seats FROM airplane WHERE airline_name = '{}' AND id = '{}'".format(
                airline, airplane_id
            )
        )
        cursor.execute(total_query)
        # find how many seats in total for that flight
        total = cursor.fetchone()[0]

        sold_query = "SELECT COUNT(*) FROM ticket WHERE airline_name = '{}' AND  flight_id = '{}'".format(
            airline, flight_num
        )
        cursor.execute(sold_query)
        sold = int(
            cursor.fetchone()[0]
        )  # find how many tickets have been sold for that flight
        available = int(total) - sold
        available_seats.append(available)  # record the available seats for this flight

    for i in range(
        len(available_flights)
    ):  # append the available seats to the available flights
        original = list(available_flights[i])
        original.append(available_seats[i])
        new = tuple(original)
        available_flights[i] = new

    cursor.close()

    return render_template(
        "customer_flight_search.html",
        flights=all_flights,
        departure_airport=departure_airports,
        arrival_airport=arrival_airports,
        table_content=available_flights,
    )


@app.route("/agent_flight_search")
def agent_flight_search(error=None):
    cursor = mysql.cursor()

    query = "SELECT DISTINCT arrival_airport_name FROM flight"
    cursor.execute(query)
    arrival_airports = cursor.fetchall()

    query = "SELECT DISTINCT departure_airport_name FROM flight"
    cursor.execute(query)
    departure_airports = cursor.fetchall()

    query = "SELECT DISTINCT flight_num FROM flight"
    cursor.execute(query)
    flights = cursor.fetchall()

    cursor.close()
    return render_template(
        "agent_flight_search.html",
        flights=flights,
        departure_airport=departure_airports,
        arrival_airport=arrival_airports,
        error=error,
    )


@app.route("/agent_search", methods=["POST"])
def agent_search():
    agent_email = session["email"]
    airline_name_query = (
        "SELECT airline_name FROM booking_agent_work_for WHERE email = '{}'".format(
            agent_email
        )
    )
    cursor = mysql.cursor()
    cursor.execute(airline_name_query)
    airline_name = cursor.fetchone()[0]
    cursor.close()

    cursor = mysql.cursor()

    query = "SELECT DISTINCT arrival_airport_name FROM flight WHERE airline_name = '{}'".format(
        airline_name
    )
    cursor.execute(query)
    arrival_airports = cursor.fetchall()

    query = "SELECT DISTINCT departure_airport_name FROM flight WHERE airline_name = '{}'".format(
        airline_name
    )
    cursor.execute(query)
    departure_airports = cursor.fetchall()

    query = "SELECT DISTINCT flight_num FROM flight WHERE airline_name = '{}'".format(
        airline_name
    )
    cursor.execute(query)
    all_flights = cursor.fetchall()

    cursor.close()

    # requesting searching parameters
    selected_flight = request.form["flights"]
    departure_airport = request.form["departure_airport"]
    arrival_airport = request.form["arrival_airport"]
    flight_date = request.form["flight_date"]

    cursor = mysql.cursor()

    flight_num_f = bool(selected_flight == "all")
    departure_airport_f = bool(departure_airport == "all")
    arrival_airport_f = bool(arrival_airport == "all")
    flight_date_f = bool(flight_date == "")

    attributes = []
    if not departure_airport_f:
        attributes.append('departure_airport_name = "{}"'.format(departure_airport))
    if not arrival_airport_f:
        attributes.append('arrival_airport_name = "{}"'.format(arrival_airport))
    if not flight_date_f:
        attributes.append('DATE(departure_time) = "{}"'.format(flight_date))
    if not flight_num_f:
        attributes.append('flight_num = "{}"'.format(selected_flight))

    attributes.append('airline_name = "{}"'.format(airline_name))

    # concatenate all the attributes and produce a query
    if len(attributes) > 0:
        for i in range(len(attributes)):
            if i == 0:
                query = (
                    "SELECT flight_num, airline_name, departure_airport_name, arrival_airport_name, departure_time, arrival_time, dep_status FROM flight WHERE "
                    + attributes[i]
                    + " AND dep_status = 'Upcoming'"
                )
            else:
                query = query + " AND " + attributes[i]
        query = query + " ORDER BY departure_time ASC;"
    else:
        return render_template(
            "agent_flight_search.html",
            flights=all_flights,
            departure_airport=departure_airports,
            arrival_airport=arrival_airports,
            error="At least one search parameter should be specified!",
        )

    cursor.execute(query)
    available_flights = cursor.fetchall()
    cursor.close()

    if len(available_flights) == 0:
        return render_template(
            "agent_flight_search.html",
            flights=all_flights,
            departure_airport=departure_airports,
            arrival_airport=arrival_airports,
            error="No flights found for the given criteria. Try again!",
        )

    cursor = mysql.cursor()
    available_seats = []

    for flight in available_flights:
        flight_num = flight[0]
        airline = flight[1]

        airplane_id_query = "SELECT airplane_id FROM flight WHERE airline_name = '{}' AND flight_num = '{}'".format(
            airline, flight_num
        )
        cursor.execute(airplane_id_query)
        airplane_id = cursor.fetchone()[0]

        total_query = (
            "SELECT seats FROM airplane WHERE airline_name = '{}' AND id = '{}'".format(
                airline, airplane_id
            )
        )
        cursor.execute(total_query)
        # find how many seats in total for that flight
        total = cursor.fetchone()[0]

        sold_query = "SELECT COUNT(*) FROM ticket WHERE airline_name = '{}' AND  flight_id = '{}'".format(
            airline, flight_num
        )
        cursor.execute(sold_query)
        sold = int(
            cursor.fetchone()[0]
        )  # find how many tickets have been sold for that flight
        available = int(total) - sold
        available_seats.append(available)  # record the available seats for this flight

    for i in range(
        len(available_flights)
    ):  # append the available seats to the available flights
        original = list(available_flights[i])
        original.append(available_seats[i])
        new = tuple(original)
        available_flights[i] = new

    cursor.close()

    return render_template(
        "agent_flight_search.html",
        flights=all_flights,
        departure_airport=departure_airports,
        arrival_airport=arrival_airports,
        table_content=available_flights,
    )


@app.route("/agent_confirmation_page", methods=["GET", "POST"])
def agent_confirmation_page():
    flight_num = request.form["flight_num"]
    airline_name = request.form["airline"]
    departure_time = request.form["departure_time"]

    arrival_time = request.form["arrival_time"]
    departure_airport = request.form["departure_airport"]
    arrival_airport = request.form["arrival_airport"]

    price_query = "SELECT price FROM flight WHERE flight_num = '{}' AND airline_name = '{}' AND departure_time = '{}';".format(
        flight_num, airline_name, departure_time
    )
    cursor = mysql.cursor()
    cursor.execute(price_query)
    price = cursor.fetchone()[0]
    cursor.close()

    return render_template(
        "agent_purchase_confirmation_page.html",
        flight_num=flight_num,
        airline_name=airline_name,
        departure_time=departure_time,
        arrival_time=arrival_time,
        departure_airport=departure_airport,
        arrival_airport=arrival_airport,
        price=price,
    )


@app.route("/agent_purchase", methods=["POST"])
def agent_purchase():
    """
    for the simplicity purposes we'll have 10% fixed commission rate for all the agents
    """
    email = request.form["email"]

    # check if the customer exists
    query = "SELECT COUNT(*) FROM customer WHERE email = '{}';".format(email)
    cursor = mysql.cursor()
    cursor.execute(query)
    count = cursor.fetchone()[0]
    cursor.close()

    # in case the customer doesn't exist
    if count == 0:
        return agent_flight_search(
            error="The customer with the given email doesn't exist, try another one!"
        )

    booking_agent = session["email"]
    flight_num = request.form["flight_num"]
    airline_name = request.form["airline_name"]

    query = "SELECT COUNT(*) FROM ticket WHERE customer_email = '{}' AND flight_id = '{}' AND airline_name = '{}';".format(
        email, flight_num, airline_name
    )
    cursor = mysql.cursor()
    cursor.execute(query)
    count = cursor.fetchone()[0]
    cursor.close()

    # in case the user has already purchased that flight
    if count != 0:
        return agent_flight_search(
            error="This flight for the given customer already exists, try another one!"
        )

    else:
        # update ticket, purchases, ticket_by_booking_agents, commission_per_agent
        cursor = mysql.cursor()
        query = "INSERT INTO ticket (customer_email, airline_name, flight_id) VALUES ('{}', '{}', '{}');".format(
            email, airline_name, flight_num
        )
        cursor.execute(query)

        query = "SELECT id FROM ticket WHERE customer_email = '{}' AND airline_name = '{}' AND flight_id = '{}';".format(
            email, airline_name, flight_num
        )
        cursor.execute(query)
        ticket_id = cursor.fetchone()[0]

        query = "INSERT INTO purchases (ticket_id, customer_email, booking_agent_id, purchase_date) VALUES ('{}', '{}', '{}', CURDATE());".format(
            ticket_id, email, booking_agent
        )
        cursor.execute(query)

        commission = 0.1 * float(request.form["price"])
        insert_query = "INSERT INTO commission_per_agent (booking_agent_email, ticket_id, commission) VALUES ('{}', '{}', '{}');".format(
            booking_agent, ticket_id, commission
        )
        cursor.execute(insert_query)

        insert_query = "INSERT INTO tickets_by_booking_agent (booking_agent_email, ticket_id) VALUES ('{}', '{}');".format(
            booking_agent, ticket_id
        )
        cursor.execute(insert_query)
        # we commit once all of the insert operations are succesful
        mysql.commit()
        cursor.close()

        # display the confirmation message, and redirect to the home page
        flash("You have successfully purchased the flight!", "success")
        return redirect(url_for("home"))


@app.route("/agent_criteria_search", methods=["GET", "POST"])
def agent_criteria_search():
    email = session["email"]
    user_type = session["user_type"]

    airline_name_query = (
        "SELECT airline_name FROM booking_agent_work_for WHERE email = '{}'".format(
            email
        )
    )
    cursor = mysql.cursor()
    cursor.execute(airline_name_query)
    airline_name = cursor.fetchone()[0]

    query = "SELECT DISTINCT F.departure_airport_name FROM purchases as P JOIN ticket as T on P.ticket_id = T.id JOIN flight F on (T.flight_id = F.flight_num AND T.airline_name = F.airline_name) WHERE F.airline_name = '{}' AND P.booking_agent_id = '{}'"
    cursor.execute(query.format(airline_name, email))
    departure_airports = cursor.fetchall()

    query = "SELECT DISTINCT F.departure_airport_name FROM purchases as P JOIN ticket as T on P.ticket_id = T.id JOIN flight F on (T.flight_id = F.flight_num AND T.airline_name = F.airline_name) WHERE F.airline_name = '{}' AND P.booking_agent_id = '{}'"
    cursor.execute(query.format(airline_name, email))
    arrival_airports = cursor.fetchall()

    departure_airport = request.form["departure_airport"]
    arrival_airport = request.form["arrival_airport"]
    start_time = request.form["start-date"]
    end_time = request.form["end-date"]
    customer_email = request.form["customer_email"]

    cursor.close()
    cursor = mysql.cursor()

    departure_airport_f = bool(departure_airport == "all")
    arrival_airport_f = bool(arrival_airport == "all")
    start_date_f = bool(start_time == "")
    end_date_f = bool(end_time == "")

    # if start_date_f or end_date_f:
    #     flash("Please specify two dates for the range search!", "error")
    #     return redirect(url_for("home"))

    attributes = []
    if not departure_airport_f:
        attributes.append('departure_airport_name = "{}"'.format(departure_airport))
    if not arrival_airport_f:
        attributes.append('arrival_airport_name = "{}"'.format(arrival_airport))
    if not (start_date_f or end_date_f):
        attributes.append(
            "DATE(departure_time) BETWEEN '{}' AND '{}'".format(start_time, end_time)
        )

    attributes.append('F.airline_name = "{}"'.format(airline_name))
    attributes.append('P.booking_agent_id = "{}"'.format(email))
    attributes.append('T.customer_email = "{}"'.format(customer_email))

    # concatenate all the attributes and produce a query

    for i in range(len(attributes)):
        if i == 0:
            query = (
                "SELECT F.airline_name, F.flight_num, F.departure_airport_name, F.departure_time, F.arrival_airport_name, F.arrival_time, F.dep_status, T.customer_email FROM purchases as P JOIN ticket as T on P.ticket_id = T.id JOIN flight F on (T.flight_id = F.flight_num AND T.airline_name = F.airline_name) WHERE "
                + attributes[i]
                + " AND F.dep_status = 'Upcoming'"
            )
        else:
            query = query + " AND " + attributes[i]

    cursor.execute(query.format(airline_name, email))
    table_data = cursor.fetchall()
    cursor.close()

    if len(table_data) == 0:
        flash("No flights found for the given criteria. Try again!", "error")
        return redirect(url_for("home"))

    cursor = mysql.cursor()

    return render_template(
        "home.html",
        user_type=user_type,
        email=email,
        upcoming_flights=table_data,
        airline_name=airline_name,
        departure_airports=departure_airports,
        arrival_airports=arrival_airports,
    )


@app.route("/agent_view_commission")
def agent_view_commission():
    return render_template("agent_view_commission.html")


@app.route("/confirmation_page", methods=["GET", "POST"])
def confirmation_page():
    email = session["email"]
    flight_num = request.form["flight_num"]
    airline_name = request.form["airline"]
    departure_time = request.form["departure_time"]

    arrival_time = request.form["arrival_time"]
    departure_airport = request.form["departure_airport"]
    arrival_airport = request.form["arrival_airport"]

    price_query = "SELECT price FROM flight WHERE flight_num = '{}' AND airline_name = '{}' AND departure_time = '{}';".format(
        flight_num, airline_name, departure_time
    )
    cursor = mysql.cursor()
    cursor.execute(price_query)
    price = cursor.fetchone()[0]
    cursor.close()

    return render_template(
        "purchase_confirmation_page.html",
        email=email,
        flight_num=flight_num,
        airline_name=airline_name,
        departure_time=departure_time,
        arrival_time=arrival_time,
        departure_airport=departure_airport,
        arrival_airport=arrival_airport,
        price=price,
    )


@app.route("/customer_purchase", methods=["POST"])
def customer_purchase():
    email = session["email"]
    flight_num = request.form["flight_num"]
    airline_name = request.form["airline_name"]

    query = "SELECT COUNT(*) FROM ticket WHERE customer_email = '{}' AND flight_id = '{}' AND airline_name = '{}';".format(
        email, flight_num, airline_name
    )
    cursor = mysql.cursor()
    cursor.execute(query)
    count = cursor.fetchone()[0]
    cursor.close()

    # in case the user has already purchased that flight
    if count > 0:
        return customer_flight_search(
            error="You have already purchased this flight, try another one!"
        )

    else:
        # update both ticket and purchase tables
        cursor = mysql.cursor()
        query = "INSERT INTO ticket (customer_email, airline_name, flight_id) VALUES ('{}', '{}', '{}');".format(
            email, airline_name, flight_num
        )
        cursor.execute(query)
        query = "SELECT id FROM ticket WHERE customer_email = '{}' AND airline_name = '{}' AND flight_id = '{}';".format(
            email, airline_name, flight_num
        )
        cursor.execute(query)

        ticket_id = cursor.fetchone()[0]
        query = "INSERT INTO purchases (ticket_id, customer_email, purchase_date) VALUES ('{}', '{}', CURDATE());".format(
            ticket_id, email
        )
        cursor.execute(query)

        # we commit once all of the insert operations are succesful
        mysql.commit()
        cursor.close()

        # display the confirmation message, and redirect to the home page
        flash("You have successfully purchased the flight!", "success")
        return redirect(url_for("home"))


@app.route("/customer_customized_spending", methods=["POST"])
def customer_customized_spending():
    email = session["email"]
    start_date = request.form["start-date"]
    end_date = request.form["end-date"]

    if start_date == "" or end_date == "":
        error = "Specify the range! Results below are default results."
        flash(error, "error")
        return customer_spending()

    if start_date == "" and end_date != "":
        error = "Specify a start date! Results below are default results."
        flash(error, "error")
        return customer_spending()

    if start_date != "" and end_date == "":
        error = "Specify an end date! Results below are default results."
        flash(error, "error")
        return customer_spending()

    cursor = mysql.cursor()
    query = "SELECT SUM(F.price) as money_spent_per_month, YEAR(P.purchase_date) AS year, MONTH(P.purchase_date) AS month FROM purchases as P JOIN ticket as T on P.ticket_id = T.id JOIN flight as F ON F.flight_num = T.flight_id WHERE P.customer_email = '{}' AND P.purchase_date BETWEEN '{}' AND '{}' GROUP BY YEAR(P.purchase_date), MONTH(P.purchase_date) ORDER BY YEAR(P.purchase_date), MONTH(P.purchase_date);"
    cursor.execute(query.format(email, start_date, end_date))
    results = cursor.fetchall()
    cursor.close()

    total_amounts = []
    labels = []
    for result in results:
        total_amounts.append(result[0])
        labels.append(f"{result[1]}-{result[2]:02}")

    # Create a vertical bar chart
    with plt.ion():
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(labels, total_amounts)
        ax.set_xlabel("Month and Year")
        ax.set_ylabel("Total Amount")
        ax.set_title("Total Amount Spent per Month")
        ax.set_xticklabels(labels, rotation=45)

        # Display the exact value of each bar
        for i, v in enumerate(total_amounts):
            ax.text(i, v / 2, "${:.2f}".format(v), ha="center", fontsize=12)

    filename = "total_customer_spending.png"

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    fig.savefig(file_path)
    flash("Your customized spending chart has been generated!", "success")
    return render_template("customer_spending.html", filepath="/static/" + filename)


@app.route("/customer_spending")
def customer_spending():
    email = session["email"]
    cursor = mysql.cursor()
    default_query = "SELECT SUM(F.price) as money_spent_per_month, YEAR(P.purchase_date) AS year, MONTH(P.purchase_date) AS month FROM purchases as P JOIN ticket as T on P.ticket_id = T.id JOIN flight as F ON F.flight_num = T.flight_id WHERE P.customer_email = '{}' AND P.purchase_date >= DATE_SUB(NOW(), INTERVAL 6 MONTH) GROUP BY YEAR(P.purchase_date), MONTH(P.purchase_date) ORDER BY YEAR(P.purchase_date), MONTH(P.purchase_date);"

    cursor.execute(default_query.format(email))
    results = cursor.fetchall()
    cursor.close()

    total_amounts = []
    labels = []
    for result in results:
        total_amounts.append(result[0])
        labels.append(f"{result[1]}-{result[2]:02}")

    # Create a vertical bar chart
    with plt.ion():
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(labels, total_amounts)
        ax.set_xlabel("Month and Year")
        ax.set_ylabel("Total Amount")
        ax.set_title("Total Amount Spent per Month")
        ax.set_xticklabels(labels, rotation=45)

        # Display the exact value of each bar
        for i, v in enumerate(total_amounts):
            ax.text(i, v / 2, "${:.2f}".format(v), ha="center", fontsize=12)

    filename = "total_customer_spending.png"

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    fig.savefig(file_path)

    return render_template("customer_spending.html", filepath="/static/" + filename)


@app.route("/logout")
def logout():
    session.pop("email")
    session.pop("user_type")
    return render_template("/goodbye.html")


app.secret_key = "some key that you will never guess"
# Run the app on localhost port 5000
# debug = True -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
