-- a. One Airline name "China Eastern".
insert into
    airline (name)
values
    ("China Southern"),
    ("Delta"),
    ("China Eastern"),
    ("Emirates"),
    ("Air Canada"),
    ("Qatar Airlines"),
    ("Air Astana");

-- b. At least Two airports named "JFK" in NYC and "PVG" in Shanghai.
insert into
    airport (name, city)
values
    ("JFK", "New York"),
    ("PVG", "Shanghai"),
    ("LAX", "Los Angeles"),
    ("CDG", "Paris"),
    ("PEK", "Beijing"),
    ("HKG", "Hong Kong"),
    ("DXB", "Dubai"),
    ("LHR", "London"),
    ("ORD", "Chicago"),
    ("AMS", "Amsterdam"),
    ("FRA", "Frankfurt"),
    ("CAN", "Guangzhou"),
    ("SIN", "Singapore");

-- c. Insert at least two customers with appropriate names and other attributes.
insert into
    customer (
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
        date_of_birth
    )
values
    (
        "yan.k@nyu.edu",
        "Yan Konichshev",
        "123is_a_bad_password",
        "1",
        "Jane Street",
        "New York City",
        "New York",
        "61349087",
        "N7312058",
        "2030-11-20",
        "Kazakhstan",
        "2002-11-30"
    ),
    (
        "ll4715@nyu.edu",
        "Lawrence Lim",
        "1919192002020",
        "1019",
        "Lawrence Street",
        "Sometown",
        "New Jersey",
        "61349099",
        "N7312656",
        "2040-12-21",
        "The United States",
        "2002-04-15"
    ),
    (
        "jane.smith@gmail.com",
        "Jane Smith",
        "sdfg12345",
        "123",
        "Main Street",
        "Los Angeles",
        "California",
        "1234567890",
        "AB1234567",
        "2025-01-01",
        "United States",
        "1990-01-01"
    ),
    (
        "john.doe@yahoo.com",
        "John Doe",
        "yuiop09876",
        "456",
        "Second Street",
        "Paris",
        "Ile-de-France",
        "0987654321",
        "CD7654321",
        "2027-01-01",
        "France",
        "1985-01-01"
    );

-- Insert one booking agent with appropriate name and other attributes.
insert into
    booking_agent (email, password, booking_agent_id)
values
    ("bookingme@booking.com", "ghghuuj4", "12122"),
    ("traveler@booking.com", "qwerty12345", "67890");

-- d. Insert at least two airplanes.
insert into
    airplane (id, seats, airline_name)
values
    (1223445, 340, "China Southern"),
    (2122234, 120, "China Southern"),
    (11111, 200, "Delta"),
    (22222, 100, "Delta");

-- Each Airline Staff will also be able to see all in-progress, upcoming, and previous flights 
-- for the airline that they work for, as well as a list of passengers for the flights.
insert into
    permission (type, description)
values
    (
        "admin",
        "able to add new airplanes and flight for the airline they work for"
    ),
    (
        "operator",
        "set in progress flight statuses in the system"
    ),
    (
        "N/A",
        "ADMIN MANUALLY ASSIGNS NEW USER'S PERMISSION"
    );

-- e. Insert At least One airline Staff working for China Eastern.
insert into
    airline_staff (
        username,
        password,
        first_name,
        last_name,
        date_of_birth,
        airline_name,
        permission
    )
values
    (
        "number_1_employee",
        "dasda122dsdklsd!@@#)WEW",
        "Adam",
        "Krok",
        "1988-02-10",
        "China Southern",
        "admin"
    ),
    (
        "employee1",
        "password123",
        "Alice",
        "Johnson",
        "1990-05-10",
        "Delta",
        "operator"
    );

-- f. Insert several flights with upcoming, in-progress, delayed statuses.
insert into
    flight (
        flight_num,
        departure_time,
        arrival_time,
        price,
        airplane_id,
        airline_name,
        departure_airport_name,
        arrival_airport_name,
        dep_status
    )
values
    (
        'CS1020',
        '2023-03-15 12:05:00.000000',
        '2023-03-16 11:00:00.000000',
        250.50,
        1223445,
        'China Southern',
        'JFK',
        'PVG',
        'Upcoming'
    ),
    (
        'CS1021',
        '2023-03-15 12:05:00.000000',
        '2023-03-16 11:00:00.000000',
        500,
        2122234,
        'China Southern',
        'JFK',
        'PVG',
        'Delayed'
    ),
    (
        'CS1022',
        '2023-03-15 12:05:00.000000',
        '2023-03-16 11:00:00.000000',
        750,
        2122234,
        'China Southern',
        'PVG',
        'JFK',
        'In-Progress'
    ),
    (
        'DL1010',
        '2023-04-01 08:00:00.000000',
        '2023-04-01 11:00:00.000000',
        300,
        11111,
        'Delta',
        'LAX',
        'CDG',
        'Upcoming'
    ),
    (
        'DL2020',
        '2023-04-03 15:00:00.000000',
        '2023-04-03 18:00:00.000000',
        500,
        22222,
        'Delta',
        'CDG',
        'LAX',
        'Delayed'
    );

-- g. Insert some tickets for corresponding flights. One customer buy ticket directly 
-- and one customer buy ticket using a booking agent.
insert into
    ticket (
        -- id int primary key auto_increment not null, 
        customer_email,
        airline_name,
        flight_id
    )
values
    ("yan.k@nyu.edu", "China Southern", "CS1020"),
    ("ll4715@nyu.edu", "China Southern", "CS1021");

insert into
    tickets_by_booking_agent (booking_agent_email, ticket_id)
values
    ("bookingme@booking.com", 2);